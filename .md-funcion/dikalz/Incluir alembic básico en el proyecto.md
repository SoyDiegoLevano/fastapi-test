
Agregar la url luego de ejecutar alembic init

![[Pasted image 20250327182524.png]]

Se crea una base general que nos ayuda a llevar control sonbre las tablas que tienen conexión a la base de datos

![[Pasted image 20250327182705.png]]

En la forma de gestionar las bases de datos (al iniciar la app crear las bases de datos si no estan) no cambia 

![[Pasted image 20250327182908.png]]

Se importa la Base , Importa los modelos que usan la base para cargar su metadata y se guarda el target_metadata la Base.metadata

![[Pasted image 20250327182951.png]]

En los modelos ahora se usa la Base importada desde Infraestructura - DB - Base
![[Pasted image 20250327183102.png]]