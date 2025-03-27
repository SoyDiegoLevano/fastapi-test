Aquí tienes una lista completa de los comandos de **Alembic**, incluyendo los más utilizados y otros que pueden ser útiles en ciertos escenarios.

---

## 📌 **Comandos más utilizados en Alembic**

### 🔹 **Inicialización y Configuración**

- `alembic init <directorio>`  
    👉 Crea la estructura de directorios y archivos necesarios para Alembic.  
    _Ejemplo:_ `alembic init alembic`
    

### 🔹 **Creación y Gestión de Migraciones**

- `alembic revision -m "mensaje"`  
    👉 Crea un archivo de migración vacío con el mensaje especificado.  
    _Ejemplo:_ `alembic revision -m "Crear tabla users"`
    
- `alembic revision --autogenerate -m "mensaje"`  
    👉 Genera automáticamente un script de migración comparando los modelos de SQLAlchemy con la base de datos.  
    _Ejemplo:_ `alembic revision --autogenerate -m "Agregar campo email a users"`
    

### 🔹 **Aplicación y Reversión de Migraciones**

- `alembic upgrade <revisión>`  
    👉 Aplica una migración específica o todas hasta la última (`head`).  
    _Ejemplo:_ `alembic upgrade head`
    
- `alembic downgrade <revisión>`  
    👉 Revierte la base de datos a una versión anterior. Puedes usar `-1` para deshacer solo la última migración.  
    _Ejemplo:_ `alembic downgrade -1`
    

### 🔹 **Gestión del Historial de Migraciones**

- `alembic current`  
    👉 Muestra la versión actual de la base de datos.
    
- `alembic history`  
    👉 Lista el historial de migraciones en orden cronológico.
    
- `alembic heads`  
    👉 Muestra todas las revisiones que están en la "cabeza" (última migración en cada rama).
    
- `alembic show <revisión>`  
    👉 Muestra detalles sobre una revisión específica.
    
- `alembic stamp <revisión>`  
    👉 Marca la base de datos con una revisión sin ejecutar la migración (para sincronizar versiones).  
    _Ejemplo:_ `alembic stamp head`
    

---

## 📌 **Todos los comandos de Alembic**

### 🔹 **Configuración y Estructura**

- `alembic init <directorio>`  
    📌 Inicializa un nuevo entorno de Alembic.
    
- `alembic ensure_version`  
    📌 Crea la tabla `alembic_version` en la base de datos si no existe.
    
- `alembic edit <revisión>`  
    📌 Abre un archivo de migración en el editor predeterminado.
    

### 🔹 **Revisiones y Migraciones**

- `alembic revision -m "mensaje"`  
    📌 Crea un nuevo archivo de migración.
    
- `alembic revision --autogenerate -m "mensaje"`  
    📌 Genera una migración basada en los cambios detectados en los modelos.
    
- `alembic upgrade <revisión>`  
    📌 Aplica una migración.
    
- `alembic downgrade <revisión>`  
    📌 Revierte una migración.
    
- `alembic stamp <revisión>`  
    📌 Marca una migración sin aplicarla.
    
- `alembic merge <revisión1> <revisión2> -m "mensaje"`  
    📌 Fusiona múltiples revisiones en una sola.
    

### 🔹 **Inspección del Estado de Migraciones**

- `alembic current`  
    📌 Muestra la versión actual de la base de datos.
    
- `alembic history`  
    📌 Lista el historial de migraciones.
    
- `alembic heads`  
    📌 Muestra las revisiones más recientes.
    
- `alembic branches`  
    📌 Muestra las ramas de migración existentes.
    
- `alembic show <revisión>`  
    📌 Muestra detalles de una revisión específica.
    
- `alembic check`  
    📌 Verifica si hay problemas en las migraciones.
    

### 🔹 **Depuración y Desarrollo**

- `alembic downgrade -1`  
    📌 Revierte solo la última migración.
    
- `alembic upgrade +1`  
    📌 Aplica solo la siguiente migración.
    
- `alembic upgrade head --sql`  
    📌 Muestra el SQL que se ejecutaría en la migración sin aplicarla.
    

---

## 📌 **Resumen**

|Comando|Descripción|
|---|---|
|`alembic init <dir>`|Inicializa Alembic en un proyecto|
|`alembic revision -m "mensaje"`|Crea una migración vacía|
|`alembic revision --autogenerate -m "mensaje"`|Genera una migración automáticamente|
|`alembic upgrade head`|Aplica todas las migraciones pendientes|
|`alembic downgrade -1`|Revierte la última migración|
|`alembic current`|Muestra la versión actual|
|`alembic history`|Lista todas las migraciones|
|`alembic stamp head`|Marca la base de datos en la última versión|

---

Con esta lista, tienes un **resumen completo** de los comandos más comunes y avanzados en **Alembic**. 🚀