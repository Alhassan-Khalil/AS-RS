#!/usr/bin/python

import time
import os
from subprocess import call,Popen

#Popen(['xterm','-e','roscore'])
#os.system("gnome-terminal -e 'roscore'")
os.system("gnome-terminal -e 'bash -c \"roscore; exec bash\"'")
time.sleep(5)


#Popen(['xterm','-e','rosrun rosserial_python serial_node.py /dev/ttyACM0'])
#os.system("gnome-terminal 'rosrun rosserial_python serial_node.py /dev/ttyACM0'")
os.system("gnome-terminal -e 'bash -c \"rosrun rosserial_python serial_node.py /dev/ttyACM0; exec bash\"'")
time.sleep(10)


#Popen(['xterm','-e','python main_GUI.py'])
#os.system("gnome-terminal 'python main_GUI.py'")
os.system("gnome-terminal -e 'bash -c \"python main_GUI.py; exec bash\"'")
