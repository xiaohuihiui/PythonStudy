import socket
import threading
import time
def tcplink(sock, addr):
    print('Received a connection request from %s:%s' % addr)
    sock.send(b'Welcome!')  # Send "Welcome!" message to the client
    while True:
        data = sock.recv(1024)  # Receive the message sent by the client
        time.sleep(1)  # Delay for 1 second
        if not data or data.decode('utf-8') == 'exit':  # If there is no data or 'exit' message is received
            break  # Terminate the loop
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))  # After receiving the message, add 'Hello' and send it back
    sock.close()  # Close the connection
    print('The connection from %s:%s is closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(5)
print("waiting for connection...")
while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

