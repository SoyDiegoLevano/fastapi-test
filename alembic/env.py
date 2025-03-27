from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv
from app.infrastructure.db.base import Base

load_dotenv()  # Si usas variables de entorno

# Este es el objeto de configuración de Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa la Base unificada
from app.infrastructure.db.base import Base

from app.user.infrastructure.models.model import UserModel
from app.product.infrastructure.models.model import ProductModel


# Actualizar la URL de conexión dinámicamente usando tus variables de entorno
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
config.set_main_option("sqlalchemy.url", DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
