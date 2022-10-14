import socket

message = "Hello World"
response = "I got it, roger"

def server_program():

    # get the hostname
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  
    server_socket.bind((host, port)) 

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    #print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        if str(data) == message:
            conn.send(response.encode())  
    conn.close() 


if __name__ == '__main__':
    server_program()