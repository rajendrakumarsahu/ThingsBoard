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
       global connected
       connected = True
    else:
       print("client not connected")
def on_message(client, userdata, msg):
      print("Message received:"+str(msg.payload.decode("utf-8")))
      print("Message topic :"+str(msg.topic))
messagerecieved = False
connected = False
    
client = paho.Client("MQTT")
sensor_data = {'temperature': 0, 'humidity': 0}
client.on_message = on_message
client.username_pw_set(username="mqtt", password="rajendra")
client.on_connect=on_connect
client.connect("localhost", 1883)
client.subscribe("test")
client.loop_start()
while connected !=True:
    #print("connected:::True block")
    time.sleep(1)
    
    
while messagerecieved !=True:
    time.sleep(1)
    #print("messagerecieved:::True block")
   
   
client.loop_stop()
    
