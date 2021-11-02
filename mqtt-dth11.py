import os
import RPi.GPIO as GPIO
import dht11
import time
import sys
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import json

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'Od13UATandxRHHjXMdvr'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)
sensor_data = {'temperature': 0, 'humidity': 0}

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
        result = instance.read()
        temperature = result.temperature
        humidity = round(result.humidity, 2)
        temperature = round(temperature, 2)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
