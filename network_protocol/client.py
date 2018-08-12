import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',2224))
# while True:
msg = "close"
# print(msg)
sock.send("hi".encode())
sock.send(msg.encode())
recv = sock.recv(1024)
print(recv.decode())
    # if recv == 'close':
    # break
sock.close()