✅ ¿ Qué es minio ?
	Es un sistema de almacenamiento de objetos compatible con la API de Amazon S3 se usa para almacenar archivos grandes, especialmente  en la nube o entornos empresariales.
	✔ **Ideal para almacenar cualquier tipo de archivo** (imágenes, PDFs, videos, etc.).  
	✔ **Compatible con la API de S3** (si en el futuro migras a Google Cloud, AWS o Yandex Cloud, será fácil).
	✔ **Puedes alojarlo en tu propio servidor gratis** y evitar pagar por tráfico de archivos.  
	✔ **Si usas un servidor externo, solo pagas almacenamiento y transferencia de datos**.
💰 **Costo:** Si lo instalas en tu propio VPS o en un servidor local, **es gratis** (solo pagas el servidor). En la nube, pagas por almacenamiento y salida de datos.

✅ INSTALACIÓN EN UBUNTO 22.04.07

🔹Documentación de MinIO https://min.io/docs/minio/linux/index.html

🔹VIDEO de referencia https://www.youtube.com/watch?v=IiljSW2Dvh4
	
```bash
## primero actualiza 
	sudo apt update
	sudo apt upgrade -y
	
## Descarga el binario de MinIO
	wget https://dl.min.io/server/minio/release/linux-amd64/minio

## Muestra todos los archivos ocultos y los activos
	ll

## Otorga permisos de Ejecución 
	chmod +x minio

## Para conectarte a minio
	sudo ./minio server /minioap
	
## Ahi te muestra tus credenciales
	RootUser: minioadmin 
	RootPass: minioadmin 

## Ingres en la siguiente URL y conectate
	API: http://192.168.20.128:9000  http://172.17.0.1:9000  http://127.0.0.1:9000
```


