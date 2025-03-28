Se quiere implementar FastAPI + GraphQL + JWT + Arq. Exagonal + PostgreSQL

La estructura de carpetas se ve de esta manera, actualmente contiene solo una tabla que viene a ser products y no contiene la validacion con JWT

```
└── app
    ├── graphql
    │   └── schema.py
    ├── infrastructure
    │   └── db
    │       └── db_config.py
    │           └── db_config.cpython-312.pyc
    ├── main.py
    ├── product
    │   ├── application
    │   │   ├── create_product.py
    │   │   └── get_product.py
    │   │       ├── create_product.cpython-312.pyc
    │   │       └── get_product.cpython-312.pyc
    │   ├── domain
    │   │   ├── entities.py
    │   │   │   ├── entities.cpython-312.pyc
    │   │   │   └── repository.cpython-312.pyc
    │   │   └── repository.py
    │   └── infrastructure
    │       ├── adapters
    │       │   ├── graphql
    │       │   │   ├── mutations.py
    │       │   │   │   ├── mutations.cpython-312.pyc
    │       │   │   │   ├── queries.cpython-312.pyc
    │       │   │   │   ├── resolvers.cpython-312.pyc
    │       │   │   │   └── types.cpython-312.pyc
    │       │   │   ├── queries.py
    │       │   │   ├── resolvers.py
    │       │   │   ├── types.py
    │       │   │   └── sqlalchemy_product_repository.cpython-312.pyc
    │       │   └── sqlalchemy_product_repository.py
    │       └── models
    │           └── model.py
    └── main.py
```

### Detalle del Flujo y Rol de cada Capa

#### 1. Capa de Infraestructura

##### 1.1 db_config.py
- Carga las variables de entorno del .env y asigna valores por defecto si no los encuentra
- Ejecuta un engine síncrono (el responsable de ejecutar acciones en la base de datos) para verificar si la base de datos existe
- Crea las tablas definidas en el modelo si no las encuentra (como Products Model)
	![[Pasted image 20250326145445.png]]
- Luego tenemos la función que nos permite crear una sesión de conexión a la base de datos que puede usarse asincronamente y se elimina al dejar de usarse (no bloquea las demás consultas al ejecutarse) (se pueden utilizar mas workers para mejorar la eficiencia de la aplicación en producción)
- Las sesiones se cierran automáticamente

#### 2. Capa de Dominio
###### 2.1 entities.py
- Se importa BaseModel el cual no va a ayudar a validar la entrada ssegun la anotacion de tipos que nosotros estamos haciendo.
- Se crea la entidad principal con sus atributos y tipos de datos
- Se crea el metodo from_orm que nos permite pasar un objeto creado por el orm a la entidad dominio y luego crear una nueva  instancia a travez de los datos brindados, esto se logra con el cls (forma de hacer referencia a la misma clase como self en metodos de instancia)
- Solo tienen los atributos mas no los tipos de relacion o informacion de como se almacenan como podria ser (index, primarykay, nueable etc)
	![[Pasted image 20250326151042.png]]
- Aunque el mismo Pydantic te proporciona la clase from_orm y solo es necesario activarlo (from_attributes) y no crear uno manual
	![[Pasted image 20250326152047.png]]
- Define los DTOs los cuales nos ayudan a limitar los datos necesarios al recibir o enviar por solicitud, de esta manera evitamos el envio innesarios de datos o que nos inyectes datos a traves de estas APIs
##### 2.2 repository.py
- Repository en este caso RepositoryProduct va a definir la interfaz plantilla de las implementaciones que debe cumplir el que realiza la persistencia de datos
- Especifica los métodos que deben existir, tipos de parametros () y retornos ->
- No contienen lógica de aplicación
	![[Pasted image 20250326161840.png]]

#### 3. Capa Aplicación

##### 3.1 create_product.py
- Define la clase CreateProduct que es el que se encarga de recibir y enviar a que se cree el producto
- Recibe el repositorio a travez de un parametro (no recibe como tal el repositorio si no mas bien compara lo recibido para que cumpla con el repositorio establecido y cumpla todos los metodos, argumentos y formas de retorno)
- Al ejecutarse lo hace a travez de la instancia (self) donde manda al repositorio(el que cumple con la platilla repositorio en este caso SQLAlchemi) y manda a crear el producto en este caso
	![[Pasted image 20250326162948.png]]
##### 3.2 get_product.py 
- Hace lo mismo que el create product.py pero en este caso solo para hacer un get (una consulta)
	![[Pasted image 20250326163124.png]]
#### 4. Capa de Infraestructura (Persistencia)

##### 4.1 model.py
- Define el modelo ProductModel usando SQLAlchemy que mapea la entidad a la tabla products
- No incluye logica de negocio en este archivo (no como lo hace entities)
- Debe tener todos sus atributos claros para hacer una conversion factible a la base de datos
	![[Pasted image 20250326164354.png]]
	
##### 4.2 sqlalchemy_product_repository.py

- En este caso como estamos usando sqlalchemy es el encargado de guardar los datos en la base de datos, podría ser cambiado fácilmente si así se quisiera
- Primero la clase se declara como subclase de el repositorio ProductRepository por lo que debe cumplir con todos los métodos definidos (se impone las reglas del juego) 
- Al utilizar la clase de sqlalchemy se le debe pasar una sesion la cual se guardara en el objeto actual de la clase (una instancia) lo cual permite guardar y acceder a los metodos de esta instancia como self.session

- Aqui se pasa de entidades al modelo usado para subirse a la base de datos o leidos por el orm
- Para el metodo create pasaremos como argumento, product_data que debe estar en formato ProductCreateDTO que es una entidad de como y que datos se debe subir para luego armar el objeto ProductModel
- Luego el objeto creado se sube -> self.session.add(aquí) que se puede interpretar como un create (en ORM)
- Luego se hace un commit para que lo cambios se realicen en la base de datos
- Luego con un refresh todos los datos nuevos de la base de datos generados (como lo es el id) se guardan en la instancia que habias utilizado para insertar
- Finalmente se retorna utilizando una funcion que lo hace pasar de un modelo a una entidad de dominio (porque de esta manera se trabaja sin depender del ORM o como se este guardado en la Base de Datos)
	![[Pasted image 20250326170828.png]]

#### 5. GraphQL
##### 5.1 types.py
- Define la estructura de datos de entrada y de salida de la API ya que quien más lo usa es GraphQL, por ejemplo define que tipos de datos debe enviar el cliente para poder crear, actualizar, eliminar o ver un productos.
- También valida la salida de datos, valida que tipo de datos va mandar la API en respuesta
- Ayuda a la segurar de los datos a que no salgan ni entren datos innecesarios y hagan más compleja la aplicacion
	![[Pasted image 20250326174436.png]]

##### 5.2 resolvers.py
- Son los encargados de conectar la parte que realiza las modificaciones en la base de datos(ORM, consultas SQL) y los que se encargan de gestionar estos metodos, pueden ser create, get, filter, etc (Aplicación -> "CreateProduct") que antes de ejecutar el método confirman que se este cumpliendo con la plantilla - repositorio (domain -> repository) y luego ejecutan el metodo
- Los resolver son como un almacen donde se guardan todos los métodos que funcionan indiferentemente si son queries (consultas, filtros) o modificadores (crear, editar, eliminar)
	![[Pasted image 20250326174458.png]]

##### 5.3 queries

- Es el encargado de exponer los métodos de consulta a GraphQL 
- Delegan la lógica a los resolvers que son los almacenes como había mencionado en el ejemplo anterior
- Guardan lo que mandan los resolver ( los resolvers convierten un ProductModel (datos con los que se comunica el ORM) a lo definido en el dominio(con lo que se trabaja en la aplicación ) 
- Finalmente antes de enviar la respuesta tranforman el product_entity en la respuesta definida en types una vez terminado se envia la respuesta al cliente
	![[Pasted image 20250326180412.png]]
##### 5.4 mutatios
- Es el encargado de exponer los métodos de mutacion a GraphQL
- Al igual que las queries delegan la lógica a los resolvers que son el almacen de los metodos y consultas que se pueden realizar
- las demás opciones que se aplican en las quieries se aplican aqui a las mutaciones
- la unica diferenca es que en las mutaciones se usan para hacer modificaciones como eliminar, editar, crear
![[Pasted image 20250326182126.png]]
##### 5.5 schemas
- Combina las peticiones de queries y mutations en un solo squema
- Es el punto de entrada de GraphQL
- Permite seguir extendiendo la aplicación
- Entre este tenemos dos schemas en la aplicación, uno para manejar una entidad y luego un general para manejar todas las entidades
	![[Pasted image 20250327091555.png]]
#### 6. Despliegue
##### 6.1 main.py
- Inicializa la aplicación con FastAPI
- Monta el router GraphQL para exponer el endpoint /graphql
- Se designa el puerto al cual ira dirigido el despliegue de la API

#### ¿Cómo es el proceso de escucha y proceso de la API para enviar una respuesta?

##### 1.  El cliente envía una solicitud 

``` json
mutation {
  createProduct(productData: { name: "Smartphone", price: 599.99 }) {
    id
    name
    price
  }
}
```
##### 2. Pasa al schema principal
La petición va a /graphql y lo manda a la sección de mutaciones, al ya tenerlo mapeado cuando se declara las mutaciones, es como tener una lista de todos los métodos mutation busca el que pide el usuario y se manda la petición a ese lugar.

``` python
import strawberry
from app.product.infrastructure.adapters.graphql.schemas import product_schema

@strawberry.type
class Query(
product_schema.query, # Hereda de ProductQuery
):

@strawberry.type
class Mutation(
product_schema.mutation, # Hereda de ProductMutation

):

schema = strawberry.Schema(query=Query, mutation=Mutation)
```
##### 3. La mutación llama al Resolver 
Se pasan los datos por los argumentos de la mutacion verificando que sean datos válidos (comparando con ProductInput en este caso)

Una vez verificado se crea una variable donde su guardara el resultado que nos devuelva el resolver, la data que se le pasara al resolver sera lo enviado por el usuario (luego de ser comprobada que cumple con los requerido)
![[Pasted image 20250327094731.png]]

##### 4.
El resolver vuelve a verificar el input de datos
Trae una session para interactuar con la base de datos
Se guarda en **product_repor** una instancia de SQLAlchemy con una session a la base de datos (ya que al no utilizar ningun metodo los argumentos van al init )
![[Pasted image 20250327095904.png]]
##### 5.
Luego en **use_case** se guarda la instancia de CreateProduct que primero verifica que la instancia de SQLAlchemy cumpla con lo definido en el repositorio, definido en product_repository
![[Pasted image 20250327100359.png]]

##### 5.
Luego de regreso con el resolver este guarda lo que nos retorna la instancia de CreateProduct y al ejecutar .execute (primero nos filtra la entrada de datos que debe ser ProductCreateDTO que anteriormente fue filtrada para que fuera del tipo input el cual deberia mantener el mismo orden que los DTO , finalmente el resolver retorna lo ejecutado por la instancia de SQLAlchemy
![[Pasted image 20250327100712.png]]
![[Pasted image 20250327100654.png]]
##### 6.
Cuando la mutación recibe la respuesta del resolver, lo retorna luego de pasarlo por el método "from_entity" de **ProductResponse**
![[Pasted image 20250327100842.png]]

##### 7.
Este método nos permite filtrar la información que va a llegar al usuario utilizando el metodo de la clase ProductResponse
1. Filtra la entrada, la data entrante debe estar en formato ProductEntity
2. Retorna la clase ProductResponse y asigna los datos a los atributos correspondientes
![[Pasted image 20250327101314.png]]
![[Pasted image 20250327102448.png]]

##### 8. Y finalmente el servidor devuelve la respuesta (ProductReponse)

![[Pasted image 20250327102808.png]]

#### ¿Cómo crear una nueva entidad funcional?

Crea una nueva carpeta dentro de app en este caso "user"

Agrega la estructura básica para cada entidad a crear
1. _ _ init _ _ .pi
2. application/
3. domain/
	1. entities.py
	2. repository.py
4. infrastructure/
	1. adapters
		1. graphql
			1. mutations.py
			2. queries.py
			3. resolvers.py
			4. schemas.py
			5. types.py
		2. sqlalchemy_(entidad)_ repository.py
	2. models
		1. model.py

![[Pasted image 20250327104546.png]]

Se crea el modelo que utilizara el ORM o lo que defina tu base de datos
![[Pasted image 20250327105707.png]]

Se importa el modelo en db_config y se agrega al (sync_engine)
![[Pasted image 20250327104831.png]]
Se crean los archivos de crud básico en application de la entidad
![[Pasted image 20250327104852.png]]

Crear el dominio empezando por las entities con las que se comunicara la aplicación

![[Pasted image 20250327112624.png]]
Crear el repository que definirá las entradas a la aplicación

![[Pasted image 20250327112635.png]]

Se definen los métodos crud en application 

![[Pasted image 20250327113826.png]]
![[Pasted image 20250327113839.png]]

Se crea el conector con la base de datos en este caso sqlachemy_user_repository
![[Pasted image 20250327115833.png]]


Una vez se crearon todos los métodos se pasa a crear los tipos para respuesta y de ingreso
![[Pasted image 20250327120455.png]]

Se crean los resolvers 
![[Pasted image 20250327122507.png]]
Se podría decir que sigue el patrón de repositorio anteriormente creado con los mismos métodos para su utilización

Se crean las queries y las mutaciones


Se crea el schema de la entidad
![[Pasted image 20250327123050.png]]
Se añade al schema principal



para evitar problemas los nombres de los metodos de 
Repository
SQLAlchemy 
Resolvers

Sean los mismo (aunque solo Repository y SQLAlchemy estan "obligados" a tener los mismos metodos)

Delete debe devolver true o false

alembic


### Notas adicionales

Para marcar atributos que nos envía el cliente como obligatorios u opcionales se hace lo siguiente esto se realiza en el archivo types.py de GraphQL
![[Pasted image 20250326180859.png]]

Flujo de las diferentes conversiones de datos que se hacen hasta llegar la respuesta al cliente
![[Pasted image 20250326181505.png]]

1. Base de datos - SQL
2. SQLAlchemy - model.py o estructura ORM de tu tabla
3. Entidad de dominio - Lo que usa la aplicacion para comunicarse
4. Se comunican con la entidad de dominio - (Product) es como una interpretacion personal definiendo atributos pero sin relacion con la base de datos
5. Pasa ese objeto Product por ProductResponse para que pueda ser filtrado y solo tenga los datos necesarios para que sea enviado al cliente
6. Envía al cliente la respuesta










Notas chatgpt - ignorar

Cuando uses CreateProduct debes pasarle un objeto que cumpla con el contrato definido por ProductRepository como lo es una instancia de SQLAlchemyProductRepository u otra clase que haga este guardado de datos (persistencia de datos)



Explicame cronolicamente 2 cosas 
1. Como es el proceso por donde pasa la data, como va moviendose de un archivo a otro de capa a capa, explicame de que manera va interactuando con lo archivos, puedes mkostrarme codigo para facilitar la compresión y usar ejemplos o comparaciones
2. Explicarme cronologicamente como podria crear nuevos modulos (entidades / tablas) que agregaria al proyecto, en este caso puedes usar usuario sin necesidad de relacionarlo con productos, y cual seria el paso a paso para poder desarrollar un nuevo modulo sin afectar toda la logica

class CustomerModel(Base):
    tablename = 'customers'

id = Column(Integer, primary_key=True, index=True)
customer_type = Column(String, index=True)
name = Column(String, index=True)
companyName = Column(String, unique=True, index=True)        # Para clientes empresa
identityNumber = Column(String, nullable=True)  # Para clientes de tipo persona
email = Column(String, unique=True)
taxId = Column(String, nullable=True)                       # Solo para compañías
phone = Column(String, unique=True)
address = Column(String)
created_at = Column(DateTime, default=func.now())
updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
orders = relationship("OrderModel", back_populates="customer")
representa![[]]tives = relationship("RepresentativeModel", back_populates="customer")