# mqtt
Developement based on https://www.elementzonline.com/blog/running-mqtt-broker-in-raspberry-pi to allow domestic instalation of R Pis and an R Pi with AIY Voice Kit to exchange data adapted for Python3.
Also incorporated info from http://www.steves-internet-guide.com/into-mqtt-python-client/    and


# Installation

'git clone https://github.com/grayerbeard/mqtt.git /home/pi/mqtt'

'sudo apt-get install mosquitto'

To edit configuration edit it using

'sudo nano /etc/mosquitto/mosquitto.conf'

I found the example configuration file needed to be unzipped see 'mosquitto_example.conf'

After editing restart the server using 

'sudo service mosquitto restart'

Install MQTT client library using the following command.

'sudo pip3 install paho-mqtt'

Check whether MQTT server is running using the following command

'sudo netstat -l -t'

My result is shown below where the 1833 items are the mosquitto running.

(You can test that by doing 'sudo service mosquitto stop' and then 'sudo service mosquitto restart')

'''pi@RPi400sd2:~/mqtt $ sudo netstat -l -t

Active Internet connections (only servers)

|Proto|Recv-Q|Send-Q|Local Address|Foreign Address|State|
| --- | --- | --- | --- | --- | --- |
|tcp|0|0|0.0.0.0:5900|0.0.0.0:*|LISTEN|     

tcp         0       0       0.0.0.0:http        0.0.0.0:*           LISTEN     

tcp        0      0 0.0.0.0:ftp             0.0.0.0:*               LISTEN     

tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     

tcp        0      0 localhost:ipp           0.0.0.0:*               LISTEN     

tcp        0      0 0.0.0.0:1883            0.0.0.0:*               LISTEN     

tcp6       0      0 [::]:5900               [::]:*                  LISTEN     

tcp6       0      0 [::]:http               [::]:*                  LISTEN     

tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     

tcp6       0      0 localhost:ipp           [::]:*                  LISTEN     

tcp6       0      0 [::]:1883               [::]:*                  LISTEN'''

You run the server on one R Pi and you run the Python3 code on other R Pis.

