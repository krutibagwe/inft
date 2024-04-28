import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 5000))

print("UDP Server is running")

while True:
    data, client_address = s.recvfrom(1024)
    print("Client: ", data.decode())

    if not data:
        break

    server_message = input("Server: ")
    s.sendto(bytes(server_message, 'utf-8'), client_address)

s.close()
       
