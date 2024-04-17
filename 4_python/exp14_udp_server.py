import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to localhost and port 5000
s.bind(('localhost', 5000))

print("UDP Server is running. Type messages to send to the client.")

while True:
    # Receive message from client
    data, client_addr = s.recvfrom(1024)
    print(f"Received message from {client_addr}: {data.decode()}")

    # Get message from server and send to client
    server_message = input("Server: ")
    s.sendto(server_message.encode(), client_addr)
