from socket import *

socket_obj = socket(AF_INET, SOCK_STREAM)

My_name = 'Praneeth Alaghari'
port = 12345

socket_obj.bind(('', port))
socket_obj.listen(10)
socket_obj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

conn, addr = socket_obj.accept()

while True:
    data_recieved = (conn.recv(1024)).decode('UTF-8')
    if data_recieved == "ciao":
        conn.close()
        break
    print("Message from ", addr , data_recieved)
    data_to_send = input(My_name + " :")
    conn.sendall(data_to_send.encode('UTF-8'))
    if data_to_send == 'ciao':
        conn.close()
        break


print("Session Ended")