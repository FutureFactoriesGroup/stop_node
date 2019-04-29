#!/usr/bin/env python
# license removed for brevity
import rospy
import time
import sys
import serial
from std_msgs.msg import String
import glob
import hashlib

rospy.init_node('StopNode', anonymous=True)
pub = rospy.Publisher('/system', String, queue_size=10)
time.sleep(2)

ports = glob.glob('/dev/ttyACM[0-9]*')
print(ports)

for i in ports:
	try:
		serialList.append(serial.Serial(i, 9600,timeout = 1))
		#pub.publish("Flag 1")
	except:
		pass

time.sleep(2)
inputString = ""
arduino = ports[0]

while(True):
	inputString += arduino.read()
	if(inputString.contains("Stop")):
		m = hashlib.sha256()
		DataToSend = "0051035"
		m.update(DataToSend.encode('utf-8'))
		Checksum = m.hexdigest()
		DataToSend = DataToSend + Checksum
		pub.publish(DataToSend)
