
| ID       | Titulo                  | Descripción | Prioridad | Actores | PreCond. | Pasos | PostCind. | CriterioAcep. |
| -------- | ----------------------- | ----------- | --------- | ------- | -------- | ----- | --------- | ------------- |
| RF-EM-01 | Ingresar a la pantalla  |             |           |         |          |       |           |               |
| RF-EM-02 |                         |             |           |         |          |       |           |               |
| RF-EM-03 |                         |             |           |         |          |       |           |               |
|          |                         |             |           |         |          |       |           |               |

## Plantilla

### ID

### Título

### Descripción

### Actores

### Pre - Condiciones

### Pasos

### Criterios de Aceptación





# Requerimientos Funcionales - Embudo
### ID
RF-EM-01

#### Título
Ingresar a la pantalla principal de Embudos (Administración)

#### Descripción
Lo usuarios registrados puede ingresar a la página de embudos y ver las opciones administrativas

#### Actores
Administradores

#### Pre - Condiciones
- Estar logueado en la aplicación
- Tener los permisos (rol) suficientes para ingresar a la sección

#### Pasos
1. Ingresar a la sección de embudos
2. Servidor retorna la vista de embudos con todo lo 
3. El usuario puede ver la información de embudos (administrador)

#### Criterios de Aceptación

1. El usuario administrador puede visualizar un menú con las opciones administrativas relacionadas con los embudos (ej. 'Crear Nuevo Embudo', 'Editar Embudo Existente', 'Gestionar Etapas', 'Configuración de Embudo').
2. Los elementos de la interfaz de las opciones administrativas deben estar presentes y bien representadas
3. El administrador puede visualizar los embudos actuales y gestionarlos
4. El administrador tiene acceso a los filtros de los embudos chats, agregar leads, asignación de chats
5. El administrador puede ver los leads actuales y las asignaciones que tienen actualmente
6. Si un usuario con un rol no autorizado intenta acceder a esta sección, el sistema debe mostrar un mensaje de error apropiado (ej. 'Acceso Denegado') o redirigirlo a una página a la que sí tenga acceso.
7. La navegación dentro de la sección de embudos debe ser intuitiva y permitir al administrador acceder fácilmente a las diferentes opciones.


### ID
RF-EM-02
#### Título
Utilizar los filtros avanzados
#### Descripción
Te permite filtrar los leads que administras actualmente, estos lead pueden ser filtrados por
- fecha
- hoy
- red social
- asignados (solo para administrador)
Al filtrar se excluyen todos los leads de embudos que no cumplen con los parámetros mencionados y solo muestra los que si cumplan con los parametros
#### Actores
- Administrador
- Vendedor (u otro subcargo)

#### Pre - Condiciones
- Debe estar logeado
- Debe ingresarse a la seccion de embudos
- Se ha hecho la validación del usuario y sus permisos
- De vuelve la vista

#### Pasos

 El usuario navega al boton de filtros dentro embudos.
- El usuario localiza y accede a la opción de "Filtros Avanzados" (hace click en "Filtros").
- El sistema muestra las opciones de filtrado disponibles: "Fecha", "Hoy", "Red Social", "Asignados", "Por Asignar".
- **Para filtrar por Fecha:**
    - El usuario selecciona la opción "Fecha".
    - El usuario selecciona la fecha o el rango de fechas deseado.
- **Para filtrar por Hoy:**
- **Para filtrar por Red Social:**
    - El usuario selecciona la opción "Red Social".
    - El sistema muestra una lista de las redes sociales disponibles (ej. Facebook, Instagram, etc).
    - El usuario selecciona una o varias redes sociales.
- **Para filtrar por Asignados:**
    - El usuario selecciona la opción "Asignados".
    - El sistema muestra una lista de los vendedores asignados.
    - El usuario selecciona uno o varios vendedores.
- **Para filtrar por el estados de los mensajes**
	- El usuario selecciona si quiere filtrar por ejemplo "entrante", "respondido", "no contestado", etc.
- El usuario hace clic en un botón para "Aplicar Filtros" o similar.
- El sistema procesa la solicitud de filtrado.
- El sistema actualiza la vista de la sección de embudos, mostrando únicamente los leads y los chats dentro que cumplen con los criterios de filtrado seleccionados.
- El sistema indica visualmente qué filtros están actualmente aplicados (ej. mostrando etiquetas con los filtros activos).
#### Criterios de Aceptación

1. **Filtrado por Fecha:**
    - Al seleccionar un rango de fechas, solo se muestran los leads que se encuentra dentro de ese rango.
    - Al seleccionar una fecha específica, solo se muestran los leads esa fecha
2. **Filtrado por Hoy:**
    - Al seleccionar "Hoy", solo se muestran los leads cuya fecha de creación corresponde al día actual.
    - Los leads de días anteriores o futuros no se muestran en la vista.
3. **Filtrado por Red Social:**
    - Al seleccionar una o varias redes sociales, solo se muestran los leads cuya fuente de origen corresponde a las redes sociales seleccionadas.
4. **Filtrado por Asignados:**
    - Al seleccionar uno o varios vendedores, solo se muestran los leads que están actualmente asignados a esos vendedores.
    - Si se selecciona la opción "Yo" (o el nombre del usuario actual), solo se muestran los leads asignados al usuario logueado.
    - Los leads asignados a otros vendedores no seleccionados no se muestran.
5. **Exclusión de Leads No Coincidentes:**
    - La aplicación del filtro debe excluir completamente de la vista los leads de todos los embudos que no cumplan con los parámetros seleccionados.
6. **Combinación de Filtros (Si aplica):**
    - (Opcional, pero común) Si el sistema permite combinar múltiples filtros (ej. leads asignados a un vendedor específico creados hoy), verificar que la combinación funcione correctamente y solo se muestren los leads que cumplen con _todos_ los criterios seleccionados.

### ID
RF-EM-03
#### Títul0
Barra de búsqueda para filtrar los leads por nombre, número, empresa o correo
#### Descripción
Es una barra búsquedas para los  leads en especifico, porque te ayuda a filtrar a los lead con mayor facilidad 
#### Actores
- Vendedor
- Administrador

#### Pre - Condiciones
- El usuario debe estar logueado en la aplicación.
- El usuario debe haber ingresado a la sección de embudos
- El sistema ha cargado y está mostrando la lista de leads a los que el usuario tiene permiso

#### Pasos
- El usuario localiza la barra de búsqueda dentro de la sección de leads.
- El usuario ingresa en la barra de búsqueda el texto (nombre, número, empresa o correo) por el cual desea filtrar los leads.
- El usuario acciona la función de búsqueda (esto puede ser presionando la tecla "Enter", haciendo clic en un botón de "Buscar" o el sistema puede filtrar en tiempo real mientras el usuario escribe).
- El sistema consulta la lista de leads y filtra aquellos que coinciden con el texto ingresado en los campos de Nombre, Número de Teléfono, Nombre de la Empresa o Correo Electrónico.
- El sistema actualiza la vista, mostrando únicamente los leads que cumplen con el criterio de búsqueda.
- Si no se encuentran leads que coincidan con el criterio de búsqueda, el sistema muestra un mensaje indicando que no se encontraron resultados.
#### Criterios de Aceptación
- **Búsqueda por Nombre:** Al ingresar un nombre (o parte de él) en la barra de búsqueda, solo se muestran los leads cuyo nombre coincida con el texto 
- **Búsqueda por Número:** Al ingresar un número de teléfono (o parte de él) en la barra de búsqueda, solo se muestran los leads cuyo número de teléfono coincida 
- **Búsqueda por Asignado:** Al ingresar un nombre de un asignado(o parte de él) se muestran resultados que coincidad con el texto ingresado.  (Solo para administrador)
- **Resultados Vacíos:** Si no se encuentra ningún lead que coincida con el texto de búsqueda, la interfaz debe mostrar un mensaje claro indicando "No se encontraron resultados" o similar.
- **Borrar Búsqueda:** Podría incluirse un criterio de aceptación que indique que debe haber una forma clara de borrar el término de búsqueda y volver a la vista de todos los leads (ej. un botón "X" dentro de la barra de búsqueda).


### ID
RF-EM-04

### Título
Crear embudo (Administrador)

### Descripción
El administrador puede crear un embudo luego de ingresar a la página de embudos y se compruebe su rol de administrador

### Actores
- Administrador

### Pre - Condiciones
- El usuario debe estar logueado en la aplicación.
- El usuario debe tener el rol de "administrador" asignado en el sistema.
- El usuario debe haber navegado exitosamente a la página principal de administración de embudos (cumpliendo con RF-EM-01).
### Pasos
- El sistema te da un embudo por defecto, si se quiere agregar un nuevo embudo se sigue los siguientes pasos.
1. En la página principal de administración de embudos, el administrador localiza y hace clic en la opción para "Crear Nuevo Embudo" .
2. El sistema muestra un formulario o ventana modal para la creación del nuevo embudo.
3. El administrador ingresa un **Nombre** para el nuevo embudo en el campo correspondiente. Este campo suele ser obligatorio.
4. (Opcional) El administrador ingresa una **Descripción** para el embudo en el campo correspondiente.
5. El sistema muestra un mensaje de confirmación indicando que el embudo ha sido creado exitosamente (con 4 etapas predeterminadas).
6. (Opcional) El administrador puede añadir  **Etapas del Embudo**.
7. (Opcional) El administrador puede tener la opción de **ordenar las etapas** arrastrándolas y soltándolas en el orden deseado.
8. El sistema guarda la información del nuevo embudo en la base de datos.


### Criterios de Aceptación

### ID
RF-EM-05

### Título
Agregar leads al embudo

### Descripción
El administrador puede agregar lead manualmente dentro de las etapas del embudo

### Actores
Administrador

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe tener el rol de "administrador" asignado en el sistema.
- Al menos un embudo debe existir en el sistema (creado previamente según RF-EM-04).
- El usuario debe haber navegado a la vista detallada de un embudo específico.

### Pasos

1. Dentro de la vista detallada de un embudo, el administrador localiza el boton de nuevo lead.
2. En la sección de la etapa seleccionada, el administrador busca y hace clic en una opción para "Agregar Lead" 
3. El sistema muestra un formulario o ventana modal para ingresar la información del nuevo lead.
4. El administrador completa los campos requeridos del formulario, que típicamente incluyen:
    - Nombre del Lead (obligatorio)
    - Número de Teléfono (obligatorio)
    - (Opcional) Correo Electrónico
    - (Opcional) Nombre de la Empresa
    - otros campos (si aplica)
5. Una vez que ha ingresado la información necesaria, el administrador hace clic en un botón para "Guardar Lead", "Crear Lead" o similar.
6. El sistema guarda la información del nuevo lead y lo asocia con la etapa por defecto la primera
7. El nuevo lead aparece visualmente dentro de la etapa correspondiente en la vista del embudo.
8. (Opcional) El sistema muestra un mensaje de confirmación indicando que el lead ha sido agregado exitosamente.

### Criterios de Aceptación

1. **Opción de Agregar Lead Visible:** Dentro de la vista de un embudo específico, en cada etapa, el administrador puede identificar y hacer clic en un elemento de la interfaz para agregar un nuevo lead.
2. **Formulario de Creación Presente:** Al hacer clic en la opción de agregar lead, se muestra un formulario o ventana modal con campos para ingresar la información del lead. El campo "Nombre del Lead" debe ser obligatorio.
3. **Validación de Campos Obligatorios:** El sistema no permite guardar el lead sin los campos obligatorios
4. **Lead Agregado a la Etapa Correcta:** Después de guardar, el nuevo lead es visible en la etapa del embudo donde se inició el proceso de creación.
5. **Información del Lead Guardada:** La información ingresada por el administrador en el formulario de creación del lead se guarda correctamente y está asociada al lead recién creado.
6. **Lead Visible en Listados:** El nuevo lead es visible en cualquier listado general de leads dentro del sistema al que el administrador tenga acceso.
7. **Asociación con el Embudo:** El nuevo lead está correctamente asociado al embudo en el que fue creado.
8. **(Opcional) Mensaje de Confirmación:** Se muestra un mensaje de éxito al administrador indicando que el lead ha sido agregado correctamente al embudo.


### ID
RF-EM-06

### Título
Asignar etapas a los trabajadores

### Descripción
El administrador a cada columna(etapa) que cree sobre el embudo principal puede asignárselo a un trabajador

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe tener el rol de "administrador" asignado en el sistema.
- Al menos un embudo debe existir en el sistema (creado previamente según RF-EM-04).
- El embudo seleccionado debe tener al menos una etapa creada.
- Debe haber usuarios con roles de "trabajador" o "vendedor" registrados en el sistema a los cuales se puedan asignar las etapas.
- El administrador debe haber navegado a la vista de edición o configuración del embudo específico.

### Pasos

1. Dentro de la vista de edición o configuración del embudo, el administrador localiza la sección donde se listan las etapas del embudo.
2. Para cada etapa, el administrador busca una opción para "Asignar Trabajador" o un elemento similar (podría ser un desplegable, un botón con un icono de persona, etc.).
3. Al hacer clic en la opción de asignación para una etapa específica, el sistema muestra una lista de los trabajadores (usuarios con roles apropiados) disponibles para ser asignados.
4. El administrador selecciona un trabajador de la lista para asignarlo a la etapa actual.
5. El sistema registra la asignación del trabajador a esa etapa específica del embudo.
6. La interfaz muestra visualmente el trabajador asignado a cada etapa (por ejemplo, mostrando su nombre junto al nombre de la etapa).
7. El administrador guarda los cambios realizados en la configuración del embudo (podría haber un botón como "Guardar Cambios", "Aplicar", etc.).
8. (Opcional) El sistema muestra un mensaje de confirmación indicando que las etapas han sido asignadas a los trabajadores exitosamente.

### Criterios de Aceptación

1. **Opción de Asignación Visible:** En la vista de configuración o edición de un embudo, para cada etapa, el administrador puede identificar y acceder a una opción para asignar un trabajador.
2. **Lista de Trabajadores Disponibles:** Al intentar asignar un trabajador a una etapa, el sistema presenta una lista de usuarios con roles de trabajador o vendedor que pueden ser seleccionados.
3. **Asignación por Etapa:** El administrador puede asignar un trabajador diferente a cada etapa(columna) del embudo.
4. **Guardado de la Asignación:** La asignación del trabajador a la etapa(columna) se guarda correctamente al guardar la configuración del embudo.
5. **Visualización de la Asignación:** En la vista de configuración del embudo, se muestra claramente el nombre del trabajador asignado a cada etapa.
6. **Permisos Implícitos (Según LeadSales):** Los leads que entren o se encuentren en una etapa asignada a un trabajador serán gestionados principalmente por ese trabajador (esto podría implicar que ese trabajador tenga permisos especiales para ver, editar o interactuar con esos leads).
7. **Posibilidad de Desasignar:** El administrador puede tener la opción de desasignar un trabajador de una etapa, dejando la etapa sin un responsable específico asignado.
8. **(Opcional) Notificación al Trabajador:** Si un trabajador es asignado a una etapa, el sistema podría enviar una notificación a ese trabajador (por correo electrónico o dentro de la plataforma).
9. **(Opcional) Validación de Roles:** El sistema impide que se asignen usuarios con roles incorrectos (ej. administradores) a las etapas destinadas a trabajadores o vendedores.

### ID
RF-EM-07

### Título
Columna general de chats del embudo

### Descripción
Al crear un embudo siempre habra una columna general donde iran todos los leads entrantes para luego poder ser asignados a los diferentes trabajadores

### Actores

- (Sistema)

### Pre - Condiciones

- Al menos un embudo debe existir en el sistema (creado previamente según RF-EM-04).

### Pasos

1. Cuando un nuevo embudo es creado por un administrador (siguiendo los pasos de RF-EM-04), el sistema automáticamente genera una columna inicial por defecto dentro de ese embudo.
2. Esta columna inicial es designada como el punto de entrada para todos los nuevos leads que se capturen o ingresen al sistema para ese embudo específico.
3. La columna se nombra con una etiqueta genérica y descriptiva, como "Leads Entrantes", "Bandeja de Entrada", "Nuevos Chats", o un nombre similar, por defecto.
4. Visualmente, esta columna se presenta como la primera columna o etapa en la representación del embudo dentro de la interfaz de usuario.

### Criterios de Aceptación

1. **Creación Automática:** Al crear un nuevo embudo, el sistema genera automáticamente una columna inicial sin necesidad de intervención manual adicional.
2. **Designación como Entrada:** La columna creada automáticamente está claramente identificada (visualmente y/o por su nombre) como la ubicación donde los nuevos leads ingresarán al embudo.
3. **Nombre por Defecto:** La columna tiene un nombre predeterminado y lógico que indica su función como punto de entrada de leads (ej. "Leads Entrantes").
4. **Posición Inicial:** La columna se muestra como la primera columna o etapa en la representación visual del embudo.
5. **Captura de Nuevos Leads:** Cualquier lead nuevo que sea capturado por el sistema y esté asociado a este embudo (ya sea por integración con otros canales, importación o creación manual) aparecerá automáticamente dentro de esta columna inicial.
6. **Funcionalidad Básica:** La columna permite realizar acciones básicas de gestión de leads, como visualizar la información del lead y, para los usuarios con los permisos adecuados, mover los leads a otras etapas del embudo.


### ID
RF-EM-08

### Título
Abrir chat general

### Descripción
Al clickear sobre el chat que te muestre un ventana emergente con el chat del número que esta ahí y las diferentes opciones se muestran para poder interactuar con el posible cliente

### Actores
- Administrador
- Trabajador (ej. vendedor)

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe haber navegado a la sección donde se muestra la lista de chats (ej. Bandeja de Entrada, una etapa específica del embudo).
- Debe existir al menos un chat disponible en la lista para ser clickeado.
- El usuario debe tener los permisos necesarios para visualizar el contenido del chat que intenta abrir (esto puede depender de su rol y de la asignación del chat).

### Pasos

1. El usuario localiza en la lista de chats el contacto o número de teléfono del cual desea ver la conversación.
2. El usuario hace clic sobre la fila o elemento visual que representa ese chat en la lista.
3. El sistema abre una ventana emergente (modal) o un panel lateral que contiene la conversación completa con ese contacto.
4. Dentro de la ventana/panel del chat, el usuario puede visualizar el historial de mensajes intercambiados con el contacto.
5. El usuario puede visualizar un boton para agregar pedidos
6. En la parte inferior de la ventana/panel, el usuario visualiza un campo de texto para escribir y enviar nuevos mensajes al contacto.
7. Junto al campo de texto o en la parte superior de la ventana/panel, el usuario puede ver opciones adicionales para interactuar con el lead, tales como:
    - Botones para enviar archivos adjuntos (si la funcionalidad está disponible).
    - Opciones para guardar notas sobre el lead.
    - Posibilidad de cambiar el estado del lead o moverlo a otra etapa del embudo.
    - Opción para asignar el lead a otro usuario (si tiene los permisos necesarios).
    - Posibilidad de utilizar respuestas rápidas o plantillas de mensajes (si están configuradas).
8. El usuario puede cerrar la ventana/panel del chat haciendo clic en un botón de cerrar (típicamente una "X" o la palabra "Cerrar").

### Criterios de Aceptación

1. **Chat Clickable:** Cada elemento de la lista de chats que representa una conversación activa o pasada debe ser clickeable.
2. **Apertura de Ventana/Panel:** Al hacer clic en un chat, se abre una ventana emergente o un panel lateral que muestra la conversación.
3. **Contenido del Chat Correcto:** La conversación mostrada en la ventana/panel corresponde al contacto o número de teléfono seleccionado.
4. **Historial de Mensajes Visible:** Se visualiza el historial completo de mensajes intercambiados con el contacto (dentro de un límite razonable o según la configuración del sistema).
5. **Campo de Texto para Escribir:** Un campo de texto claramente identificable está presente para que el usuario pueda redactar nuevos mensajes.
6. **Funcionalidad de Enviar Mensajes:** Los mensajes escritos en el campo de texto pueden ser enviados exitosamente al contacto al presionar "Enter" o hacer clic en un botón de enviar.
7. **Visualización de Mensajes Enviados:** Los mensajes enviados por el usuario aparecen en la ventana/panel del chat.
8. **Opciones de Interacción Presentes:** Las opciones adicionales para interactuar con el lead (enviar archivos, guardar notas, cambiar estado, asignar, respuestas rápidas) están visibles en la ventana/panel del chat (si estas funcionalidades están implementadas).
9. **Cierre de la Ventana/Panel:** Existe un mecanismo claro para cerrar la ventana/panel del chat y volver a la lista de chats (ej. un botón "Cerrar" o un icono de "X").
10. **Información del Contacto:** La ventana/panel del chat muestra información básica del contacto (ej. nombre si está guardado, número de teléfono).
11. **Rendimiento:** La ventana/panel del chat se abre en un tiempo razonable después de hacer clic en el chat.






### ID
RF-EM-09

### Título
Eliminar columnas(administradores) o etapas internas (trabajadores)

### Descripción
Permite al usuario eliminar columnas que fueron asignadas a trabajadores (pero mandando sus chats pendientes a otro trabajador) o a los trabajadores eliminar sus etapas de gestion que tienen (pero antes mover sus leads a otra columna).

### Actores
- Administrador
- Vendedor

### Pre - Condiciones

- **Administrador:**
    - El usuario debe estar logueado en la aplicación con rol de "administrador".
    - Debe existir al menos un embudo creado con columnas asignadas a trabajadores.
    - La columna que se intenta eliminar debe tener trabajadores asignados previamente.
    - Debe haber al menos otro trabajador activo en el sistema al cual se puedan reasignar los chats pendientes.
- **Vendedor:**
    - El usuario debe estar logueado en la aplicación con rol de "vendedor".
    - Debe haber ingresado a la sección de embudos donde visualiza sus etapas de gestión internas.
    - La etapa interna que se intenta eliminar debe haber sido creada previamente por el vendedor.
    - La etapa interna que se intenta eliminar no debe contener leads activos.

### Pasos

- **Administrador (Eliminar Columna):**
    1. El administrador navega a la sección de configuración o administración de embudos.
    2. El administrador selecciona el embudo que contiene la columna a eliminar.
    3. El administrador localiza la columna que desea eliminar.
    4. El administrador acciona la opción para eliminar la columna (ej. clic en un icono de "eliminar", botón "Eliminar Columna").
    5. El sistema muestra una ventana modal o similar preguntando al administrador a qué otro trabajador desea reasignar los chats pendientes de la columna que se va a eliminar.
    6. El administrador selecciona un trabajador de la lista de trabajadores disponibles.
    7. El administrador confirma la acción de eliminar la columna y reasignar los chats.
    8. El sistema transfiere todos los leads pendientes de la columna eliminada al trabajador seleccionado.
    9. El sistema elimina la columna del embudo.
    10. El sistema muestra un mensaje de confirmación al administrador indicando que la columna ha sido eliminada y los chats reasignados.
- **Vendedor (Eliminar Etapa Interna):**
    1. El vendedor navega a la sección de embudos donde visualiza sus etapas de gestión internas.
    2. El vendedor localiza la etapa interna que desea eliminar.
    3. El vendedor verifica que la etapa interna no contenga ningún lead activo. Si contiene leads, debe moverlos a otra columna o etapa primero.
    4. El vendedor acciona la opción para eliminar la etapa interna (ej. clic en un icono de "eliminar", botón "Eliminar Etapa").
    5. El sistema muestra una ventana modal o similar pidiendo confirmación para eliminar la etapa interna.
    6. El vendedor confirma la eliminación de la etapa interna.
    7. El sistema elimina la etapa interna de la vista del vendedor.
    8. El sistema muestra un mensaje de confirmación al vendedor indicando que la etapa interna ha sido eliminada.

### Criterios de Aceptación

- **Administrador (Eliminar Columna):**
    1. El administrador puede encontrar la opción para eliminar una columna asignada a un trabajador.
    2. El sistema obliga al administrador a seleccionar un trabajador para reasignar los chats pendientes antes de eliminar la columna.
    3. Todos los leads que estaban en la columna eliminada son correctamente reasignados al trabajador seleccionado.
    4. La columna eliminada ya no es visible en la estructura del embudo.
    5. El administrador recibe un mensaje de confirmación de la eliminación y la reasignación de chats.
    6. Los leads reasignados son visibles en la columna o sección correspondiente del trabajador al que fueron asignados.
- **Vendedor (Eliminar Etapa Interna):**
    1. El vendedor puede encontrar la opción para eliminar una etapa de gestión interna que haya creado.
    2. El sistema impide la eliminación de una etapa interna si contiene leads activos, mostrando un mensaje al vendedor indicándole que debe mover los leads primero.
    3. Una vez que la etapa interna no contiene leads, el vendedor puede eliminarla.
    4. La etapa interna eliminada ya no es visible en la vista de embudos del vendedor.
    5. El vendedor recibe un mensaje de confirmación de la eliminación de la etapa interna.


### ID
RF-EM-10

### Título
Editar atributos del Lead

### Descripción
El usuario puede editar la información del Lead una vez abierto su chat en una ventana emergente

### Actores
- Administrador
- Trabajador

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe tener abierto el chat de un lead específico en una ventana emergente (según RF-EM-07).
- El usuario debe tener los permisos necesarios para editar la información del lead (esto puede depender de su rol y de la configuración de permisos del sistema).

### Pasos

1. Dentro de la ventana emergente del chat, el usuario localiza la sección o el botón que permite ver o editar los detalles del lead (ej. "Ver Detalles", "Editar Información", un icono de lápiz, etc.).
2. Al hacer clic en esta opción, el sistema muestra los atributos del lead en formato editable (ej. campos de texto, desplegables, casillas de verificación). Los atributos típicos incluyen:
    - Nombre del Lead
    - Número de Teléfono
    - Correo Electrónico
    - Nombre de la Empresa
    - Fuente del Lead
    - Vendedor Asignado (si el usuario tiene permisos)
    - Etapa del Embudo (si el usuario tiene permisos)
    - Cualquier campo personalizado configurado para los leads.
3. El usuario modifica los valores de los campos que desea editar.
4. Una vez realizadas las modificaciones, el usuario hace clic en un botón para "Guardar", "Actualizar", "Aplicar Cambios" o similar.
5. El sistema guarda la información actualizada del lead en la base de datos.
6. (Opcional) El sistema muestra un mensaje de confirmación indicando que la información del lead ha sido actualizada exitosamente.
7. La información del lead mostrada en la ventana emergente del chat se actualiza con los nuevos valores.
8. La información actualizada del lead también se refleja en la lista general de leads y en la vista del embudo.

### Criterios de Aceptación

1. **Opción de Editar Visible:** Dentro de la ventana emergente del chat, el usuario puede identificar y acceder a una opción para editar la información del lead.
2. **Campos Editables Presentes:** Al hacer clic en la opción de editar, los atributos del lead se muestran en campos de formulario que permiten su modificación.
3. **Modificación de Atributos:** El usuario puede modificar los valores en los campos editables.
4. **Guardado de Cambios:** Al hacer clic en el botón de guardar, los cambios realizados en los atributos del lead se guardan correctamente en el sistema.
5. **Persistencia de Datos:** La información del lead se actualiza en la base de datos y los cambios son permanentes.
6. **(Opcional) Mensaje de Confirmación:** Se muestra un mensaje de éxito al usuario indicando que la información del lead ha sido actualizada.
7. **Actualización en la Ventana del Chat:** La información del lead mostrada en la ventana emergente del chat se actualiza inmediatamente después de guardar los cambios.
8. **Actualización en Listados:** La información actualizada del lead también se refleja en la lista general de leads y en la vista del embudo donde aparece el lead.
9. **(Opcional) Validación de Datos:** El sistema realiza validaciones básicas en los campos editados (ej. formato de correo electrónico, formato de número de teléfono) y muestra mensajes de error si la información ingresada no es válida.
10. **Control de Permisos:** Los usuarios solo pueden editar los atributos para los cuales tienen los permisos correspondientes según su rol. Por ejemplo, un vendedor podría no tener permiso para cambiar la etapa del embudo si esa acción está reservada para administradores.


### ID
RF-EM-11

### Título
Agregar pedidos a los chats

### Descripción
El usuario puede asignar pedidos al Lead, la opción se encuentra al abrir el Lead en la parte superior esto te pide datos como (agarra el nombre por defecto) descripción código de pedido cantidad precio-unitario total servicio fecha-pedido fecha-entrega 

### Actores
- Administrador
- Trabajador

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe tener abierto el chat de un lead específico en una ventana emergente (según RF-EM-07).
- El usuario debe tener los permisos necesarios para agregar pedidos a los leads (esto puede depender de su rol y de la configuración de permisos del sistema).

### Pasos

1. Dentro de la ventana emergente del chat, el usuario localiza la opción para "Agregar Pedido" o un elemento similar, que se encuentra en la parte superior de la ventana.
2. Al hacer clic en esta opción, el sistema muestra un formulario o ventana modal para ingresar los detalles del pedido.
3. El campo "Nombre" del pedido se completa automáticamente con el nombre del lead asociado al chat.
4. El usuario completa los siguientes campos del formulario:
    - Descripción del Pedido
    - Código de Pedido
    - Cantidad
    - Precio Unitario
    - Total
    - Servicio (El servicio por el que se esta cobrando o el producto)
    - Fecha del Pedido
    - Fecha de Entrega
5. Una vez que ha ingresado toda la información del pedido, el usuario hace clic en un botón para "Guardar Pedido", "Crear Pedido" o similar.
6. El sistema guarda la información del pedido y la asocia con el lead cuyo chat estaba abierto.
7. (Opcional) El sistema muestra un mensaje de confirmación indicando que el pedido ha sido agregado exitosamente al lead.
8. El pedido recién agregado se puede visualizar en el historial 

### Criterios de Aceptación

1. **Opción de Agregar Pedido Visible:** En la parte superior de la ventana emergente del chat, el usuario puede identificar y acceder a una opción para agregar un pedido al lead.
2. **Formulario de Pedido Presente:** Al hacer clic en la opción de agregar pedido, se muestra un formulario o ventana modal con los campos requeridos: "Descripción", "Código de Pedido", "Cantidad", "Precio Unitario", "Total", "Servicio", "Fecha Pedido", "Fecha Entrega".
3. **Nombre del Lead por Defecto:** El campo "Nombre" del formulario de pedido se precarga automáticamente con el nombre del lead cuyo chat está abierto.
4. **Ingreso de Datos:** El usuario puede ingresar información en todos los campos del formulario de pedido.
5. **Guardado del Pedido:** Al hacer clic en el botón de guardar, la información del pedido se guarda correctamente y se asocia con el lead.
6. **(Opcional) Mensaje de Confirmación:** Se muestra un mensaje de éxito al usuario indicando que el pedido ha sido agregado al lead.
7. **Pedido Visible en Detalles del Lead:** El pedido agregado se puede visualizar en una sección dedicada a los pedidos dentro de los detalles del lead (Historial).
8. **(Opcional) Validación de Datos:** El sistema realiza validaciones básicas en los campos del pedido (ej. formato de fechas, valores numéricos en cantidad, precio, total) y muestra mensajes de error si la información ingresada no es válida.
9. **Control de Permisos:** Los usuarios solo pueden agregar pedidos a los leads si tienen los permisos correspondientes según su rol.

### ID
RF-EM-12

### Título
Historial de pedidos de los chats

### Descripción
Se puede ver historial de pedidos de cada chat individualmente
Se puede buscar en los historial también
Se puede filtrar tambien
### Actores
- Administrador
- Trabajador

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe tener abierto el chat de un lead específico en una ventana emergente (según RF-EM-07).
- El lead cuyo chat está abierto debe tener al menos un pedido asociado (creado previamente según RF-EM-11).
- El usuario debe tener los permisos necesarios para visualizar el historial de pedidos de los leads.

### Pasos

1. Dentro de la ventana emergente del chat, el usuario localiza y accede a la sección o pestaña denominada "Historial de Pedidos" o similar.
2. El sistema muestra una lista de todos los pedidos asociados al lead actual. Para cada pedido, se muestra información relevante como:
    - Código de Pedido
    - Descripción del Pedido
    - Fecha del Pedido
    - Fecha de Entrega
    - Total del Pedido
    - (Opcional) Estado del Pedido
3. El usuario localiza la barra de búsqueda dentro de la sección del historial de pedidos.
4. El usuario ingresa en la barra de búsqueda el texto pero antes selecciona que quiere buscar (ej. código de pedido, descripción) por el cual desea filtrar el historial.
5. El sistema filtra la lista de pedidos, mostrando solo aquellos que coinciden con el texto de búsqueda en los campos relevantes.
6. El usuario localiza las opciones de filtrado (ej. desplegables, selectores de fecha) dentro de la sección del historial de pedidos. Los filtros podrían incluir:
    - Rango de Fechas del Pedido
    - (Opcional) Estado del Pedido
7. El usuario selecciona los criterios de filtrado deseados.
8. El sistema aplica los filtros seleccionados y actualiza la lista de pedidos, mostrando solo aquellos que cumplen con los criterios.

### Criterios de Aceptación

1. **Sección de Historial Visible:** Dentro de la ventana emergente del chat, existe una sección o pestaña claramente identificada como "Historial de Pedidos" o similar.
2. **Lista de Pedidos Presente:** Si el lead tiene pedidos asociados, estos se muestran en una lista dentro de la sección del historial.
3. **Información del Pedido:** Para cada pedido en la lista, se muestra al menos el Código de Pedido, la Descripción, la Fecha del Pedido, la Fecha de Entrega y el Total.
4. **Barra de Búsqueda:** Una barra de búsqueda está disponible dentro de la sección del historial de pedidos.
5. **Funcionalidad de Búsqueda:** Al ingresar texto en la barra de búsqueda, el historial de pedidos se filtra correctamente, mostrando solo los pedidos que coinciden con el texto en los campos de Código de Pedido y Descripción (la búsqueda no distingue mayúsculas de minúsculas y soporta búsquedas parciales).
6. **Opciones de Filtrado:** Se presentan opciones para filtrar el historial de pedidos, incluyendo al menos un filtro por rango de fechas del pedido.
7. **Funcionalidad de Filtrado:** Al seleccionar criterios de filtrado, la lista de pedidos se actualiza correctamente, mostrando solo los pedidos que cumplen con los criterios seleccionados.
8. **Mensaje Sin Pedidos:** Si el lead no tiene ningún pedido asociado, la sección del historial de pedidos muestra un mensaje indicando que no se encontraron pedidos.
9. **Presentación Clara:** El historial de pedidos se presenta de manera organizada y fácil de leer.


### ID
RF-EM-13

### Título
Opciones para los mensajes 
### Descripción
Son opciones que puede visualizar al clickear sobre un mensaje tiene las opciones (Responder, Reenviar, Editar, Eliminar)
### Actores
- Administrado
- Trabajador

### Pre - Condiciones

- El usuario debe estar logueado en la aplicación.
- El usuario debe tener abierto el chat con un lead (según RF-EM-07).
- Debe haber al menos un mensaje presente en la conversación del chat.

### Pasos

1. Dentro de la ventana del chat, el usuario realiza una acción sobre un mensaje específico para desplegar las opciones (esto podría ser un clic derecho, un hover prolongado, o un clic en un icono de "tres puntos" asociado al mensaje).
2. Un menú contextual o una barra de opciones aparece cerca del mensaje seleccionado, mostrando las opciones: "Responder", "Reenviar", "Editar", "Eliminar".
3. **Responder:** Si el usuario selecciona "Responder", el campo de texto para escribir un nuevo mensaje se activa, y el mensaje seleccionado se cita o se muestra una referencia a él en la parte superior del campo de texto.
4. **Reenviar:** Si el usuario selecciona "Reenviar", el sistema presenta una interfaz (ej. ventana modal, lista de contactos) donde el usuario puede seleccionar a uno o varios destinatarios para enviar el mensaje.
5. **Editar:** Si el usuario selecciona "Editar" (y si esta opción está habilitada para el tipo de mensaje y el usuario), el contenido del mensaje seleccionado se vuelve editable directamente en la ventana del chat. El usuario puede modificar el texto y luego guardar los cambios.
6. **Eliminar:** Si el usuario selecciona "Eliminar" (y si tiene los permisos necesarios), el sistema muestra una ventana de confirmación para eliminar el mensaje. Al confirmar, el mensaje se elimina de la vista del chat
### Criterios de Aceptación

1. **Opciones Visibles:** Al interactuar con un mensaje (según el paso 1), las opciones "Responder", "Reenviar", "Editar" y "Eliminar" se visualizan cerca del mensaje.
2. **Funcionalidad Responder:**
    - Al seleccionar "Responder", el campo de texto se activa.
    - El mensaje original se cita o referencia de forma clara.
    - El usuario puede escribir y enviar una respuesta que se muestra en el chat referenciando el mensaje original.
3. **Funcionalidad Reenviar:**
    - Al seleccionar "Reenviar", se presenta una interfaz para seleccionar destinatarios.
    - El usuario puede seleccionar uno o varios destinatarios.
    - El mensaje seleccionado se envía correctamente a los destinatarios elegidos como un nuevo mensaje.
4. **Funcionalidad Editar:**
    - Al seleccionar "Editar" en un mensaje enviado por el usuario actual (si está permitido), el contenido del mensaje se vuelve editable.
    - El usuario puede modificar el texto del mensaje.
    - Al guardar la edición, el mensaje original se actualiza en la vista del chat.
5. **Funcionalidad Eliminar:**
    - Al seleccionar "Eliminar", se muestra una confirmación antes de eliminar el mensaje.
    - Al confirmar, el mensaje se elimina de la vista del chat del usuario que realizó la acción. 
6. **Visibilidad Contextual:** Las opciones aparecen de forma contextual al mensaje sobre el que se interactúa.
7. **Control de Permisos:** La opción "Editar" y "Eliminar" solo están disponibles si el usuario tiene los permisos necesarios para realizar estas acciones (por ejemplo, un trabajador podría no poder editar mensajes de un administrador o eliminar mensajes de clientes, dependiendo de la configuración).




### ID
RF-EM-14

### Título
Crear etapas dentro de la columna asignada por el administrador
### Descripción
Se pueden crear etapas de proceso dentro de cada columna (donde asigna el administrador a los trabajador), por defecto siempre se creara una etapa de proceso donde iran todos lo Leads que asigne el administrador al trabajador

### Actores
- Administrador
- Trabajador

### Pre - Condiciones

- **Administrador:**
    - El usuario debe estar logueado en la aplicación con rol de "administrador".
    - Debe existir al menos un embudo creado con columnas asignadas a trabajadores (RF-EM-06).
    - El administrador debe haber navegado a la vista de edición o configuración del embudo.
- **Trabajador:**
    - El usuario debe estar logueado en la aplicación con rol de "trabajador" o "vendedor".
    - El administrador debe haberle asignado al menos una columna dentro de un embudo (RF-EM-06).
    - El trabajador debe haber ingresado a la vista del embudo donde se visualizan las columnas que le han sido asignadas.

### Pasos

- **Administrador (Crear Etapa Interna - Opcional, según diseño):**
    1. El administrador navega a la vista de edición del embudo.
    2. Selecciona la columna asignada a un trabajador donde desea crear una etapa interna.
    3. Busca y acciona la opción para "Agregar Etapa Interna" dentro de esa columna (ej. un botón "+", un enlace).
    4. Ingresa el nombre de la nueva etapa interna.
    5. Guarda la nueva etapa interna.
- **Trabajador (Crear Etapa Interna):**
    1. El trabajador navega a la vista del embudo y visualiza la columna que le ha sido asignada.
    2. Dentro de la columna asignada, el trabajador busca y acciona la opción para "Agregar Etapa Interna" o similar (ej. un botón "+", un enlace dentro de la columna).
    3. Ingresa el nombre de la nueva etapa interna que desea crear para organizar sus leads dentro de esta columna.
    4. Guarda la nueva etapa interna.

### Criterios de Aceptación

1. **Creación por Administrador (Opcional):** Si los administradores pueden crear etapas internas:
    - El administrador puede encontrar la opción para agregar una etapa interna dentro de una columna asignada a un trabajador.
    - El administrador puede nombrar la nueva etapa interna.
    - La etapa interna creada por el administrador es visible dentro de la columna asignada al trabajador.
2. **Creación por Trabajador:**
    - El trabajador puede encontrar la opción para agregar una etapa interna dentro de la columna que le ha sido asignada.
    - El trabajador puede nombrar la nueva etapa interna.
    - La etapa interna creada por el trabajador es visible dentro de la columna asignada.
3. **Etapa de Proceso por Defecto:** Al asignarse una columna a un trabajador (o al crearse el embudo, según el diseño), una etapa interna predeterminada con un nombre como "Etapa Default" se crea automáticamente dentro de esa columna.
4. **Ubicación Visual:** Las etapas internas creadas son visualmente distinguibles y se muestran dentro de la columna principal asignada.
5. **Gestión de Leads:** Los leads asignados a la columna principal pueden ser movidos entre las diferentes etapas internas creadas dentro de esa columna por el trabajador (o por el administrador si tiene permisos).
6. **Limitación (Trabajador):** Los trabajadores solo pueden crear etapas internas dentro de las columnas que les han sido asignadas, no en otras columnas del embudo.
7. **(Opcional) Límite de Etapas:** Se podría definir un límite en la cantidad de etapas internas que un trabajador puede crear por columna.
8. **(Opcional) Permisos:** Se podrían definir permisos más granulares sobre quién puede crear, editar o eliminar etapas internas.

![[Pasted image 20250331163750.png]]
![[Pasted image 20250331163758.png]]

### ID
RF-EM-15

### Título
Mover leed entre trabajadores (administrador) y entre etapas (trabajador)
### Descripción
El administrador puede asignar manualmente a donde ira cada Lead cuando los reciba en la columna creada al crear el embudo. El vendedor puede elegir entre uno sus varias etapas que tiene a cargo (General, Contactado, Cierre) e ir manejando sus Leads asignados entre estas etapas para llevar un mejor control

### Actores
- Administrador
- Trabajador

### Pre - Condiciones

- **Administrador (Mover entre trabajadores):**
    - El usuario debe estar logueado en la aplicación con rol de "administrador".
    - Debe existir al menos un embudo creado con la columna general inicial.
    - Debe haber leads presentes en la columna general inicial o en columnas asignadas a trabajadores.
    - Debe haber al menos dos trabajadores activos en el sistema a los cuales se puedan asignar los leads.
- **Trabajador (Mover entre etapas):**
    - El usuario debe estar logueado en la aplicación con rol de "trabajador" o "vendedor".
    - El administrador debe haberle asignado al trabajador al menos una columna dentro de un embudo (RF-EM-06).
    - Debe haber leads asignados a la columna del trabajador.
    - La columna asignada al trabajador debe tener al menos dos etapas internas creadas (incluyendo la etapa por defecto).

### Pasos

- **Administrador (Mover Lead entre trabajadores):**
    1. El administrador navega a la vista del embudo.
    2. Localiza el lead que desea reasignar, el cual estará en la columna general o en la columna de un trabajador.
    3. Acciona la función para reasignar el lead. Esto podría ser mediante:
        - **Arrastrar y soltar:** Arrastrar el lead desde su columna actual a la columna del trabajador al que se desea asignar.
        - **Opción de Asignar:** Hacer clic en el lead y seleccionar una opción como "Asignar a" o similar, y luego elegir el trabajador de una lista.
        - **Acciones en lote:** Seleccionar varios leads y realizar una acción masiva para asignarlos a un trabajador específico.
    4. El sistema actualiza la información del lead, asignándolo al trabajador seleccionado.
    5. El lead desaparece de la vista del administrador (o de la columna donde estaba anteriormente) y aparece en la columna o vista del trabajador al que fue asignado.
    6. (Opcional) El sistema muestra un mensaje de confirmación al administrador indicando que el lead ha sido reasignado.
- **Trabajador (Mover Lead entre etapas):**
    1. El trabajador navega a la vista del embudo y visualiza la columna que le ha sido asignada.
    2. Localiza el lead que desea mover entre sus etapas internas.
    3. Mueve el lead a la etapa deseada dentro de su columna. Esto podría ser mediante:
        - **Arrastrar y soltar:** Arrastrar el lead desde su etapa actual a la etapa de destino dentro de la misma columna.
        - **Opción de Mover a Etapa:** Hacer clic en el lead y seleccionar una opción como "Mover a etapa" o similar, y luego elegir la etapa de destino de una lista de sus etapas internas.
    4. El sistema actualiza la información del lead, moviéndolo a la etapa interna seleccionada dentro de la columna del trabajador.
    5. El lead se visualiza ahora en la nueva etapa interna dentro de la columna del trabajador.

### Criterios de Aceptación

- **Administrador (Mover Lead entre trabajadores):**
    1. El administrador puede seleccionar un lead y reasignarlo a otro trabajador utilizando la funcionalidad de arrastrar y soltar o la opción de asignar.
    2. El lead se mueve exitosamente de la columna de origen a la columna del trabajador destino.
    3. La asignación del lead se actualiza correctamente en el sistema, reflejándose en la vista del trabajador.
    4. (Opcional) El administrador recibe una notificación o mensaje de confirmación de la reasignación.
- **Trabajador (Mover Lead entre etapas):**
    1. El trabajador puede seleccionar un lead asignado a su columna.
    2. El trabajador puede mover el lead entre las diferentes etapas internas de su columna utilizando la funcionalidad de arrastrar y soltar o la opción de mover a etapa.
    3. El lead se mueve exitosamente de la etapa interna de origen a la etapa interna de destino dentro de la misma columna.
    4. La etapa del lead se actualiza correctamente en el sistema, reflejándose en la vista del trabajador.



(No estoy seguro de este requerimiento)
### ID
RF-EM-16

### Título
Lógica Embudos Vendedor
### Descripción
El sistema debe de ser posible de enlazar diferentes vendedores, para que al terminar las etapas dentro de un vendedor pueda ser asignado a otro, regresar al inicio de las etapas de ese vendedor o incluso regresar al incio (recepcion de leds)

### Actores
- (Sistema)

### Pre - Condiciones

- Debe existir al menos un embudo creado (RF-EM-04).
- Debe haber varios usuarios con rol de "vendedor" registrados en el sistema.
- Las etapas del embudo deben estar definidas y, idealmente, asignadas a diferentes vendedores (RF-EM-06).
- Debe haber una forma de configurar la lógica de flujo entre vendedores para cada embudo (esto podría ser una configuración a nivel del embudo).

### Pasos

1. Un lead ingresa al embudo (a través de la columna general o asignado directamente a un vendedor).
2. El lead avanza a través de las etapas asignadas al primer vendedor.
3. Cuando el lead alcanza una etapa designada como "final" para ese vendedor (esto podría ser la última etapa interna del vendedor o una etapa específica marcada para transferencia), el sistema evalúa la lógica configurada para ese punto.
4. Según la configuración, el sistema realiza una de las siguientes acciones:
    - **Asignar a otro vendedor:** El sistema identifica al siguiente vendedor en la secuencia definida para el embudo y asigna automáticamente el lead a la columna o etapa correspondiente de ese vendedor.
    - **Regresar al inicio de las etapas del vendedor actual:** El sistema mueve el lead a la primera etapa (o a una etapa específica designada como inicio) dentro de la columna asignada al vendedor actual.
    - **Regresar al inicio (recepción de leads):** El sistema mueve el lead a la columna general de recepción de leads del embudo.
5. El sistema actualiza el estado y la asignación del lead en la base de datos.
6. El lead se visualiza en la nueva ubicación (columna del nuevo vendedor, etapa inicial del vendedor actual o columna de recepción).

### Criterios de Aceptación

1. **Configuración de Flujo:** El sistema permite a un administrador configurar la lógica de flujo de leads entre diferentes vendedores dentro de un embudo específico. Esta configuración debe permitir definir el siguiente vendedor, el retorno al inicio de las etapas del vendedor actual y el retorno a la recepción de leads.
2. **Disparador de Transferencia:** Al alcanzar un lead una etapa designada como "final" para un vendedor, el sistema identifica correctamente la lógica de flujo configurada para ese punto.
3. **Asignación a Otro Vendedor:** Si la lógica configurada es "asignar a otro vendedor", el lead se asigna automáticamente al siguiente vendedor especificado en la configuración del embudo y aparece en su columna o etapa correspondiente.
4. **Retorno a Etapas del Vendedor Actual:** Si la lógica configurada es "regresar al inicio de las etapas del vendedor actual", el lead se mueve a la primera etapa (o a la etapa designada como inicio) dentro de la columna asignada al vendedor actual.
5. **Retorno a Recepción de Leads:** Si la lógica configurada es "regresar al inicio (recepción de leads)", el lead se mueve a la columna general de recepción de leads del embudo.
6. **Transición Fluida:** La transición del lead entre vendedores o etapas se realiza de manera automática y se refleja correctamente en la interfaz del sistema.
7. **Visibilidad:** Los administradores y los vendedores involucrados pueden visualizar el movimiento del lead a través del embudo según la lógica configurada.
8. **(Opcional) Notificaciones:** El sistema podría enviar notificaciones a los vendedores cuando un lead es asignado a ellos o cuando un lead regresa a su gestión.
9. **(Opcional) Definición de Etapa Final:** Debe haber una forma de definir qué etapa o condición se considera como "final" para un vendedor y que dispara la evaluación de la lógica de flujo.


