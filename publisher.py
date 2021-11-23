import os
import time
import sys
import json
import paho.mqtt.client as paho
import random

#define callback
def on_connect(client, userdata, flags,rc):
    if rc==0:
       print("client is connected")
    else:
       print("client not connected")
def on_message(client, userdata, msg):
      print("Message received:"+str(msg.payload.decode("utf-8")))
      print("Message topic :"+str(msg.topic))
client = paho.Client("MQTT")
sensor_data = {'temperature': 0, 'humidity': 0}
# Set access token
client.username_pw_set(username="mqtt", password="rajendra")
client.on_connect=on_connect
client.connect("localhost", 1883)
client.subscribe("api/mqtt")
client.loop_start()
while True:
    time.sleep(1)
    sensor_data['temperature'] = random.randint(1, 100)
    sensor_data['humidity'] = random.randint(1, 100)
    client.publish('test', sensor_data['temperature'], 1)
    
