import socket
import os

# Server configuration
server_address = ('localhost', 5000)
directory_path = 'C:\\Users\\Kruti Bagwe\\Desktop\\misc\\codes\\python idle\\exp14'  

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections (max backlog of connections set to 5)
server_socket.listen(5)

print("TCP File Search Server is running. Waiting for connections...")

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        # Receive file name from client
        file_name = client_socket.recv(1024).decode().strip()
        print(f"Received file name: {file_name}")

        # Check if the file exists in the specified directory
        file_path = os.path.join(directory_path, file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            # Open and read the file contents
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Send file contents back to the client
            client_socket.sendall(file_contents.encode())
            print("File sent successfully")
        else:
            # Send file not found message to the client
            client_socket.sendall("File not found".encode())
            print("File not found")

    finally:
        # Close the client socket
        client_socket.close()
