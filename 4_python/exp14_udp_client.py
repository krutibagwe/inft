import socket

# Create a UDP socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 5000)

print("UDP Client is running. Type messages to send to the server.")

while True:
    # Get message from client and send to server
    client_message = input("Client: ")
    c.sendto(client_message.encode(), server_address)

    # Receive response from server
    data, server_addr = c.recvfrom(1024)
    print(f"Received message from server: {data.decode()}")
