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
      __  ___ ___  _   _  ___ ___
    /' _/| __| _ \| \ / || __| _ \ \t
    `._`.| _|| v /`\ V /'| _|| v /
    |___/|___|_|_\  \_/  |___|_|_\   Version 1.0
    """)


#Function: Asking user for server setup
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


#Function: To setup and communicate with the client
def Server_Setup():

    #Printing the banner
    Banner()

    #Setting server address and port
    server_address, server_port = User_Input()

    #Initializing a new socket connection
    my_socket = socket(AF_INET, SOCK_STREAM)

    #Setting socket for reuse
    my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    #Binding the new socket to specified host and port
    my_socket.bind((server_address, server_port))

    #Listening for number of connections simultaneously
    my_socket.listen(3)
    print("[+] Server started! Waiting for connections...")

    #Accepting the connection from client
    connection, address = my_socket.accept()
    print("[+] Client connected with address: ", address)

    #Infinite loop for receiving messages from client
    while True:
        # 1024 is the buffer size
        data = connection.recv(1024)
        if not data:
            print("[+] Closing transport")
            break
        else:
            print("[+] Client:", data.decode('utf-8'))

    connection.close()


try:
    Server_Setup()

except KeyboardInterrupt:
    print("[+] Closing transport")

except OSError:
    print("[+] Invalid host")
