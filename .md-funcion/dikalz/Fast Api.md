
1. Datos en el Body (Cuerpo de la Solicitud)

Qué sucede:
Cuando envías datos en el cuerpo de la solicitud (por ejemplo, en formato JSON), FastAPI automáticamente intenta mapear ese JSON a los parámetros de la función que esperan un modelo Pydantic.

Ejemplo en tu endpoint:

```ts
@router.post("/orders", response_model=Order)
async def create_order(order: OrderCreate, use_case: OrderUseCase = Depends(get_order_use_case)):
    return await use_case.create_order(order)
```
	Aquí, el parámetro order es de tipo OrderCreate. Esto le indica a FastAPI que:

Extraiga el cuerpo de la solicitud (el JSON).
Convierta ese JSON en un diccionario.
Cree una instancia de OrderCreate pasando ese diccionario, lo cual también hace que se validen los datos (tipos, campos requeridos, etc.) según lo definido en OrderCreate.
Resumen:
Todo lo que envíes en el body se asignará al parámetro order si usas un modelo Pydantic como OrderCreate.

2. Datos en Parámetros de Consulta (Query Parameters)
Qué sucede:
Los parámetros de consulta son los que van en la URL después del signo ? (por ejemplo, /orders?page=2).

Cómo recibirlos:
Si defines en tu función un parámetro simple (como un entero o cadena) que no está presente en la ruta, FastAPI lo interpretará como un query parameter.

Ejemplo:
```ts
@router.get("/orders")
async def list_orders(page: int = 1, search: str = None):
    # page y search se extraen de la URL, ej.: /orders?page=2&search=abc
    return {"page": page, "search": search}
```

Resumen:
Los query parameters se asignan a los parámetros de la función que sean de tipos simples (int, str, etc.) y no estén en la ruta ni se especifiquen de otra forma.

3. Datos en Parámetros de Ruta (Path Parameters)
Qué sucede:
Los parámetros de ruta son parte de la URL misma. Por ejemplo, en una ruta como /orders/{order_id}, order_id es un parámetro de ruta.

Cómo recibirlos:
Se definen en la ruta y se reciben en la función con el mismo nombre.

Ejemplo:
```ts
@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    # order_id se extrae de la URL, ej.: /orders/123
    return {"order_id": order_id}
```
Resumen:
Los parámetros en la ruta se asignan a los parámetros de la función correspondientes.

4. Otros Métodos de Envío de Datos
Form Data:
Si envías datos desde un formulario HTML, puedes recibirlos usando la dependencia Form().

```ts
from fastapi import Form

@router.post("/submit")
async def submit_form(name: str = Form(...)):
    return {"name": name}
```

Archivos (Files):
Para recibir archivos, se utiliza File() o UploadFile.

```ts
from fastapi import File, UploadFile

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```
Headers:
Si necesitas datos de las cabeceras HTTP, usas Header().

```ts
from fastapi import Header

@router.get("/headers")
async def read_headers(user_agent: str = Header(None)):
    return {"User-Agent": user_agent}
```

Cookies:
Para leer datos de las cookies, puedes utilizar Cookie().

```ts
from fastapi import Cookie

@router.get("/cookies")
async def read_cookies(session_id: str = Cookie(None)):
    return {"session_id": session_id}
```

Conclusión
Cuerpo de la Solicitud (Body):
Los datos enviados en el body (normalmente en JSON) se reciben en el parámetro order porque está tipado como OrderCreate. FastAPI se encarga de leer el body, convertirlo en un diccionario y crear una instancia del modelo.

Query y Path Parameters:
Se reciben como parámetros simples en la función, ya sea desde la URL (query parameters) o desde la parte dinámica de la ruta (path parameters).

Otros Tipos de Datos:
Además del body, puedes enviar y recibir datos a través de formularios, archivos, headers o cookies utilizando las dependencias correspondientes.






### Fast no tiene un administrador como Django Admin

FastAPI, a diferencia de Django, no viene con un panel de administración incorporado. Sin embargo, tienes varias alternativas para lograr una funcionalidad similar y gestionar la configuración de tu sistema (como tipos de servicios, etapas, roles, métodos de pago, etc.):

1. **Usar una librería de administración para FastAPI:**
    
    - **FastAPI-Admin:**  
        Es una solución de terceros que ofrece un panel de administración similar a Django Admin. Te permite definir modelos, gestionar usuarios, roles y configuraciones, y se integra con bases de datos (usualmente a través de SQLAlchemy o Tortoise ORM).  
        Puedes ver más en [FastAPI-Admin en GitHub](https://github.com/fastapi-admin/fastapi-admin).
        
    - **SQLAdmin:**  
        Otra opción (especialmente si usas SQLAlchemy) es SQLAdmin, que ofrece una interfaz administrativa para gestionar tus modelos de forma similar a Django Admin.
        
2. **Crear tu propio módulo administrativo:**
    
    - Puedes desarrollar endpoints CRUD específicos para la administración de las configuraciones de tu aplicación.
    - Con FastAPI y Pydantic, puedes construir formularios, vistas y rutas protegidas (usando autenticación y autorización) para que los administradores configuren y actualicen parámetros del sistema.
    - Puedes incluso usar plantillas con Jinja2 para renderizar interfaces web si prefieres una experiencia más visual, aunque esto implica más desarrollo manual.
3. **Integrar con un CMS o solución externa:**
    
    - Otra opción es utilizar algún CMS o panel administrativo externo y conectarlo a tu base de datos. Esto puede ser útil si ya tienes experiencia con alguna solución y solo necesitas gestionar ciertos datos.


### Fast no tiene proceso de migracion

En FastAPI no hay un comando de migración integrado, pero lo más habitual es usar una herramienta externa como **Alembic** para manejar las migraciones de esquema de la base de datos cuando modificas tus modelos (por ejemplo, al agregar campos como ruc y email).

Esta distinción es crucial:

- Las migraciones son para evolucionar schemas existentes cuando la estructura de la base de datos cambia.
### ¿Qué debes hacer?

1. **Instalar Alembic:**
      
    `pip install alembic`
    
2. **Inicializar Alembic en tu proyecto:**

    `alembic init alembic`
    
    Esto creará una carpeta `alembic` y un archivo `alembic.ini`.
    
3. **Configurar Alembic:**
    
    - Abre el archivo `alembic.ini` y actualiza la variable `sqlalchemy.url` para que apunte a tu DATABASE_URL (o configúralo en el archivo env.py).
        
    - En el archivo `alembic/env.py`, asegúrate de que la variable `target_metadata` esté asignada a la metadata de tus modelos, por ejemplo:
 
        `from app.database import Base  # Asegúrate de importar la Base común que usas en todos tus modelos  target_metadata = Base.metadata`
        
	### Seguir estos pasos:

1 - Ubicarse en el archivo `alembic.ini` y no asignarle un valor vacío:

`sqlalchemy.url = 

2 - Ubicarse en el archivo `alembic/.env`

```
from alembic import context
import os
from app.infrastructure.db.database import Base



load_dotenv(".env.local")

# Actualizar la URL de conexión dinámicamente usando tus variables de entorno
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
config.set_main_option("sqlalchemy.url", DATABASE_URL)



target_metadata = Base.metadata

```
        
4. **Generar una migración:**
    
    Una vez que hayas modificado tus modelos (por ejemplo, agregaste ruc y email a Tenant), ejecuta:
    
    `alembic revision --autogenerate -m "Agregar campos ruc y email a Tenant"`
    
    Alembic analizará los cambios en tu metadata y generará un archivo de migración con las instrucciones necesarias (por ejemplo, ALTER TABLE para agregar columnas).
    
5. **Aplicar la migración:**

    `alembic upgrade head`
    
    Esto actualizará tu base de datos aplicando la migración generada.


6. **Generar una migración:**
    
    Para futuras modificaciones en sus modelos, simplemente haga los cambios en sus archivos de modelo y luego ejecute::
    
    `alembic revision --autogenerate -m "Agregar campos ruc y email a Tenant"`
    
    Alembic analizará los cambios en tu metadata y generará un archivo de migración con las instrucciones necesarias (por ejemplo, ALTER TABLE para agregar columnas).
    
7. **Aplicar la migración:**

    `alembic upgrade head`
    
    Esto actualizará tu base de datos aplicando la migración generada.





```ts

from logging.config import fileConfig
import os
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from app.core.config import settings
from sqlalchemy.engine import Connection
from sqlalchemy import pool
from alembic import context

from app.tenants.infrastructure.db.database import Base
from app.tenants.infrastructure.models.models import SiteSetting, Tenant
from app.tenants.infrastructure.db.db_config import DATABASE_URL

# Importa los modelos de Order y Customer
from app.order.infrastructure.models.model import OrderModel, OrderItemModel
from app.customer.infrastructure.models.model import CustomerModel

# Cargar variables de entorno desde .env.local
load_dotenv(".env.local")

# Configuración de Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

# Crear una URL síncrona a partir de la URL asíncrona para Alembic
sync_url = DATABASE_URL.replace('postgresql+asyncpg', 'postgresql')
config.set_main_option("sqlalchemy.url", sync_url)

def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

def include_object(object, name, type_, reflected, compare_to):
    """Filtra los objetos para incluir únicamente tablas en el esquema 'public' o sin esquema."""
    if type_ == "table":
        allowed_schema = settings.DEFAULT_TENANT_SUBDOMAIN
        return object.schema in [None, allowed_schema]
    return True

def run_migrations_online() -> None:
    """Ejecuta las migraciones en modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            compare_type=True
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```