## Introducción

¡Hola! Vamos a explicar paso a paso cómo configurar MinIO con Rclone de una manera muy sencilla. Imagina que estás armando tu juguete favorito - ¡vamos a hacerlo pieza por pieza! 🧩
## Paso 1: Iniciar la Configuración

Cuando escribes:

`rclone config`

Es como decirle a Rclone: "¡Hola! Quiero configurar algo nuevo contigo" 👋

Y Rclone te muestra un menú con opciones:

```bash
rclone config
Current remotes:
Name                 Type
====                 ====
yandex_minio         yandex
```

Esto es como una lista de tus juguetes actuales. En este caso, ya tienes configurado Yandex.
## Paso 2: Crear una Nueva Configuración

Cuando te muestra:
```bash
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
```

Es como preguntarte: "¿Qué quieres hacer?"
- 'n' es para crear algo nuevo (como abrir una caja de juguetes nueva)
- 'e' es para cambiar algo que ya tienes
- 'd' es para tirar algo que ya no quieres
- 'r' es para cambiarle el nombre
- 'q' es para decir "ya terminé"
## Paso 3: Elegir un Nombre

Cuando escribes:
```bash
e/n/d/r/c/s/q> n
name> minio
```

Es como ponerle nombre a tu nuevo juguete. En este caso, le pusimos "minio" 🏷️
## Paso 4: Elegir el Tipo de Almacenamiento

```bash
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, Tencent COS, etc)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Citrix Sharefile
   \ "sharefile"
 9 / Dropbox
   \ "dropbox"
10 / Encrypt/Decrypt a remote
   \ "crypt"
```

Cuando eliges:

`Storage> 4`

Estás eligiendo el tipo de juguete. El número 4 es para "Amazon S3", que es como decir "quiero un juguete que funcione como MinIO" 🎮
## Paso 5: Elegir el Proveedor

```bash 
Choose your S3 provider.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Amazon Web Services (AWS) S3
   \ "AWS"
 2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
   \ "Alibaba"
 3 / Ceph Object Storage
   \ "Ceph"
 4 / Digital Ocean Spaces
   \ "DigitalOcean"
 5 / Dreamhost DreamObjects
   \ "Dreamhost"
 6 / IBM COS S3
   \ "IBMCOS"
 7 / Minio Object Storage
   \ "Minio"
 8 / Netease Object Storage (NOS)
   \ "Netease"
 9 / Scaleway Object Storage
   \ "Scaleway"
10 / StackPath Object Storage
   \ "StackPath"
11 / Tencent Cloud Object Storage (COS)
   \ "TencentCOS"
12 / Wasabi Object Storage
   \ "Wasabi"
13 / Any other S3 compatible provider
   \ "Other"
```

Cuando seleccionas:

`provider> 7`

Estás diciendo específicamente "quiero usar MinIO". Es como elegir la marca específica de tu juguete 🎯
## Paso 6: Configurar la Autenticación

```bash 
#En este paso, debes seleccionar **"false"** para ingresar manualmente las credenciales de MinIO, ya que no estás usando las credenciales de AWS, sino las de MinIO.

Get AWS credentials from runtime (environment variables or EC2/ECS meta data if no env vars).
Only applies if access_key_id and secret_access_key is blank.
Enter a boolean value (true or false). Press Enter for the default ("false").
Choose a number from below, or type in your own value
 1 / Enter AWS credentials in the next step
   \ "false"
 2 / Get AWS credentials from the environment (env vars or IAM)
   \ "true"
```

Cuando te pregunta sobre `env_auth`:

`env_auth> false`

Es como decir "voy a poner yo mismo las llaves para abrir mi juguete" en vez de usar llaves que ya están guardadas 🔑
## Paso 7: Configurar las Credenciales

Cuando ingresas `false` automáticamente te pedirá el `access_key_id` y `secret_access_key`:

```bash
#AWS Access Key ID.
#Leave blank for anonymous access or runtime credentials.
#Enter a string value. Press Enter for the default ("").
access_key_id> minioadmin
#AWS Secret Access Key (password)
#Leave blank for anonymous access or runtime credentials.
#Enter a string value. Press Enter for the default ("").
secret_access_key> minioadmin
```

Es como poner el nombre de usuario y la contraseña. Son las llaves especiales para que solo tú puedas usar tu juguete 🗝️
## Paso 8: Configurar la Región

```bash
#Leave blank if you are using an S3 clone and you don't have a region.
#Enter a string value. Press Enter for the default ("").
#Choose a number from below, or type in your own value
 1 / Use this if unsure. Will use v4 signatures and an empty region.
   \ ""
 2 / Use this only if v4 signatures don't work, eg pre Jewel/v10 CEPH.
   \ "other-v2-signature"
region> 
```

Cuando dejas en blanco la región:

`region>`

Es como decir "mi juguete está aquí mismo, no necesito decir dónde está" 📍
## Paso 9: Configurar el Endpoint

```bash
#Required when using an S3 clone.
#Enter a string value. Press Enter for the default ("").
#Choose a number from below, or type in your own value
endpoint> http://192.168.20.128:9000
#Location constraint - must be set to match the Region.
#Leave blank if not sure. Used when creating buckets only.
#Enter a string value. Press Enter for the default ("").
location_constraint> 
```

Cuando escribes:

`endpoint> http://192.168.20.128:9000`

Es como decirle a Rclone dónde está tu MinIO. Es la dirección de tu casa de juguetes 🏠
## Paso 10: Configurar los Permisos (ACL)

```bash
#Choose a number from below, or type in your own value
	#**private**: Solo el propietario del bucket tiene control total sobre el objeto, nadie más tiene acceso (opción por defecto).
 1 / Owner gets FULL_CONTROL. No one else has access rights (default).
   \ "private"
   #**public-read**: El propietario tiene control total y el público tiene acceso de solo lectura. **Usado comúnmente para archivos públicos**.
 2 / Owner gets FULL_CONTROL. The AllUsers group gets READ access.
   \ "public-read"
   #**public-read-write**: El propietario tiene control total, pero el público tiene acceso completo (lectura y escritura). **No recomendado por razones de seguridad**.
   / Owner gets FULL_CONTROL. The AllUsers group gets READ and WRITE access.
 3 | Granting this on a bucket is generally not recommended.
   \ "public-read-write"
   #**authenticated-read**: El propietario tiene control total y solo los usuarios autenticados tienen acceso de lectura.
 4 / Owner gets FULL_CONTROL. The AuthenticatedUsers group gets READ access.
   \ "authenticated-read"
   #**bucket-owner-read**: El propietario del bucket tiene acceso de lectura, aunque no sea el propietario del objeto.
   / Object owner gets FULL_CONTROL. Bucket owner gets READ access.
 5 | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ "bucket-owner-read"
   / Both the object owner and the bucket owner get FULL_CONTROL over the object.
   #**bucket-owner-full-control**: El propietario del bucket tiene control total sobre el objeto.
 6 | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ "bucket-owner-full-control"
```

Cuando eliges:

`acl> 4`

Estás eligiendo quién puede jugar con tus juguetes. La opción 4 significa que solo las personas que conoces pueden ver tus juguetes 👥
## Paso 11: Configurar el Cifrado

```bash
#Choose a number from below, or type in your own value

#**None**: No se usará cifrado, los objetos se almacenarán en texto claro. **Opción predeterminada** si no necesitas cifrado.
 1 / None
   \ ""
#**AES256**: Se utiliza el algoritmo de cifrado **AES-256** para proteger los datos de manera que solo los usuarios autorizados puedan acceder a ellos.
 2 / AES256
   \ "AES256"
#**aws:kms**: Utiliza el servicio de **AWS Key Management Service (KMS)** para gestionar las claves de cifrado, lo que te da un mayor control sobre el acceso y administración de las claves de cifrado.
 3 / aws:kms
   \ "aws:kms"
server_side_encryption> 2
```

Cuando eliges:

`server_side_encryption> 2`

Es como poner un candado especial en tus juguetes para que estén más seguros. El número 2 significa que usarás un candado muy fuerte llamado AES256 🔒
## Paso 12: Finalizar la Configuración

```bash
Choose a number from below, or type in your own value
 1 / None
   \ ""
 2 / arn:aws:kms:*
   \ "arn:aws:kms:us-east-1:*"
sse_kms_key_id> None
```

Selecciona :

`**"None"** o simplemente presiona **Enter** para omitir este paso.`

###### Cuando te pregunta por la configuración avanzada:

Significa que estás a punto de ajustar configuraciones adicionales que no son necesarias para la configuración básica, pero que podrían ser útiles en escenarios más específicos.

Si no necesitas configuraciones avanzadas adicionales, como optimización de rendimiento o configuraciones personalizadas, lo mejor es seleccionar **"n"** para continuar con la configuración predeterminada.

```bash
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n> n
Remote config
```

###### Ahora que tienes la configuración final, te están dando tres opciones:

```bash
Remote config
--------------------
[minio]
provider = Minio
env_auth = false
access_key_id = minioadmin
secret_access_key = minioadmin
endpoint = http://192.168.20.128:9000
acl = authenticated-read
server_side_encryption = AES256
sse_kms_key_id = None
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
```

- **"y"**: Confirma que la configuración es correcta y se guarda.
- **"e"**: Permite editar nuevamente la configuración.
- **"d"**: Elimina esta configuración y la cancela.

Cuando eliges:

`y/e/d> y`

Es como decir "¡Sí, todo está bien! Guardemos esta configuración" ✅

**Finalmente nos imprime esto**

```bash
Current remotes:
Name                 Type
====                 ====
minio                s3
yandex_minio         yandex

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q # para cerrar la terminal
```
## ¿Qué Sigue?

Ahora que has terminado, puedes:

1. Ver tus archivos con: `rclone ls minio:`
2. Copiar archivos a MinIO
3. Sincronizar archivos entre MinIO y otros lugares

## Comandos Útiles

### Para Ver tus Archivos

`rclone ls minio:`

Es como abrir tu caja de juguetes para ver qué hay dentro 📦
### Para Copiar un Archivo

`rclone copy archivo.txt minio:`

Es como poner un juguete nuevo en tu caja 📥
### Para Sincronizar Archivos

`rclone sync carpeta_local minio:carpeta_remota`

Es como asegurarte de que todos tus juguetes están en el lugar correcto 🔄
## Conclusión

¡Felicitaciones! 🎉 Has configurado MinIO con Rclone. Ahora puedes guardar y mover tus archivos como si fueran juguetes en diferentes cajas. ¡Es fácil y divertido! 🌟


### AQUÍ TE DEJO LA TERMINAL COMPLETA

```bash
elsa@elsa-virtual-machine:~$ rclone config
Current remotes:

Name                 Type
====                 ====
yandex_minio         yandex

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> n
name> minio
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, Tencent COS, etc)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Citrix Sharefile
   \ "sharefile"
 9 / Dropbox
   \ "dropbox"
10 / Encrypt/Decrypt a remote
   \ "crypt"
11 / FTP Connection
   \ "ftp"
12 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
13 / Google Drive
   \ "drive"
14 / Google Photos
   \ "google photos"
15 / Hubic
   \ "hubic"
16 / In memory object storage system.
   \ "memory"
17 / Jottacloud
   \ "jottacloud"
18 / Koofr
   \ "koofr"
19 / Local Disk
   \ "local"
20 / Mail.ru Cloud
   \ "mailru"
21 / Microsoft Azure Blob Storage
   \ "azureblob"
22 / Microsoft OneDrive
   \ "onedrive"
23 / OpenDrive
   \ "opendrive"
24 / OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
25 / Pcloud
   \ "pcloud"
26 / Put.io
   \ "putio"
27 / SSH/SFTP Connection
   \ "sftp"
28 / Sugarsync
   \ "sugarsync"
29 / Transparently chunk/split large files
   \ "chunker"
30 / Union merges the contents of several upstream fs
   \ "union"
31 / Webdav
   \ "webdav"
32 / Yandex Disk
   \ "yandex"
33 / http Connection
   \ "http"
34 / premiumize.me
   \ "premiumizeme"
35 / seafile
   \ "seafile"
Storage> 4
** See help for s3 backend at: https://rclone.org/s3/ **

Choose your S3 provider.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Amazon Web Services (AWS) S3
   \ "AWS"
 2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
   \ "Alibaba"
 3 / Ceph Object Storage
   \ "Ceph"
 4 / Digital Ocean Spaces
   \ "DigitalOcean"
 5 / Dreamhost DreamObjects
   \ "Dreamhost"
 6 / IBM COS S3
   \ "IBMCOS"
 7 / Minio Object Storage
   \ "Minio"
 8 / Netease Object Storage (NOS)
   \ "Netease"
 9 / Scaleway Object Storage
   \ "Scaleway"
10 / StackPath Object Storage
   \ "StackPath"
11 / Tencent Cloud Object Storage (COS)
   \ "TencentCOS"
12 / Wasabi Object Storage
   \ "Wasabi"
13 / Any other S3 compatible provider
   \ "Other"
provider> 7
Get AWS credentials from runtime (environment variables or EC2/ECS meta data if no env vars).
Only applies if access_key_id and secret_access_key is blank.
Enter a boolean value (true or false). Press Enter for the default ("false").
Choose a number from below, or type in your own value
 1 / Enter AWS credentials in the next step
   \ "false"
 2 / Get AWS credentials from the environment (env vars or IAM)
   \ "true"
env_auth> false
AWS Access Key ID.
Leave blank for anonymous access or runtime credentials.
Enter a string value. Press Enter for the default ("").
access_key_id> minioadmin
AWS Secret Access Key (password)
Leave blank for anonymous access or runtime credentials.
Enter a string value. Press Enter for the default ("").
secret_access_key> minioadmin
Region to connect to.
Leave blank if you are using an S3 clone and you don't have a region.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Use this if unsure. Will use v4 signatures and an empty region.
   \ ""
 2 / Use this only if v4 signatures don't work, eg pre Jewel/v10 CEPH.
   \ "other-v2-signature"
region> 
Endpoint for S3 API.
Required when using an S3 clone.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
endpoint> http://192.168.20.128:9000
Location constraint - must be set to match the Region.
Leave blank if not sure. Used when creating buckets only.
Enter a string value. Press Enter for the default ("").
location_constraint> 
Canned ACL used when creating buckets and storing or copying objects.

This ACL is used for creating objects and if bucket_acl isn't set, for creating buckets too.

For more info visit https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl

Note that this ACL is applied when server side copying objects as S3
doesn't copy the ACL from the source but rather writes a fresh one.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Owner gets FULL_CONTROL. No one else has access rights (default).
   \ "private"
 2 / Owner gets FULL_CONTROL. The AllUsers group gets READ access.
   \ "public-read"
   / Owner gets FULL_CONTROL. The AllUsers group gets READ and WRITE access.
 3 | Granting this on a bucket is generally not recommended.
   \ "public-read-write"
 4 / Owner gets FULL_CONTROL. The AuthenticatedUsers group gets READ access.
   \ "authenticated-read"
   / Object owner gets FULL_CONTROL. Bucket owner gets READ access.
 5 | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ "bucket-owner-read"
   / Both the object owner and the bucket owner get FULL_CONTROL over the object.
 6 | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ "bucket-owner-full-control"
acl> 4
The server-side encryption algorithm used when storing this object in S3.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / None
   \ ""
 2 / AES256
   \ "AES256"
 3 / aws:kms
   \ "aws:kms"
server_side_encryption> 2
If using KMS ID you must provide the ARN of Key.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / None
   \ ""
 2 / arn:aws:kms:*
   \ "arn:aws:kms:us-east-1:*"
sse_kms_key_id> None
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n> n
Remote config
--------------------
[minio]
provider = Minio
env_auth = false
access_key_id = minioadmin
secret_access_key = minioadmin
endpoint = http://192.168.20.128:9000
acl = authenticated-read
server_side_encryption = AES256
sse_kms_key_id = None
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y
Current remotes:

Name                 Type
====                 ====
minio                s3
yandex_minio         yandex

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q
elsa@elsa-virtual-machine:~$ rclone ls minio:
181298 produccion/rusia.jpg

```