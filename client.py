import socket
import threading

# Define the host and port
PORT = 9999
server_ip = input(format("Server IP: ")) # Replace with your server IP

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Try to connect to the server
try:
    client.connect((server_ip, PORT))
    print(f"Socket bound to {server_ip}:{PORT}")
except socket.error as e:
    print(f"Error binding socket: {str(e)}")
    exit()

def send(msg):
    msg = msg.encode('utf-8')
    msg_length = len(msg)
    send_length = str(msg_length).encode('utf-8') # Convert the length to bytes
    client.send(send_length)
    client.send(msg)

send("Hello, server!")
send("Bye, server!")

# Close the socket
client.close()

print("Connection is terminated")

