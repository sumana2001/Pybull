# To run this script
# For windows users: run cmd as administrator and specify the path to this script
# For Linux/Mac users: first run the command- sudo chmod 777 /etc/hosts to change permissions then execute this script


import time
from datetime import datetime as dt

#host path for Windows users
hostPath = r"C:\Windows\System32\drivers\etc\hosts"
#host path for Linux/Mac users: hostPath="/etc/hosts"
redirect = "127.0.0.1"
websites = []
while True:
    site = input('Enter website to block: ')
    if site=='':
        break
    else:
        websites += [site]
for site in websites:
   print('-----Set duration for blocking website----')
   startTime = input('Enter start time: ')
   endTime = input('Enter end time: ')
   if dt(dt.now().year,dt.now().month,dt.now().day, int(startTime)) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, int(endTime)):
        print ("Website blocked")
        with open(hostPath,'r+') as file:
            contents = file.read()
        if site in contents:
            pass
        else:
            file.write(redirect+" "+site+"\n")
   else:
      with open(hostsPath,'r+') as file:
          contents = file.readlines()
          file.seek(0)
          for line in contents:
             if not any (site in line for site in websites):
                file.write(line)
             file.truncate()
      print ("Access Permitted")
time.sleep(2)
