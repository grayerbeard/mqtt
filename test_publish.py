#!/usr/bin/env python3
 
'''
Developed By: Dhanish Vijayan
Company: Elementz Engineers Guild Pvt Ltd
'''
import paho.mqtt.client as mqtt
mqttc = mqtt.Client("python_pub")
mqttc.connect("192.168.0.120", 1883) # use the ip of your rpi here
mqttc.publish("Elementz/welcome", "Welcome to Open Source")
mqttc.loop(2) #timeout = 2s
