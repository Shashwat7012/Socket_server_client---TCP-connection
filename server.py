# tcp connection

import socket
# for multithreading
import threading

def connect_a_client(conn,addr):
  print("New client connected")
  data = conn.recv(2048)
  print("data recieved from client is:", data)
  conn.sendall(b"Server has recieved your data")

HOST = "localhost"

PORT = 3000

#  created a new socket object
server_socket = socket.socket()

# bind the socket object to host and port

server_socket.bind((HOST, PORT))

# start listening to connections
server_socket.listen()

print("server is lisrening on ", HOST,PORT)

# wait for new connections acceptence
while True:
  conn, addr =  server_socket.accept() # accepting a new connections
#   create a new thread
  t = threading.Thread(target=connect_a_client, args=(conn,addr)) # preparing the thread
  t.start() #it is running the thread

