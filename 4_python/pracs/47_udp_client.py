import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5000)

while True:
    client_message = input("Client: ")
    c.sendto(bytes(client_message, 'utf-8'), server_address)

    server_message, server_address = c.recvfrom(1024)
    print("Server: ", server_message.decode())

    if not server_message:
        break

c.close()
