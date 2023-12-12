import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = "127.0.0.1"
PORT = 1234

msg = "Hello"
sock.sendto(msg.encode(), (HOST, PORT))

response, addr = sock.recvfrom(1024)

print(f'response from server : {response.decode()}')
print('Client closed')
