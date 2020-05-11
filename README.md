# mqtt
Developement based on https://www.elementzonline.com/blog/running-mqtt-broker-in-raspberry-pi to allow domestic instalation testing of R Pis using MQTT to pulish/subscribe information.  The code is configured with the aim of allowing easy incorporation into another program.

Also incorporated info from http://www.steves-internet-guide.com/into-mqtt-python-client/ and several other places.

# Installation

Ideally use three R Pi and get set up so that they each have a separate function. Server or Publisher or Subscriber. 

I found it easiest to control things from my Windows 10 Laptop where I set up FileZilla FTP Client and Termius" SSH client so that they can both communicate to all three devices, and when developing also with a browser to GitHub.

(If you use GitHub then you could start by Forking off this repository and then cloning from there rather than cloning to each device as no doubt you will want to try changes) 

## MQTT Server

R Pi "One" is the MQTT server where you install 'mosquitto' MQTT server using. You DO NOT need this on either the Subscriber or the Publisher.  Also you do not need the  

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

So now you have the Message "Telephone exchange" running and you need a "sender" and a "receiver".

On idealy two but one will work Install the code from this repository using

'git clone https://github.com/grayerbeard/mqtt.git /home/pi/mqtt'

Then install the python module using

'sudo pip3 install paho-mqtt'

Then run the relavant Python scripts on each R Pi. (or I have provided commands to start them in Tmux sessions for that you may need to install tmux with 'sudo apt install tmux')

First on the publisher

'python3 test_publisher.py'

Then on the subscriber 

'python3 test_subscriber.py'

The subscriber loops less often than the publisher and the format would allow the subscriber to be any looping control program that needs to sometimes get the status of the publisher.

