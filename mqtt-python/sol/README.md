# Prácticas MQTT con Python

Práctica de Python centrada en el uso de MQTT para comunicación entre clientes y publicación/suscripción a topics.

## Índice
1. [Ejecuta `sisub.py`](#1-ejecuta-sisubpy)
2. [Ejecuta `sipub.py`](#2-ejecuta-sipubpy)
3. [Modificar `sisub.py`](#3-modificar-sisubpy)
4. [Configurar topics](#4-configurar-topics)
5. [Opción `retained`](#5-opción-retained)
6. [Aplicación de chat muy básica](#6-aplicación-de-chat-muy-básica)
7. [App TTN JSON](#7-app-ttn-json)

---

## 1. Ejecuta `sisub.py` 

Ejecuta `sisub.py` y explica el resultado obtenido.

### Solución:
1. El cliente se conecta al broker [*test.mosquitto.org*](http://test.mosquitto.org/), lo que permite realizar distintas pruebas con MQTT:
    ```python
    THE_BROKER = "test.mosquitto.org"
    client.connect(THE_BROKER, port=1883, keepalive=60)
    ```

2. Nos suscribimos al topic `$SYS/#` para recibir todos los mensajes del grupo $SYS.

    El segundo parámetro `qos` (Quality of Service) indica la garantía de entrega del mensaje:

    - Nivel 0: el mensaje se envía una sola vez y no se garantiza la entrega.

3. Se definen dos funciones de callback para manejar eventos:

    ```python
    def on_connect(client, userdata, flags, rc):
        # Se ejecuta al conectarse al broker
        ...

    def on_message(client, userdata, msg):
        # Se ejecuta al recibir un mensaje

    ...

    client.on_connect = on_connect
    client.on_message = on_message
    ```

4. Bucle principal que mantiene siempre activo, esperando la recepción de mensajes
    ```python
    client.loop_forever()
    ```

El resultado de la ejecución muestra de manera continua los mensajes recibidos al suscribirse a una serie de topics:
    
```bash
connected to  test.mosquitto.org port:  1883
flags:  {'session present': 0} returned code:  0
message received with topic: $SYS/broker/bytes/received and payload:
b'842828392053'
message received with topic: $SYS/broker/bytes/sent and payload:
b'14649543471842
...
```
---

## 2. Ejecuta sipub.py 

Ejecuta `sipub.py` y explica el resultado obtenido.

---

## 3. Modificar `sisub.py`

Modifica `sisub.py` para poder recibir los datos por `sipub.py`.

---

## 4. Configurar topics

Usando el código de la Pregunta 3, configura como topic del “subscriber” el valor Spain/Vlc/Code y ejecútalo. A continuación, modifica el código del “publisher” para que utilice el topic spain/vlc/code y como mensaje el texto que desees. Luego, ejecuta el “publisher”.

---

## 5. Opción `retained`

Prueba los siguientes pasos:

- Publica un mensaje con la opcion de retained a “False”. ¿Qué recibe el “subscriber”?

- Publica un mensaje con la opcion de retained a “True”. ¿Qué recibe el “subscriber”?   

- Publica varios mensajes (diferentes) con la opcion de retained a “True” antes de activar el “subscriber”.

---

## 6. Aplicación de chat muy básica

Crea una aplicación de chat muy básica, donde todos los mensajes publicados de cualquiera de los miembros sean recibidos solo por los miembros del grupo.

---

## 7. App TTN JSON

Crea una aplicacion en python utilizando el cliente mqtt-explorer leemos datos desde TTN. En este caso es suficiente imprimir todo el JSON que llega. 