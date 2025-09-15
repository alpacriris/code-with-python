# Prácticas MQTT con Python

Práctica de Python centrada en el uso de MQTT para comunicación entre clientes y publicación/suscripción a topics.

### Organización de archivos

- **`src/`** → contiene los archivos fuente.  
- **`sol/`** → contiene las soluciones de los ejercicios propuestos.

---

### 1. Ejecuta `sisub.py` 

Ejecuta `sisub.py` y explica el resultado obtenido.

### 2. Ejecuta sipub.py 

Ejecuta `sipub.py` y explica el resultado obtenido.

### 3. Modificar `sisub.py`

Modifica `sisub.py` para poder recibir los datos por `sipub.py`.

### 4. Configurar topics

Usando el código de la Pregunta 3, configura como topic del “subscriber” el valor Spain/Vlc/Code y ejecútalo. A continuación, modifica el código del “publisher” para que utilice el topic spain/vlc/code y como mensaje el texto que desees. Luego, ejecuta el “publisher”.

### 5. Opción `retain`

Prueba los siguientes pasos:

- Publica un mensaje con la opcion de retain a “False”. ¿Qué recibe el “subscriber”?

- Publica un mensaje con la opcion de retain a “True”. ¿Qué recibe el “subscriber”?   

- Publica varios mensajes (diferentes) con la opcion de retain a “True” antes de activar el “subscriber”.
    
### 6. Aplicación de chat muy básica

Crea una aplicación de chat muy básica, donde todos los mensajes publicados de cualquiera de los miembros sean recibidos solo por los miembros del grupo.

### 7. App TTN JSON

Crea una aplicacion en python utilizando el cliente mqtt-explorer para leer datos desde TTN. En este caso es suficiente imprimir todo el JSON que llega.