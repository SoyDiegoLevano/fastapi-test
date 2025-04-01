# Objetivo

Integrar la API de Yandex Disk para permitir la carga, descarga y gestión de archivos de una aplicación de chat de manera eficiente.
## Requisitos previo

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Tener una conexión estable a Internet.
- Contar con conocimientos básicos de Python.
- Tener instalada la biblioteca `requests` en Python (`pip install requests`).
- Tener una cuenta en Yandex Disk.
- Obtener un `client_id` y un `access_token` para la API.
#### 1. Crea una cuenta 

Para utilizar la API de Yandex Disk, primero debes crear una cuenta:

1. Ingresa a [Yandex Disk](https://360.yandex.com/disk/).
2. Regístrate con tu correo electrónico y crea una cuenta.
3. Una vez dentro, accede a tu disco para familiarizarte con su interfaz.
4. Video por si sea necesario https://www.youtube.com/watch?v=nn3Ziy6biYo&t=196s?
#### 2. Configuración de la Aplicación de Yandex

Para acceder a la API, debes crear una aplicación en el portal de Yandex OAuth.

5. Accede a [Yandex OAuth](https://oauth.yandex.com/client/new).
6. Crea una nueva aplicación y proporciona los siguientes detalles:
    - **Nombre de la Aplicación**: Elige un nombre representativo.
    - **Tipo de Aplicación**: Selecciona "Web Service".
    - **Permisos (Scopes)**: Marca las siguientes opciones:
        - `cloud_api:disk.read` → Permite leer archivos. 
        - `cloud_api:disk.write` → Permite escribir archivos.
        - `cloud_api:disk.app_folder` → Accede a una carpeta específica de la aplicación.
7. Guarda la configuración y copia el `client_id` generado.
#### 3. Obtener el Token de Acceso

Para autenticarte en la API, debes obtener un `access_token`. Sigue estos pasos:

8. Genera la URL de autorización:
`https://oauth.yandex.com/authorize?response_type=token&client_id=TUIDAQUIENTUID`
**Nota:** Reemplaza `TUIDAQUIENTUID` por el `client_id` que copiaste en el paso anterior.

9. Abre la URL en tu navegador y concede permisos a la aplicación.
10. Luego de autorizar, serás redirigido a una página con el `access_token`. Cópialo y guárdalo de manera segura.
#### 4. Implementación del Código

- Usar una biblioteca `yasdisk` para interactuar con el api de `Yandex Disk`
- Implementar funciones para verificar la conexión, listar archivos y obtener información del disco.
#### 5. Implementación del código detallado

##### 1. Importaciones y Configuración Inicial

```bash
import yadisk
python test_yandex.py
```
- `yadisk`: Biblioteca para interactuar con la api de Yandex Disk.

##### 2. Funciones para Obtener la URL de Autorización

```python
def get_auth_url():
    client_id = "0cc84ae60e454d8a9fd8ac6274598700"
    client_secret = "c1f3b9aa9eb743039ab20323b70ab2d7"
    
    # Construir la URL de autorización manualmente usando los scopes oficiales
    scopes = "cloud_api:disk.read%20cloud_api:disk.write%20cloud_api:disk.app_folder"
    auth_url = f"https://oauth.yandex.com/authorize?response_type=token&client_id={client_id}&scope={scopes}"
    
    print("✅ URL de autorización generada:")
    print(auth_url)
    print("\n1. Abre esta URL en tu navegador")
    print("2. Inicia sesión si es necesario")
    print("3. Autoriza la aplicación")
    print("4. Copia el token que aparece en la URL después de 'access_token='")
```
- Objetivo: Genera una URL que el usuario deba  abrir  para autorizar la aplicación y obtener el token.
- Scopes: Especifican los permisos que la aplicación necesita.
##### 3. Funciones para verificar la Conexión y Listar Archivos

```python
def test_connection():
    token = "y0__xDHyaPqBxjblgMgv9mImBIfeFZPwKlXV9UD5IiQCaMXB6TFqg"
    
    try:
        # Inicializar el cliente con el token
        y = yadisk.YaDisk(token=token)
        
        # Verificar si el token es válido
        if y.check_token():
            print("✅ Conexión exitosa con Yandex Disk!")
            
            # Obtener información del disco
            info = y.get_disk_info()
            print("\n📂 Información del disco:")
            print(f"Espacio total: {info['total_space'] / (1024**3):.2f} GB")
            print(f"Espacio usado: {info['used_space'] / (1024**3):.2f} GB")
            print(f"Espacio libre: {(info['total_space'] - info['used_space']) / (1024**3):.2f} GB")
            
            print("\n📁 Archivos y carpetas:")
            print("-----------------------")
            
            try:
                # Listar archivos y directorios
                items = list(y.listdir("/"))
                if not items:
                    print("El directorio está vacío")
                else:
                    for item in items:
                        prefix = "📂" if item.type == "dir" else "📄"
                        if item.type == "file":
                            size_mb = item.size / (1024 * 1024)
                            print(f"{prefix} {item.name} ({size_mb:.2f} MB)")
                        else:
                            print(f"{prefix} {item.name}/")
            except Exception as e:
                print(f"Error al listar archivos: {str(e)}")
            
            return True
        else:
            print("❌ Token inválido")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False
```
- Objetivo: Verificar la conexión con Yandex Disk y listar archivos en el directorio de la raíz.
- Verificación de Token: Asegura que el token sea válido antes de realizar operaciones.
##### 4. Ejecución del código

```python
if __name__ == "__main__":
    test_connection()
```
- Objetivo: Ejecutar la función de conexión la iniciar el script

## Conclusión

En este código has logrado integrar integrar Yandex Disk en tu aplicación, permitiendo la verificación de conexión y la visualización de archivos. Ahora, puedes procesar a implementar funciones adicionales como cargar y descargar archivos.


# Yandex Disk Configuration
YANDEX_DISK_TOKEN=y0__xDHyaPqBxjblgMgv9mImBIfeFZPwKlXV9UD5IiQCaMXB6TFqg
YANDEX_DISK_CHAT_DIR=/chat_files
YANDEX_TOKEN_REFRESH_URL=https://oauth.yandex.com/token
YANDEX_CLIENT_ID=0cc84ae60e454d8a9fd8ac6274598700
YANDEX_CLIENT_SECRET=c1f3b9aa9eb743039ab20323b70ab2d7

### LINKS

nphne-2cfc5yy3@yandex.ru
JTQxhX966bpdR*v
https://oauth.yandex.com/client/0cc84ae60e454d8a9fd8ac6274598700

https://www.youtube.com/watch?v=nn3Ziy6biYo&t=196s&ab_channel=BiMineMinecraftServer%21
https://yandex.ru/dev/disk/poligon#access_token=y0__xDIoqTqBxjblgMg8paJmBKalBvICV430zHz6TsK0OuJ2Yd_vg&token_type=bearer&expires_in=31536000&cid=3zfgbxgmcg361qz9hkahx4kyem

https://disk.yandex.com/client/disk
https://oauth.yandex.com/
https://yadisk.readthedocs.io/en/latest/intro.html#




[yandex_minio]
token = {"access_token":"y0__xCry-zvBxjCpQsg5P3ooBIF4Z5jP8NFKlnpSbGKeDiV5Ze-7g","token_type":"bearer","refresh_token":"1:ixzU8ygGvEtq2XV9:WpVEzEQQXJD9X5z-1ZYETWD0OZOicuRo7mXFCG9YFszPPV8zcnLPDyZp4DabHOWZI_xp5kg:YUfkog8KjIuj1ZdPDSspkA","expiry":"2026-02-12T09:10:47.269065433-05:00"}