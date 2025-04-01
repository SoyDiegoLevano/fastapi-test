
El flujo básico pensado de la aplicación es

Cualquier usuario rellena un formulario, el formulario puede ser Tipo1(Persona) y Tipo2(Empresa)
Se validan que todos los datos estén rellenados
Se acepta el envio a la api

La api extrae un campo dependiendo de que tipo de formulario sea Tipo1(DNI) y Tipo2(RUC) y se manda a validar el campo a un proceso externo

Nos devuelve true o false

Si es true 

Se almacenan todos los cambos en la BD junto a un proceso de admision que estará en "en proceso" por defecto 

Estos datos se consumen desde otro frontend, se puede ver la tabla de información de la persona o empresa que quiere ser admitida adicionalmente para cada persona hay un botón de aceptar y cancelar

Si se le da aceptar

Se envía a la API una respuesta 
La api al recibir la respuesta de admitir (idadmision) y el tipo si es tipo 1 o tipo 2 empieza un proceso un proceso nuevo donde 
Se envia a un proceso externo donde se envia la informacion del nombre de la empresa (si es tipo2) y nombre de la persona (si es tipo1) 
Esto nos devuelve true o false
Si es true se agrega al registro de la base de datos en admision como "admitido" si es false se coloca como "error registro" continuando con si es true
Y se enviara un correo al correo registrado
para esto se invoca una funcion enviaremail(Tipo, nombre)
En el que debemos mandarle el tipo de dato que es
Si es tipo 1
Se llama a la funcion enviaremailpersona(nombre)
La funcion a su vez llama a un template de correo para persona en html y agrega el nombre para luego enviarlo 
una vez enviado devuelve true 
Si se tipo 2
Se llama a la funcion enviaremailempre(nombre)
La funcion a su vez llama a un template de correo para empresa en html y agrega el nombre para luego enviarlo 
una vez enviado devuelve true 


Si es false

Se le muestra un mensaje en el frontend del formulario (no se ha podido comprobar su identidad)



#### **1. Ingreso de Datos**

- Un usuario completa un formulario, que puede ser:
    - **Tipo 1**: Persona (requiere DNI).
    - **Tipo 2**: Empresa (requiere RUC).
        
- Se validan que todos los campos estén completos.
    
- Si faltan datos, se muestra un error en el frontend y no se envía el formulario.
    
- Si los datos son correctos, se envían a la API.
    

#### **2. Validación Inicial**

- La API extrae el identificador clave según el tipo:
    - **Tipo 1**: DNI.
    - **Tipo 2**: RUC.
        
- Se manda a validar con un proceso externo.
    
- Si la validación falla, se devuelve un mensaje al frontend:  
    **"No se ha podido comprobar su identidad"**.
    
- Si la validación es exitosa:
    - Se almacenan los datos en la base de datos.
    - Se crea un registro de admisión con estado **"en proceso"**.
        

#### **3. Evaluación en el Segundo Frontend**

- Otro frontend permite visualizar la tabla con las solicitudes en estado `"en proceso"`.
- Cada registro tiene botones de **"Aceptar"** y **"Cancelar"**.
    

#### **4. Aprobación Manual**

- Si un administrador presiona **"Aceptar"**:
    
    - Se envía a la API la solicitud de admisión con:
        - `id_admision`
        - `tipo` (Tipo 1 o Tipo 2).
            
    - La API realiza una segunda validación externa enviando:
        - **Tipo 1**: Nombre de la persona.
        - **Tipo 2**: Nombre de la empresa.
            
    - Si la validación externa devuelve **false**, el estado de admisión cambia a **"error registro"**.
        
    - Si la validación externa devuelve **true**, el estado de admisión cambia a **"admitido"**.
        

#### **5. Envío de Correo**

- Si el usuario es admitido, se envía un correo de confirmación según el tipo:
    
    - **Tipo 1**:
        - Se llama a `enviaremailpersona(nombre)`.
        - Se usa un template de correo para personas.
            
    - **Tipo 2**:
        - Se llama a `enviaremailempre(nombre)`.
        - Se usa un template de correo para empresas.
            
- Si el correo se envía correctamente, finaliza el proceso.

Consideraciones Adicionales
- Indexar DNI RUC email
- Rate Limit
- Uvicorn Asincrono
- Tanto usuarios como empresa estan dentro de la misma tabla solo que se nunea DNI y viceversa si es empresa 
- Para los procesos externos colocale una funcion que devuelva true solo si no menciono que hace ese proceso

``` python
from fastapi import FastAPI, Depends
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=lambda request: request.client.host)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/submit")
@limiter.limit("5/minute")  # Máximo 5 envíos por minuto por IP
async def submit_form(data: dict):
    return {"message": "Formulario recibido"}
```

```python
### **Usar un Servidor Asíncrono (Uvicorn con Gunicorn)**

- FastAPI es asíncrono, por lo que puedes usar **Uvicorn con Gunicorn** (`gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app`) para manejar múltiples conexiones concurrentes.
    
- Ajusta el número de workers según la cantidad de CPU disponibles.
```