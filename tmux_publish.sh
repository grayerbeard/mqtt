#!/bin/bash
cd /home/pi/mqtt
echo looking to kill any old tmux mqtt_p session
tmux kill-session -t mqtt_p
echo now new tmux sauna session 
tmux new-session -d -s mqtt_p 'python3 test_publish.py'

