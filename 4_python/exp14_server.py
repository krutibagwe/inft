import socket

s = socket.socket()
s.bind(('localhost', 5000))

s.listen(3)
print ("waiting for connection")

while True:
    c, addr = s.accept()
    print("Client connected", addr)

    c.send(bytes("Welcome", 'utf-8'))

    c.close()
