# Proyecto Urban Grocers 
El siguiente proyecto consiste en la automatización de pruebas de API 
para la aplicación Urban Grocers, específicamente en la sección 
***"creación de kits de producto"***. En este documento se presentan 
los resultados actuales que se ejecutaron a la lista de comprobación 
al campo **"name"**.

# Fuente de documentación utilizada
apiDoc

# Tecnologías utilizadas
Pycharm, Git y GitHub

# Pruebas

**Pre condiciones**

- **1**. Tener guardado la URL y las rutas de la solicitudes en **configuration.py**

- **2**. Colocar los cuerpos de la solicitud POST en el archivo **data.py**

- **3**. Todas las solicitudes *POST* que necesitas para resolver 
la tarea se deben almacenar en el archivo **sender_stand_request.py** 

- **4**. Envía una solicitud para crear un nuevo usuario 
(recuerda el token de autenticación **"authToken"**).

- **5**. Envía una solicitud para crear un kit personal para este usuario o usuaria. 
Esto lo puedes ver en el archivo **sender_stand_request.py**.

**Pasos para ejecutar las pruebas**

- **1**. Crear el archivo **create_kit_name_kit_test.py**.

- **2**- importar los archivos **data** y **sender_stand_request** 
para **create_kit_name_kit_test.py**.

- **3**. En el mismo archivo Define la función 
*GET* para Kit_body y new_user_token (***get_kit_body( def kit_name):*** 
y ***def get_new_user_token():***).

- **4**. Definir las funciones de forma separada para 
***positive_assert(kit_body)*** y ***negative_assert_code_400(kit_body):***.

- **5**. Se añade la **"Lista de comprobación de pruebas"** 
definiendo cada prueba de forma separada prefijo *test_*.
