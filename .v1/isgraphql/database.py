from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Parámetros de conexión (ajusta según tu entorno)
user = "postgres"
pssw = "postgres"
host = "localhost"
port = "5432"
db_name = "bd-test"

DATABASE_URL = f"postgresql://{user}:{pssw}@{host}:{port}/{db_name}"

# Crear el engine y la sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definición del modelo
class ItemDB(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    is_offer = Column(Boolean, default=False)

# Función para inicializar la DB (crea las tablas si no existen)
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
