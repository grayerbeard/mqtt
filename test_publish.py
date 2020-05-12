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
from utility import make_time_text,fileexists
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

mqttc = mqtt.Client("python_pub")
mqttc.connect(config.broker_address, config.broker_port) # use the ip of your rpi here

while True:
	try:
		count += 1
		time_text = make_time_text(datetime.now())
		message =  "msg#: " + str(count) + "  Time Here is " + time_text
		mqttc.publish(config.topic,message,retain=True)
		mqttc.loop(2) #timeout = 2s
		print("My Loop# : " + str(count) + " Message sent to Topic : \"" + config.topic + "\" was >" + message + "<")
		time_sleep(config.scan_delay) # wait a bit before sending again
	except KeyboardInterrupt:
		print(".........Ctrl+C pressed... I tell everyone I am stopping")
		message =  "msg#: " + str(count) + "  I have been stopped, Time Here was " + make_time_text(datetime.now()) 
		mqttc.publish(config.topic, message)
		mqttc.loop(2) #timeout = 2s
		print("Final message sent to Topic : \"" + config.topic + "\" was >" + message + "<")
		time_sleep(2.5) 
		sys_exit()
