import socket

def mpm():
    host = "127.0.0.1"
    port = 6000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    print("Waiting for connection...")
    c,addr = s.accept()
    print("Connection Established with client address {}".format(addr))
    while True:
        try:
            print()
            data = c.recv(1024)
            d = data.decode('ascii')
            print("Client Message : ",d)
            print()
            x = input("Server Message : ")
            y = x.encode('ascii')
            c.send(y)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated")
            break
mpm()
