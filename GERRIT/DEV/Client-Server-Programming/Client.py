import socket

socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 19898


host_ip = socket.gethostbyname('localhost')
socket_obj.connect((host_ip,port))

recv = socket_obj.recv(1024)
print(recv.decode('utf8'))

#socket_obj.close()
