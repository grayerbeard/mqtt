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
from sys import exit as sys_exit

broker_address = "192.168.0.120" # Change to suite your brokers address
broker_port = 1883 # Check on server port being used 'sudo netstat -l -t'
topic_top = "House"
topic_sub = "test"
topic_separator = "/"
count = 0

mqttc = mqtt.Client("python_pub")
mqttc.connect(broker_address, broker_port) # use the ip of your rpi here


while True:
	try:
		count += 1
		time_text = make_time_text(datetime.now())
		message =  "msg#: " + str(count) + "  Time Here is " + time_text
		# mqttc.publish(topic_top + topic_separator + topic_sub, message)
		mqttc.publish("House/test", message,retain=True)
		mqttc.loop(2) #timeout = 2s
		print("Loop : ",count," At : ",time_text)
		time_sleep(10) # wait a bit before sending again
	except KeyboardInterrupt:
		print(".........Ctrl+C pressed... I will stop")
		message =  "msg#: " + str(count) + "I have been stopped, Time Here is " + make_time_text(datetime.now()) 
		mqttc.publish(topic_top + topic_separator + topic_sub, message)
		mqttc.loop(2) #timeout = 2s
		time_sleep(2.5) 
		sys_exit()
