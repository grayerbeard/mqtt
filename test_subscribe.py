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
from utility import make_time_text
from datetime import datetime

broker_address = "192.168.0.120" # Change to suite your brokers address
broker_port = 1883 # Check on server port being used 'sudo netstat -l -t'
topic_top = "House"
topic_sub = "test"
topic_separator = "/"
count = 0
house_test_latest.msg = ""
house_test_latest.count = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(self, client, userdata, rc):
	print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	self.subscribe(topic_top + topic_separator + topic_sub)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	count += 1
	if msg.topic = topic_top + topic_separator + topic_sub:
		house_test_latest.msg = str(msg.payload)
		house_test_latest.count = count
	else:
		print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()

while True:
	print("Msg# :",house_test_latest.count," Time: ",make_time_text(datetime.now()),"\n","  Latest House/Test Message is : ",house_test_latest,"\n")
	time_sleep(7) 
