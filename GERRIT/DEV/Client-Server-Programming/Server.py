import socket

#Creating socket object

try:
    socket_object = socket.socket()
except socket.error as sock_err:
    print("Error in socket :", sock.err)

port = 19898

#Server do not need 'connect' method because it need not connect to client instead it should bind to incoming port

socket_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_object.bind(('', port))
print("Socket binded to port :", port)

socket_object.listen(1)

while True:
    c,addr = socket_object.accept()
    print("Got addr from :", addr)
    c.sendall(b'Cool buddy!!!!')
    c.close()
