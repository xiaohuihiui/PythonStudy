
import socket        # import socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.connect(('www.dangdang.com', 80))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.connect(('www.dangdang.com', 80))  # establish a connection with Dangdang.com
s.send(b'GET / HTTP/1.1\r\nHost: www.dangdang.com\r\nConnection: close\r\n\r\n')
# Receiving data:
buffer = []
while True:
    d = s.recv(1024)  # Receive at most 1k bytes of data from the server each time
    if d:  # Is it empty data?
        buffer.append(d)  # Append the byte string to the list
    else:
        break  # Return empty data, indicating that reception is complete, exit the loop

data = b''.join(buffer)
s.close()  # Close the connection
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# Write the received data to a file:
with open('dd.html', 'wb') as f:
    f.write(html)
# establish a connection with Dangdang.com