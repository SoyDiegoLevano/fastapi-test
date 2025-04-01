YAN## ¿Qué es Rclone?

Rclone es un programa que nos ayuda a mover, copiar y ver archivos en la nube, como si fuera una carpeta en la computadora.
## ¿Qué hicimos?

Vamos a explicar paso a paso lo que hicimos en la terminal para conectar Yandex Disk con Rclone.

---
## 1. Instalamos Rclone

Escribimos este comando en la terminal:

```
sudo apt install rclone -y
```

- `sudo` significa que estamos usando permisos de administrador.
    
- `apt install rclone` le dice a la computadora que instale Rclone.
    
- `-y` hace que diga "sí" automáticamente a cualquier pregunta.
    
**Salida en la terminal:** La computadora nos dice que ya tenemos la última versión de Rclone instalada.

---
## 2. Configuramos Rclone

Escribimos este comando en la terminal:

```
rclone config
```

Nos aparece un menú donde podemos hacer varias cosas. Como es la primera vez, elegimos `n` para crear un nuevo "remote" (conexión a la nube).

![[Pasted image 20250212095529.png]]

Escribimos un nombre para la conexión:

```
yandex_minio
```

Luego, nos pide que elijamos el tipo de almacenamiento. Como estamos usando Yandex Disk, escribimos:

![[Pasted image 20250212095700.png]]
![[Pasted image 20250212095758.png]]
```
32
```

Nos pregunta si queremos ingresar un `client_id` y un `client_secret`. Como no los necesitamos, simplemente presionamos **Enter**.

---
## 3. Autorizamos el acceso a Yandex Disk

Nos pregunta si queremos usar `auto config` y elegimos `y` (sí). Esto abre un enlace en el navegador. link: http://127.0.0.1:53682/auth?state=avguAZg3hYNeiqqK-XPMjg esa url te genera en la misma terminal

- **Abrimos el enlace en el navegador.**
    
- **Ingresamos nuestra cuenta de Yandex y damos permiso a Rclone.**
    
- **La terminal recibe un código y termina la configuración.**

- **Recibirás un código como este**

```bash
If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=avguAZg3hYNeiqqK-XPMjg
Log in and authorize rclone for access
Waiting for code...
Got code
--------------------
[yandex_minio]
token = {"access_token":"y0__xCry-zvBxjCpQsg5P3ooBIF4Z5jP8NFKlnpSbGKeDiV5Ze-7g","token_type":"bearer","refresh_token":"1:ixzU8ygGvEtq2XV9:WpVEzEQQXJD9X5z-1ZYETWD0OZOicuRo7mXFCG9YFszPPV8zcnLPDyZp4DabHOWZI_xp5kg:YUfkog8KjIuj1ZdPDSspkA","expiry":"2026-02-12T09:10:47.269065433-05:00"}
```

- **Luego te saldrá comandos como este :**

```bash
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y
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
e/n/d/r/c/s/q> q # se presiona q para salir
```
---
## 4. Revisamos nuestra conexión

Para ver si la conexión funciona, escribimos:

```
rclone lsd yandex_minio:
```

La terminal nos muestra que existe una carpeta llamada `chat_files`.

Para ver los archivos dentro de esa carpeta, escribimos:

```
rclone ls yandex_minio:/chat_files/
```

La terminal nos muestra archivos con su tamaño y nombre, como:

```
    28 20250211_182921_test_file.txt
    82706 20250211_190742_paris.png
    12499 20250211_191117_images.jpeg
    11515 20250211_192755_images (1).jpeg
```

---
## 5. ¿Qué significa cada comando?

- `rclone lsd yandex_minio:` → Lista las carpetas dentro de Yandex Disk.
    
- `rclone ls yandex_minio:/chat_files/` → Muestra los archivos dentro de la carpeta `chat_files`.
---
## 6. Conclusión

Hemos instalado Rclone, conectado Yandex Disk y visto los archivos almacenados en la nube. Ahora podemos usar comandos de Rclone para copiar, mover o descargar archivos de manera fácil.

## Aquí muestro la terminal completa por siacaso

```bash
elsa@elsa-virtual-machine:~$ sudo apt install rclone -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
rclone is already the newest version (1.53.3-4ubuntu1.22.04.3).
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.
elsa@elsa-virtual-machine:~$ rclone config
2025/02/12 08:51:51 NOTICE: Config file "/home/elsa/.config/rclone/rclone.conf" not found - using defaults
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> yandex_minio
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
Storage> 32
** See help for yandex backend at: https://rclone.org/yandex/ **

OAuth Client Id
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_id> 
OAuth Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret> 
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n> n
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes (default)
n) No
y/n> y
If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=avguAZg3hYNeiqqK-XPMjg
Log in and authorize rclone for access
Waiting for code...
Got code
--------------------
[yandex_minio]
token = {"access_token":"y0__xCry-zvBxjCpQsg5P3ooBIF4Z5jP8NFKlnpSbGKeDiV5Ze-7g","token_type":"bearer","refresh_token":"1:ixzU8ygGvEtq2XV9:WpVEzEQQXJD9X5z-1ZYETWD0OZOicuRo7mXFCG9YFszPPV8zcnLPDyZp4DabHOWZI_xp5kg:YUfkog8KjIuj1ZdPDSspkA","expiry":"2026-02-12T09:10:47.269065433-05:00"}
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y
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
e/n/d/r/c/s/q> q
elsa@elsa-virtual-machine:~$ rclone lsd yandex_minio:
2025/02/12 09:14:37 Automatically upgraded OAuth config.
           0 2025-02-11 18:29:20        -1 chat_files
elsa@elsa-virtual-machine:~$ rclone ls yandex_minio:/chat_files/
       28 20250211_182921_test_file.txt
    82706 20250211_190742_paris.png
    12499 20250211_191117_images.jpeg
    11515 20250211_192755_images (1).jpeg
elsa@elsa-virtual-machine:~$ ^C
elsa@elsa-virtual-machine:~$ 

```