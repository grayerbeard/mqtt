# mqtt
Developement based on https://www.elementzonline.com/blog/running-mqtt-broker-in-raspberry-pi to allow domestic instalation of R Pis and an R Pi with AIY Voice Kit to exchange data adapted for Python3.
Also incorporated info from http://www.steves-internet-guide.com/into-mqtt-python-client/    and several other places.

The aim was to develope the code so that it was ready to be inserted into an application where the clinent was runnings a constant loop that at any stage might want to get the latest state of the publishers status.


# Installation

Ideally use three R Pi and get set up so that they each have a separate function. 

I found it easiest to control things from my Windows 10 Laptop where I set up FileZilla FTP Client and Termius" SSH client so that they can both communicate to all three devices, and when developing also with a browser to GitHub.

(If you use GitHub then you could start by Forking off this repository and then cloning from there rather than cloning to each device as no doubt you will want to try changes) 

## MQTT Server

R Pi "One" is the MQTT server where you install 'mosquitto' MQTT server using 

'sudo apt-get install mosquitto'

To edit configuration edit it using

'sudo nano /etc/mosquitto/mosquitto.conf'

I found the example configuration file needed to be unzipped see 'mosquitto_example.conf'.  However I have not yet found it necessary to modify the configuration.

After editing restart the server using 

'sudo service mosquitto restart'

Install MQTT client library using the following command.

'sudo pip3 install paho-mqtt'

Check whether MQTT server is running using the following command

'sudo netstat -l -t'

My result is shown below where the 1833 items are the mosquitto running.

(You can test that by doing 'sudo service mosquitto stop' and then 'sudo service mosquitto restart')

Active Internet connections (only servers)

|Proto|Recv-Q|Send-Q|Local Address|Foreign Address|State|
| --- | --- | --- | --- | --- | --- |
|tcp|0|0|0.0.0.0:5900|0.0.0.0:*|LISTEN|     
|tcp|0|0|0.0.0.0:http|0.0.0.0:*|LISTEN|     
|tcp|0|0|0.0.0.0:ftp|0.0.0.0:*|LISTEN|     
|tcp|0|0|0.0.0.0:ssh|0.0.0.0:*|LISTEN|     
|tcp|0|0|localhost:ipp|0.0.0.0:*|LISTEN|     
|tcp|0|0|0.0.0.0:1883|0.0.0.0:*|LISTEN|    
|tcp6|0|0|[::]:5900|[::]:*|LISTEN|     
|tcp6|0|0|[::]:http|[::]:*|LISTEN|     
|tcp6|0|0|[::]:ssh|[::]:*|LISTEN|     
|tcp6|0|0|localhost:ipp|[::]:*|LISTEN|     
|tcp6|0|0|[::]:1883|[::]:*|LISTEN|

## Publishers and Subscribers

So now you have the Nessage "Telephone exchange" running and you need a "sender" and a "receiver".

On idealy two but one will work Install the code from this repository using

'git clone https://github.com/grayerbeard/mqtt.git /home/pi/mqtt'

Then run the relavant Python scripts on each R Pi or I have provided commands to start them in Tmux sessions (for that you may need to install tmux with sudo apt install tmux)

