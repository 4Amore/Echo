import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = 'localhost'
port = 9090

usr_host_name = input('Введите хост :')
usr_port = input('Введите порт :')
if usr_host_name != '': host_name = usr_host_name
if usr_port != '': port = usr_port

sock.bind((host_name, int(port)))
logs = open('log.txt', 'a')
logs.write(f'host: {host_name}\nport: {port}')
logs.write('Сервер запущен ')
def start_server():
    conn, addr = sock.accept()
    logs.write(str(addr) + ' подключился!')
    conn.send('вы подключились к серверу!'.encode('utf-8'))
    data = ''
    while data != 'exit':
        data = conn.recv(1024).decode("utf-8")
        print(f'client: {data}')
        logs.write(f'client: {data}')

while True:
    sock.listen(5)
    start_server()
