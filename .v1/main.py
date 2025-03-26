
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from v1.isgraphql.database import init_db, get_db
from isgraphql.schema import schema  # Importa el esquema que definiste en graphql/schema.py
from fastapi.middleware.cors import CORSMiddleware

# Define los orígenes permitidos (ajusta según necesites)
origins = [
    "http://localhost", 
    "http://127.0.0.1",
    "http://127.0.0.1:5500"
]

# Inicializa la base de datos (crea las tablas si es necesario)
init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],    # Permite todos los métodos
    allow_headers=["*"],    # Permite todos los headers
)
# Función para inyectar el contexto con la sesión de la DB
def get_context():
    return {"db": next(get_db())}

# Configurar el router de GraphQL en FastAPI
graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/graphql")

# Agregar una ruta en la raíz para confirmar que el servidor está funcionando
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API GraphQL. Usa /graphql para interactuar."}


