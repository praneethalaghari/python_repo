from socket import *
import sys

socket_obj = socket(AF_INET, SOCK_STREAM)

My_name = 'Praneeth Alaghari'
port = 12345

socket_obj.bind(('', port))
socket_obj.listen(10)
socket_obj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

list_of_connections = []

while True:
    conn, addr = socket_obj.accept()

    list_of_connections.append(conn)
    print(list_of_connections)
    print(addr)

print("Session Ended")