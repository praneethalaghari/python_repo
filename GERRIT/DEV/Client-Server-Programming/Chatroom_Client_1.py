import socket

socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

My_name = 'Thanmai Mendu'

port = 12345

ip_address = socket.gethostbyname('localhost')

socket_object.connect((ip_address, port))

while True:
    data_to_send = input(My_name + " :")
    socket_object.sendall(data_to_send.encode('UTF-8'))
    if str(data_to_send) == 'ciao':
        socket_object.close()
        break

    data_received = socket_object.recv(1024)
    if data_received == 'ciao':
        socket_object.close()
        break
    print("Praneeth Alaghari :", data_received.decode('UTF-8'))


print("Session Ended")