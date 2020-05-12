#!/usr/bin/env python3
'''
Developed By: Dhanish Vijayan
Company: Elementz Engineers Guild Pvt Ltd
https://www.elementzonline.com/blog/running-mqtt-broker-in-raspberry-pi
addapted by David Torrens (https://github.com/grayerbeard/mqtt) based on info from
http://www.steves-internet-guide.com/into-mqtt-python-client/

Was revised to work with Python3
'''

import paho.mqtt.client as mqtt
from time import sleep as time_sleep
from utility import fileexists
from datetime import datetime
from sys import exit as sys_exit
from config import class_config

config = class_config()
if fileexists(config.config_filename):		
	print( "will try to read Config File : " ,config.config_filename)
	config.read_file() # overwrites from file
else : # no file so file needs to be writen
	config.write_file()
	print("New Config File Made with default values, you probably need to edit it")
	
count = 0
# set latest_message global so that on_message can set it with latest info
global latest_msg

# The callback for when the client receives a CONNACK response from the server.
def on_connect(self, client, userdata, rc):
	''' Result Codes
	0: Connection successful 
	1: Connection refused – incorrect protocol version 
	2: Connection refused – invalid client identifier 
	3: Connection refused – server unavailable 
	4: Connection refused – bad username or password 
	5: Connection refused – not authorised 
	6-255: Currently unused. 
	Subscribing in on_connect() means that if we lose the connection and
	reconnect then subscriptions will be renewed.'''
	print("Connected with result code "+str(rc))
	self.subscribe(config.topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	global latest_msg
	latest_msg = msg

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(config.broker_address, config.broker_port, 60)
# Set up the client to keep listening
client.loop_start()
try:
	# Loop at a slower rate that the new messages are published and print latest info
	while True:
		count += 1
		time_sleep(1.33 * config.scan_delay)
		print("My Loop Count (every " + str(1.33 * config.scan_delay) + " seconds) : " + str(count)
		+ "  Message Received on Topic \"" + config.topic + "\" was >" + latest_msg.payload.decode() + "<") 
except KeyboardInterrupt:
	print(".........Ctrl+C pressed... I am stopping")
	print("Last Message Received on Topic : \"" + config.topic + "\" was >" + latest_msg.payload.decode() + "<") 
	client.loop_stop() 
	time_sleep(2.5) 
	sys_exit()
