# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:47:55 2018

@author: dmccaslin
"""

import socket
import subprocess
import sys
from datetime import datetime

#clear the screen
subprocess.call('clear',shell=True)

#ask for input
remoteServer = input("Enter a remote host: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a Banner
print("-",60)
print("Please wait, scanning remote host " + remoteServerIP)
print("-",60)

#Check what time the scan started
t1 = datetime.now()

#Using range function, specify ports
successes = []

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        print("Trying port ",port)
        if result == 0:
            print("Port{}: Open".format(port))
            successes.append(port)
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except sock.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except sock.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()
# Create a dictionary of popular ports
popports = {22:'ssh',23:'telnet',25:'smtp',53:'dns',67:'dhcp',69:'tftp',
            80:'http',110:'pop3',143:'imap',389:'ldap',443:'https'}
# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)
print('Open Ports: ')
for i in range(len(successes)):
    print(successes[i],':',popports[successes[i]])

