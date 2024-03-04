import socket
print("starting a new client : client 1")

HOST = "localhost"
PORT = 3000 # this is the port for the server to connect

client_socket = socket.socket()

# three way handshake
client_socket.connect((HOST,PORT)) #clients need to connect to server side

client_socket.sendall(b"Hello from the client1")

response_from_server = client_socket.recv(2048) 
print(response_from_server)

