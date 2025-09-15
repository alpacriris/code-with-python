# File: sisub.py
#
# The simplest MQTT subscriber.

import paho.mqtt.client as mqtt

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "Alpaca/Code" # subscribe to all topics
CLIENT_ID = ""

def on_connect(client, userdata, flags, rc):
    print("connected to ", client._host, "port: ", client._port)
    print("flags: ", flags, "returned code: ", rc)

    client.subscribe(THE_TOPIC, qos=0)

def on_message(client, userdata, msg):
    print("message received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))

client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)

client.loop_forever()
