import socket

# Server address and port
server_address = ('localhost', 5000)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(server_address)

    # Get file name from user input
    file_name = input("Enter file name to search at server: ")

    # Send file name to the server
    client_socket.sendall(file_name.encode())

    # Receive response from server
    response = client_socket.recv(1024).decode()
    print("Server response:", response)

    if response != "File not found":
        # If file found, print the file contents
        print("File contents:")
        print(response)

finally:
    # Close the socket
    client_socket.close()
