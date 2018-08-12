import socket
from threading import Thread

def server(conn, args):
    while True:
        msg = conn.recv(1024)
        if msg.decode() == 'close':
            break
        conn.send(msg)
    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',2224))
s.listen(10)
while True:
    conn, addr = s.accept()
    # print('New connection:', addr)
    thread = Thread(target=server, args=(conn, addr))
    thread.start()

