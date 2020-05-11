# -*- coding: utf-8 -*-
'''
Developed By: Dhanish Vijayan
Company: Elementz Engineers Guild Pvt Ltd
'''
import paho.mqtt.client as mqtt
# The callback for when the client receives a CONNACK response from the server.
def on_connect(self, client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    self.subscribe("House/test")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.120", 1883, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()