import socket
import time
import os
from pathlib import Path

message = "Hello World"
response = "I got it, roger"

configfile = open("/etc/configs/config.file", "r")

average_values = configfile.read()

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    data = ""
    client_socket.send(message.encode())  # send message
    while True:
        data = client_socket.recv(1024).decode()  # receive response
        if data == response:
            time.sleep(average_values)
            client_socket.send(message.encode())
        #print('Received from server: ' + data)  # show in terminal

    client_socket.close()  # close the connection


if __name__ == '__main__':

    client_program()