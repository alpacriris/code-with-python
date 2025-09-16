# Prácticas MQTT con Python

Práctica de Python centrada en el uso de MQTT para comunicación entre clientes y publicación/suscripción a *topics*.

## Índice
1. [Ejecuta `sisub.py`](#1-ejecuta-sisubpy)
2. [Ejecuta `sipub.py`](#2-ejecuta-sipubpy)
3. [Modificar `sisub.py`](#3-modificar-sisubpy)
4. [Configurar topics](#4-configurar-topics)
5. [Opción `retain`](#5-opción-retain)
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
$ python sisub.py
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

### Solución:
1. El cliente se conecta al broker [*test.mosquitto.org*](http://test.mosquitto.org/) y se prepara para enviar mensajes al topic definido:  
    ```python
    THE_BROKER = "test.mosquitto.org"
    THE_TOPIC = "Alpaca/Code"
    client.connect(THE_BROKER, port=1883, keepalive=60)
    ```

2. Se definen dos funciones de *callback* para manejar los eventos:  
    ```python
    def on_connect(client, userdata, flags, rc):
        # Se ejecuta al conectarse al broker
        ...

    def on_publish(client, userdata, mid):
        # Se ejecuta al publicar un mensaje
        ...
    ```

    - **`on_connect`**: confirma la conexión con el broker.  
    - **`on_publish`**: indica que un mensaje ha sido publicado correctamente.  

3. Se activa el bucle del cliente para gestionar la comunicación en segundo plano:  
    ```python
    client.loop_start()
    ```

4. En un bucle infinito, se genera un número aleatorio entre 0 y 100 y se publica cada segundo en el topic `Alpaca/Code`:  
    ```python
    while True:
        msg_to_be_sent = random.randint(0, 100)
        print("publishing: ", msg_to_be_sent)
        client.publish(THE_TOPIC,
                       payload=msg_to_be_sent,
                       qos=0,
                       retain=True)
        time.sleep(1)
    ```

    - `random.randint(0, 100)`: genera el número aleatorio.  
    - `retain=True`: el último mensaje queda almacenado en el broker.  
    - `time.sleep(1)`: envía mensajes con un intervalo de 1 segundo.  

El resultado de la ejecución muestra la conexión al broker y la publicación periódica de mensajes:  

```bash
$ python sipub.py
publishing:  99
sipub: msg published (mid=1)
connected to  test.mosquitto.org port:  1883
flags:  {'session present': 0} returned code:  0
publishing:  43
sipub: msg published (mid=2)
publishing:  69
sipub: msg published (mid=3)
...
```

---

## 3. Modificar `sisub.py`

Modifica `sisub.py` para poder recibir los datos enviados por `sipub.py`.

### Solución

1. **Suscribirse al mismo topic** que usa `sipub.py`. Debe coincidir con el topic usado en `sipub.py`:

    ```python
    THE_TOPIC = "Alpaca/Code"
    client.subscribe(THE_TOPIC, qos=0)
    ``` 
2. Ejecutar ambos programas (primero `sisub.py` y luego `sipub.py`):

    ```bash
    $ python sisub.py
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    message received with topic: Alpaca/Code and payload: b'40'
    message received with topic: Alpaca/Code and payload: b'93'
    ...
    ```

    ```bash
    $ python sipub.py
    publishing:  40
    sipub: msg published (mid=1)
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    publishing:  93
    sipub: msg published (mid=2)
    publishing:  23
    sipub: msg published (mid=3)
    publishing:  87
    ...
    ```
El suscriptor recibe correctamente los mensajes publicados por el publicador en el topic `Alpaca/Code`. Esto demuestra que `sisub.py` está recibiendo todos los mensajes enviados por `sipub.py`.

---

## 4. Configurar topics

Usando el código de la Pregunta 3, configura como topic del “subscriber” el valor Spain/Vlc/Code y ejecútalo. A continuación, modifica el código del “publisher” para que utilice el topic spain/vlc/code y como mensaje el texto que desees. Luego, ejecuta el “publisher”.

### Solución:

1. Modifica el *subscriber* para suscribirse al nuevo topic `Spain/Vlc/Code`:

    ```python
    THE_TOPIC = "Spain/Vlc/Code"
    client.subscribe(THE_TOPIC, qos=0)
    ```

2. Modifica el *publisher* para publicar en el topic `spain/vlc/code`:

    ```python
    THE_TOPIC = "spain/vlc/code"
    client.publish(THE_TOPIC, payload=msg_to_be_sent, qos=0, retain=True)
    ```

3. Ejecutamos primero el *subscriber* y luego el *publisher*:

    ```bash
    $ python sisub.py
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    ```

    ```bash
    $ python sipub.py
    publishing:  75
    sipub: msg published (mid=1)
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    publishing:  79
    sipub: msg published (mid=2)
    publishing:  24
    sipub: msg published (mid=3)
    publishing:  14
    sipub: msg published (mid=4)
    publishing:  6
    ...
    ```

El *subscriber* no recibe ningún mensaje publicado por el *publisher*, puesto que **los topics distinguen entre mayúsculas y minúsculas**.
Esto significa que el *subscriber* no está suscrito al topic correcto.

---

## 5. Opción `retain`

Prueba los siguientes pasos:

- Publica un mensaje con la opcion de retain a “False”. ¿Qué recibe el “subscriber”?

- Publica un mensaje con la opcion de retain a “True”. ¿Qué recibe el “subscriber”?   

- Publica varios mensajes (diferentes) con la opcion de retain a “True” antes de activar el “subscriber”.

### Solución:

- Publica un mensaje con la opcion de retain a “False”. ¿Qué recibe el “subscriber”?

    ```python
    msg1 = "1: Never Mind."
    client.publish(THE_TOPIC, payload=msg1, qos=0, retain=False)
    ```

    Al ejecutar:

    ```bash
    $ python sipub.py
    sipub: msg published (mid=1)
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0        
    sipub: msg published (mid=1)
    ```
    ```bash
    $ python sisub.py
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    ```

    - El mensaje **no se almacena** en el broker.

    - Los `subscribers` que se conecten después de la publicación **no recibirán** este mensaje.

- Publica un mensaje con la opcion de retain a “True”. ¿Qué recibe el “subscriber”?

    ```python
    msg1 = "1: Never Mind."
    client.publish(THE_TOPIC, payload=msg1, qos=0, retain=True)
    ```

    ```bash
    $ python sipub.py
    sipub: msg published (mid=1)
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0        
    sipub: msg published (mid=1)
    ```
    ```
    $ python sisub.py
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    message received with topic: nevermind and payload: b'1: Never Mind.'
    ```

    En este caso, el mensaje **sí se ha almacenado** en el broker, por lo que el subscriber recibe correctamente el mensaje retenido.

- Publica varios mensajes (diferentes) con la opcion de retain a “True” antes de activar el “subscriber”.

    Esta vez publicamos cuatro mensajes:

    ```python
    msg1 = "1: Never Mind."
    msg2 = "2: Never Mind."
    msg3 = "3: Never Mind."
    msg4 = "4: Never Mind."
    client.publish(THE_TOPIC, payload=msg1, qos=0, retain=True)
    client.publish(THE_TOPIC, payload=msg2, qos=0, retain=True)
    client.publish(THE_TOPIC, payload=msg3, qos=0, retain=True)
    client.publish(THE_TOPIC, payload=msg4, qos=0, retain=True)
    ```

    ```bash
    $ python sipub.py
    sipub: msg published (mid=1)
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0        
    sipub: msg published (mid=1)
    sipub: msg published (mid=2)
    sipub: msg published (mid=3)
    sipub: msg published (mid=4)
    ```
    ```
    $ python sisub.py
    connected to  test.mosquitto.org port:  1883
    flags:  {'session present': 0} returned code:  0
    message received with topic: nevermind and payload: b'4: Never Mind.'
    ```

    Al conectarse, el suscriptor recibe únicamente **el último mensaje** publicado, ya que solo se retiene un mensaje por topic; los mensajes anteriores se sobrescriben.

---

## 6. Aplicación de chat muy básica

Crea una aplicación de chat muy básica, donde todos los mensajes publicados de cualquiera de los miembros sean recibidos solo por los miembros del grupo.

### Solución:

El archivo [`chat.py`](./chat.py) implementa un chat simple utilizando MQTT.  

1. Se define el broker y el topic de comunicación:  
    ```python
    THE_BROKER = "test.mosquitto.org"
    THE_TOPIC = "rse/chat"
    ```

2. Al conectarse, cada usuario introduce su nickname y se suscribe al topic:  
    ```python
    def on_connect(client, userdata, flags, rc):
        global CLIENT_NAME
        client.subscribe(THE_TOPIC, qos=0)
        CLIENT_NAME = input("Tell me your nickname: ")
    ```

3. La función `on_message` recibe los mensajes publicados por otros miembros:  
    ```python
    def on_message(client, userdata, msg):
        print(msg.payload.decode("utf-8"))
    ```

4. El bucle principal permite enviar mensajes al grupo, con el nickname del remitente:  
    ```python
    msg = input("")
    client.publish(THE_TOPIC, payload=f"{CLIENT_NAME}: {msg}", qos=0, retain=False)
    ```

#### Explicación:
- Cada usuario se suscribe al topic `rse/chat` y recibe los mensajes publicados por otros.

- El nickname `CLIENT_NAME` se añade al mensaje publicado para identificar al remitente.

- La opción `retain=False` asegura que los mensajes no se guarden en el broker para futuras conexiones.

- Se utiliza un bucle infinito junto con `input()` para permitir la entrada continua de mensajes.

- Todos los mensajes publicados en el topic son recibidos por cada suscriptor activo en tiempo real.

Si suponemos dos miembros en el grupo y para cada uno ejecutamos el `chat.py` anterior:
        
```bash
$ python chat.py
Connected to test.mosquitto.org  port:  1883
Tell me your nickname: alvaro
----------------------------------------------
Welcome alvaro ! You can start chatting now!
----------------------------------------------
someone there?
alvaro: someone there?
cristina: hi!
hello cristina!
alvaro: hello cristina!
cristina: nice to meet you!
```

```bash
$ python chat.py
Connected to test.mosquitto.org  port:  1883
Tell me your nickname: cristina
----------------------------------------------
Welcome cristina ! You can start chatting now!
----------------------------------------------
alvaro: someone there?
hi!
cristina: hi!
alvaro: hello cristina!
nice to meet you!
cristina: nice to meet you!
```
---

## 7. App TTN JSON

Crea una aplicacion en python utilizando el cliente mqtt-explorer leemos datos desde TTN. En este caso es suficiente imprimir todo el JSON que llega. 

### Solución:

En este ejemplo se implementa un cliente MQTT que se conecta al broker de **The Things Network (TTN)** para recibir mensajes de los dispositivos registrados y mostrarlos en formato JSON. El código completo se encuentra en [`ttn_sub.py`](./ttn_sub.py).

1. Se definen las credenciales y parámetros de conexión en un diccionario:

    ```python
    mqtt_options = {
        "broker": "eu1.cloud.thethings.network",
        "username": "mi-aplicacion@ttn",
        "password": "NNSXS.xxxxxxxx",
        "topic": "v3/+/devices/#"
    }
    ```

2. La función `on_connect` se ejecuta al establecer la conexión y suscribe al topic definido:
    ```python
    def on_connect(client, userdata, flags, rc):
        client.subscribe(mqtt_options["topic"])
    ```
3. La función `on_message` imprime los mensajes recibidos en formato JSON legible:
    ```python
    def on_message(client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)
        print(json.dumps(data, indent=4))
    ```

4. Finalmente, se configuran las credenciales, se conecta al broker y se mantiene en escucha con:
    ```python
    client.username_pw_set(mqtt_options["username"], mqtt_options["password"])
    client.connect(mqtt_options["broker"])
    client.loop_forever()
    ```

#### Explicación:

- El cliente se conecta al broker de TTN y se suscribe al topic configurado para recibir mensajes de los dispositivos de la aplicación.

- Cada mensaje recibido se decodifica de JSON y se muestra de forma legible en consola.

- Esto permite visualizar en tiempo real los datos enviados por los dispositivos IoT registrados en TTN.

- La opción `loop_forever()` mantiene activo el cliente a la espera de nuevos mensajes.

Resultado de la ejecución presenta una estructura similar a:

```bash
connected to eu1.cloud.thethings.network  port: 1883
{
    "end_device_ids": {
        "device_id": "example-device",
        "application_ids": {
            "application_id": "example-app"
        }
    },
    "received_at": "2025-12-12T23:23:23Z",
    "uplink_message": {
        "f_port": 2,
        "f_cnt": 4011,
        "decoded_payload": {
            "humidity": 56.0,
            "lux": -17,
            "temperature": 29.7
        },
        "rx_metadata": [
            {
                "gateway_ids": {
                    "gateway_id": "example-gateway"
                },
                "rssi": -97,
                "snr": 8.2
            },
            {
                "gateway_ids": {
                    "gateway_id": "another-gateway"
                },
                "rssi": -21,
                "snr": 11
            }
        ],
        "settings": {
            "frequency": "868100000",
            "data_rate": {
                "lora": {
                    "spreading_factor": 12
                }
            }
        }
    }
}
```