import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    message = "Hello"
    client_socket.connect((HOST, PORT))
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024)

    print(f'response from server : {response.decode()}')
    print('client closed')
