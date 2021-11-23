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
sensor_data = {
	"deviceName": "WESCO001000",
	"deviceFriendlyName": "Smart Meter Sensor",
	"deviceId": "784f394c-42b6-435a-983c-b7beff2784f9",
	"totalPowerConsumed": 5500,
	"topics": {
		"eventTopic": {
			"timeStamp": "Unix time Stamp",
			"activePower": 9000,
			"eventType": "High Active Power, Device Fault",
			"deviceName": "WESCO001000",
			"deviceId": "784f394c-42b6-435a-983c-b7beff2784f9",
			"deviceFriendlyName": "Smart Meter Sensor"
		},
		"telemteryTopic": {
			"timeStamp": "Unix time Stamp",
			"activePower": 9000,
			"reactivePower": 3000,
			"deviceName": "WESCO001000",
			"deviceId": "784f394c-42b6-435a-983c-b7beff2784f9",
			"deviceFriendlyName": "Smart Meter Sensor"
		},
		"attributeTopic": {
			"timeStamp": "Unix time Stamp",
			"activePower": 9000,
			"reactivePower": 3000,
			"totalPowerConsumed": 2500,
			"deviceName": "WESCO001000",
			"deviceId": "784f394c-42b6-435a-983c-b7beff2784f9",
			"deviceFriendlyName": "Smart Meter Sensor"
		}
	}
}
# Set access token
client.username_pw_set(username="mqtt", password="rajendra")
client.on_connect=on_connect
client.connect("localhost", 1883)
client.loop_start()
while True:
    time.sleep(1)
    sensor_data['totalPowerConsumed'] = random.randint(1, 1000)
    sensor_data['topics']['eventTopic']['activePower'] = random.randint(1, 1000)
    sensor_data['topics']['telemteryTopic']['activePower'] = random.randint(1, 1000)
    sensor_data['topics']['telemteryTopic']['reactivePower'] = random.randint(1, 1000)
    sensor_data['topics']['attributeTopic']['activePower'] = random.randint(1, 1000)
    sensor_data['topics']['attributeTopic']['reactivePower'] = random.randint(1, 1000)
    client.publish('api/mqtt/publish', json.dumps(sensor_data), 1)
    
