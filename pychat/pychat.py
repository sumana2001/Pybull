#! /usr/bin/python3

"""
__Description__='This is a simple script which establishes socket connection
between server and client using TCP protocol and python socket
library.'
"""

from socket import *


#Function: To display the banner
def Banner():
    print("""
    ________              ______        _____
    ___  __ \____  __________  /_______ __  /_
    __  /_/ /_  / / /  ___/_  __ \  __ `/  __/
    _  ____/_  /_/ // /__ _  / / / /_/ // /_
    /_/     _\__, / \___/ /_/ /_/\__,_/ \__/
            /____/                             Version 1.0
    """)


#Function: Asking user for server address and port
def User_Input():


    #Function: For validating IP address
    def Valid_IP():
        while True:
            try:
                host = input("[+] Enter server address: ")
                valid_ip = host.split('.')
                for items in valid_ip:
                    if(len(valid_ip) == 4 and int(items)):
                        return host
                    else:
                        print("[+] Enter a valid IP")
                        continue
            except ValueError:
                    print("[+] Enter a valid IP")
                    continue


    #Function: For validating port number
    def Valid_Port():
        while True:
            try:
                port = int(input("[+] Enter server port: "))
                if(port > 0 and port < 65535):
                    pass
                else:
                    print("[+] Port must be 0-65535")
                    continue
            except ValueError:
                print("[+] Enter a valid port number")
                continue
            else:
                break
        return port

    host, port = Valid_IP(), Valid_Port()

    return host, port


#Function: To exit or continue the connection
def Client_Exit():
    while True:
        user_value = input("[+] Want to send more messages? (y/n): ")
        if (user_value == 'y' or user_value == 'n'):
            return user_value
        else:
            print("[+] Wrong input")
            continue


#Function: To setup and communicate with the server
def Client_Setup():

    #Printing the banner
    Banner()

    #Setting the server address and port
    server_address, server_port = User_Input()

    #Initializing a new socket connection
    my_socket = socket(AF_INET, SOCK_STREAM)
    print("[+] Establishing connection")

    #Connecting the socket to specified host and port
    my_socket.connect((server_address, server_port))
    print("[+] Connection established")

    #Infinite loop for sending messages to server
    while True:
        message = input("[+] Message to send: ")
        #uncomment the below line if you're using ncat/netcat for better
        #terminal readability
        #message = message + "\n"
        my_socket.send(message.encode('utf-8'))

        user_value = Client_Exit()
        if (user_value == 'n'):
            print("[+] Closing transport")
            my_socket.close()
            break
        else:
            continue


try:
    Client_Setup()

except ConnectionRefusedError:
    print("[+] Connection refused")

except TimeoutError:
    print("[+] Connection timeout")

except KeyboardInterrupt:
    print("[+] Closing transport")

except OSError:
    print("[+] Invalid host")
