import socket

# Define IP address and port number
IP_ADDRESS = '192.168.50.157'
PORT = 5000

# Create a socket object
control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the rover computer
control_socket.connect((IP_ADDRESS, PORT))

while True:
    # Send data to the rover computer
    message = input("Enter a message to send: ")
    control_socket.send(message.encode())

    # Receive data from the rover computer
    data = control_socket.recv(1024)

    # Process the received data
    print("Received data:", data.decode())

# Close the socket
control_socket.close()

