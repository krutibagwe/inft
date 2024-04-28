import socket

c = socket.socket()

c.connect(('localhost', 5000))

while True:
    # Receive message from server
    server_message = c.recv(1024).decode()
    print("Server:", server_message)
    
    # Break loop if server sends an empty message (indicating end of conversation)
    if not server_message:
        break
    
    # Get message from client and send to server
    client_message = input("Client: ")
    c.send(bytes(client_message, 'utf-8'))

c.close()
