# User/Infrastructure/Persistence/postgres_user_repository.py
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional
from User.Domain.user import User

# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos desde .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Conectar a PostgreSQL
conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
""")
conn.commit()

class PostgresUserRepository:
    def get_user_by_username(self, username: str) -> Optional[User]:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result:
            return User(id=result["id"], username=result["username"], password=result["password"])
        return None

    def create_user(self, username: str, hashed_password: str) -> User:
        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
                (username, hashed_password)
            )
            new_id = cursor.fetchone()["id"]
            conn.commit()
            return User(id=new_id, username=username, password=hashed_password)
        except psycopg2.IntegrityError:
            conn.rollback()
            raise Exception("Usuario ya existe")
        except Exception:
            conn.rollback()
            raise Exception("Error interno del servidor")
