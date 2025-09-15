#
# 6. A simple chat application using MQTT
#
import paho.mqtt.client as mqtt
import time
import json

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = 'rse/chat'

def on_connect(client, userdata, flags, rc):
  global CLIENT_NAME
  print("Connected to", client._host, " port: ", client._port)

  client.subscribe(THE_TOPIC, qos=0)
  CLIENT_NAME = input("Tell me your nickname: ")
  print("-----------------------------------------------")
  print(" Welcome", CLIENT_NAME, "! You can start chatting now!")
  print("-----------------------------------------------")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)
        print(json.dumps(data, indent=4))
    except Exception:
        print(payload)  # Si no es JSON válido, imprime plano


client = mqtt.Client(client_id="",
                     clean_session=True,
                     userdata=None,
                     protocol=mqtt.MQTTv311,
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.connect(THE_BROKER, port=1883, keepalive=60)

client.loop_start()
while True:
  time.sleep(1)
  msg = input("")
  client.publish(THE_TOPIC, payload=CLIENT_NAME+": "+msg, qos=0, retain=False)
client.loop_stop()
