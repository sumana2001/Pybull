Hello everyone to get started with pychat you just need your IP address and any port number ranging from 1-65535
but my recommendations would be take any port number above 1000 as below are already assigned to other services.
This client,server script can work on both remote and local machines.

For Eg:- IP:192.168.0.108(Local IP), 24.18.46.234(Remote IP)
         Port:6666,8080,7641

1. For Windows
      ipconfig /all

2. For Linux/MacOS
      ifconfig

1. First start the server script and enter the IP address and port number
    python server.py
    [+] Enter server address: 192.168.108
    [+] Enter server port: 8888

2. Then start the pychat script
    python pychat.py
    [+] Enter server address: 192.168.108
    [+] Enter server port: 8888
