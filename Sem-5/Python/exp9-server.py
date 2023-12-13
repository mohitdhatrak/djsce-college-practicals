import socket


def mpm_server():
    host = "127.0.0.1"
    port = 6000
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("Waiting for connection...")
    c, addr = s.accept()
    print("Connection Established!")
    print("Client Address:", addr)

    while True:
        try:
            print()
            data = c.recv(1024)
            d = data.decode("ascii")
            print("Client:", d)
            print()
            if d == "Connection from Client terminated!":
                print("Connection terminated, server no more listening!")
                break
            x = input("Enter New Message: ")
            y = x.encode("ascii")
            c.send(y)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            break

    c.close()


mpm_server()
