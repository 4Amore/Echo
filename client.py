import socket

sock = socket.socket()
host_name = 'localhost'
port = 9090

usr_host_name = input('Введите хост :')
usr_port = input('Введите порт :')
if usr_host_name: host_name = usr_host_name
if usr_port: port = usr_port
sock.connect(((host_name, int(port))))
m = sock.recv(1024).decode('utf-8')
print(m)

while m != 'exit':
    m = input('Введите сообщение :')
    sock.send(bytes(m, encoding = 'utf-8'))
sock.close()