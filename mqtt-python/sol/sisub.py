# File: sisub.py
#
# The simplest MQTT subscriber.

import paho.mqtt.client as mqtt

THE_BROKER = "test.mosquitto.org"
#THE_TOPIC = "$SYS/#"           # 1. subscribe to all topics
THE_TOPIC = "Alpaca/Code"      # 3. subscribe to the topic to which we publish
#THE_TOPIC = "spain/vlc/code"    # 4. subscribe to the topic "Spain/Vlc/Code"
#THE_TOPIC = "nevermind"        # 5. subscribe to the topic "nevermind"
CLIENT_ID = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("connected to ", client._host, "port: ", client._port)
    print("flags: ", flags, "returned code: ", rc)

    client.subscribe(THE_TOPIC, qos=0)

# The callback for when a message is received from the server.
def on_message(client, userdata, msg):
    print("sisub: message received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))

client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()

client.disconnect()