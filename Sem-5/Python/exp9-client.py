import socket


def mpm_client():
    host = "127.0.0.1"
    port = 6000
    s = socket.socket()
    s.connect((host, port))
    print("Connection Established!")

    while True:
        try:
            print()
            x = input("Enter New Message: ")
            y = x.encode("ascii")
            s.send(y)
            print()
            data = s.recv(1024)
            d = data.decode("ascii")
            print("Server:", d)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            s.send("Connection from Client terminated!".encode("ascii"))
            break

    s.close()


mpm_client()
