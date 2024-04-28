import socket

s = socket.socket()
s.bind(('localhost', 5000))

s.listen(3)
print("Waiting for connection...")

while True:
    c, addr = s.accept()
    print("Client connected", addr)
    
    while True:
        # Get message from server and send to client
        server_message = input("Server: ")
        c.send(bytes(server_message, 'utf-8'))
        
        # Break loop if server sends an empty message (indicating end of conversation)
        if not server_message:
            break
        
        # Receive message from client
        client_message = c.recv(1024).decode()
        print("Client:", client_message)
        
        # Break loop if client sends an empty message (indicating end of conversation)
        if not client_message:
            break

    c.close()
