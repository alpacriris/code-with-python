#
# 7. Subscribe to TTN MQTT broker and print incoming messages in JSON format
#
import paho.mqtt.client as mqtt
import json

mqtt_options = {
    "broker": "eu1.cloud.thethings.network",
    "username": "mi-aplicacion@ttn",    # cambiar por tu aplicación en TTN
    "password": "NNSXS.xxxxxxxx",       # cambiar por la clave generada en TTN
    "topic": "v3/+/devices/#"
}

def on_connect(client, userdata, flags, rc):
    print("connected to", client._host, " port:", client._port)

    client.subscribe(mqtt_options["topic"])
    
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    try:
        data = json.loads(payload)          # convierte a diccionario
        print(json.dumps(data, indent=4))   # imprime en formato JSON
    except json.JSONDecodeError:
        print("No es JSON válido:", payload)
    
client = mqtt.Client(
    client_id="",
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport="tcp"
)

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(mqtt_options["username"], password=mqtt_options["password"])
client.connect(mqtt_options["broker"])

client.loop_forever()