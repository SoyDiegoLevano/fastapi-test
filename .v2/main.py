from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
import strawberry 
import jwt
import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Optional

# Configuración
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

DATABASE_URL = "dbname=bd-test user=postgres password=postgres host=localhost"

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

# Seguridad
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# GraphQL Schema
@strawberry.type
class Query:
    @strawberry.field
    def secure_data(self, info) -> str:
        user = info.context["user"]
        if not user:
            raise HTTPException(status_code=401, detail="No autorizado")
        return f"Hola {user['username']}, este es un dato seguro."

@strawberry.type
class Mutation:
    @strawberry.mutation
    def login(self, username: str, password: str) -> str:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if not user or not verify_password(password, user['password']):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        token = create_access_token({"username": user["username"]})
        return token

    @strawberry.mutation
    def register(self, username: str, password: str) -> str:
        hashed_password = get_password_hash(password)
        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
                (username, hashed_password)
            )
            new_id = cursor.fetchone()["id"]
            conn.commit()
            return "Usuario registrado"
        except psycopg2.IntegrityError:
            conn.rollback()
            raise HTTPException(status_code=400, detail="Usuario ya existe")
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error interno del servidor")

schema = strawberry.Schema(query=Query, mutation=Mutation)

def get_current_user(authorization: Optional[str] = Header(None)) -> Optional[dict]:
    if not authorization:
        raise HTTPException(status_code=401, detail="Token requerido")
     
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None

    token = parts[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"username": payload["username"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

def context_dependency(user=Depends(get_current_user)):
    return {"user": user}

# Configurar FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(GraphQLRouter(schema, context_getter=context_dependency), prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
