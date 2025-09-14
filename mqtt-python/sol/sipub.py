# File: sipub.py
#
# The simplest MQTT producer.

import random
import time

import paho.mqtt.client as mqtt

THE_BROKER = "test.mosquitto.org"
#THE_TOPIC = "Alpaca/Code"          # 2. publish to this topic
#THE_TOPIC = "spain/vlc/code"        # 4. publish to the topic "spain/vlc/code" 
THE_TOPIC = "nevermind"             # 5. publish to the topic "nevermind"

CLIENT_ID = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("connected to ", client._host, "port: ", client._port)
    print("flags: ", flags, "returned code: ", rc)

# The callback for when a message is published.
def on_publish(client, userdata, mid):
    print("sipub: msg published (mid={})".format(mid))

client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)


# 5. publish several messages with retain=True
msg1 = "1: Never Mind."
msg2 = "2: Never Mind."
msg3 = "3: Never Mind."
msg4 = "4: Never Mind."
client.publish(THE_TOPIC, payload=msg1, qos=0, retain=False)
# client.publish(THE_TOPIC, payload=msg2, qos=0, retain=True)
# client.publish(THE_TOPIC, payload=msg3, qos=0, retain=True)
# client.publish(THE_TOPIC, payload=msg4, qos=0, retain=True)
# end of 5.

# client.loop_start()

# while True:

#     msg_to_be_sent = random.randint(0, 100) 
#     print("publishing: ", msg_to_be_sent) 
#     client.publish(THE_TOPIC, 
#                    payload=msg_to_be_sent, 
#                    qos=0, 
#                    retain=False)      
    
#     time.sleep(1)

# client.loop_stop()

client.disconnect()