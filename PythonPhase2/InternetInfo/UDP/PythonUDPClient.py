import socket  # import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

x = input("Please enter the X coordinate")
y = input("Please enter the y coordinate")
data = str(x) + "," + str(y)

s.sendto(data.encode('utf-8'), ('127.0.0.1', 8888))  # encode() encodes the string into a byte string for transmission

# Receive the coordinate data after the server adds 1:
data2, addr = s.recvfrom(1024)
print("Received coordinate data after server added 1: ", data2.decode('utf-8'))  # decode() decodes

s.close()