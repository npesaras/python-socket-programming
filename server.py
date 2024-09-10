import socket
import threading

# Define the host and port
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

DISCONNECT_MESSAGE = "DISCONNECT"
clients = [] # List to store client connections

def handle_client(conn, addr):
    print(f"New Connection {addr} connected.")
    clients.append(conn)  # Add the client to the list

    connected = True
    while connected:
        msg = conn.recv(64).decode("utf-8")  # Receive the message directly
        if msg:
            if msg == DISCONNECT_MESSAGE:
                break  # Disconnect the client
            print(f"Received message from {addr}: {msg}")  # Print the received message
    conn.close()
    clients.remove(conn)  # Remove the client from the list

def start_server():
    server.listen(5) # Max number of connections
    print(f"Server is listening on {SERVER}:{PORT}") # Start listening for incoming connections
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # Create a new thread for each client connection
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}") # Print the number of active connections

print("Starting the server...")
start_server()