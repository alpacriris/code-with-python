# File: sipub.py
#
# The simplest MQTT producer.

import random
import time

import paho.mqtt.client as mqtt

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "Alpaca/Code"
CLIENT_ID = ""

def on_connect(client, userdata, flags, rc):
    print("connected to ", client._host, "port: ", client._port)
    print("flags: ", flags, "returned code: ", rc)

def on_publish(client, userdata, mid):
    print("msg published (mid={})".format(mid))


client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)

client.loop_start()

while True:

    msg_to_be_sent = random.randint(0, 100)
    print("publishing: ", msg_to_be_sent)
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=0, 
                   retain=True)

    time.sleep(1)

client.loop_stop()