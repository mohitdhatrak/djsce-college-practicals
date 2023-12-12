import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = "127.0.0.1"
PORT = 1234

sock.bind((HOST, PORT))
print("Waiting for client...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f'Received message : {data.decode()} from {addr}')
    response = "message received"
    sock.sendto(response.encode(), addr)
    print('server closed')
