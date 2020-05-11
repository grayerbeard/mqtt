#!/bin/bash
cd /home/pi/mqtt
echo looking to kill any old tmux mqtt_s session
tmux kill-session -t mqtt_s
echo now new tmux sauna session 
tmux new-session -d -s mqtt_s 'python3 test_subscribe.py'

