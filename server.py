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

def handle_client(conn, addr):
    print(f"New Connection {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode("utf-8") 
        if msg == DISCONNECT_MESSAGE:
            connected = False # Disconnect the client
        print(f"Received message from {addr}: {msg}")
    conn.close()


def start_server():
    server.listen(5) # Max number of connections
    print(f"Server is listening on {SERVER}:{PORT}") # Start listening for incoming connections
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")

print("Starting the server...")
start_server()