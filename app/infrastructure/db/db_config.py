# app/infrastructure/db/db_config.py
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

# Importamos el "Base" de nuestro modelo (puedes importar más bases si tienes varias)
from app.product.infrastructure.models.model import Base as ProductBase

load_dotenv()

DB_NAME = os.getenv("DATABASE_NAME", "my_database")
DB_USER = os.getenv("DATABASE_USER", "postgres")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
DB_HOST = os.getenv("DATABASE_HOST", "localhost")
DB_PORT = os.getenv("DATABASE_PORT", "5432")

# URL de conexión asíncrona (para uso en la app)
ASYNC_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 1. Creamos un engine síncrono para verificar/crear la BD y tablas.
sync_engine = create_engine(ASYNC_DATABASE_URL.replace("+asyncpg", ""))

# Verificar si existe la BD, si no, crearla
if not database_exists(sync_engine.url):
    create_database(sync_engine.url)

# Crear las tablas si no existen (en este caso, las de ProductBase)
ProductBase.metadata.create_all(sync_engine)

# 2. Creamos el engine asíncrono (que sí se usará en la aplicación)
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True, future=True)

# 3. Creamos la sesión asíncrona
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            # La sesión se cierra automáticamente al salir del contexto
            pass