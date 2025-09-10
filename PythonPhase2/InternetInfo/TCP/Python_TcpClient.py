import socket  # import socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8888))  # establish connection

# print the received welcome message:
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)  # The client program sends name data to the server
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()