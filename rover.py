import socket

# Define IP address and port number
IP_ADDRESS = '192.168.50.157'
PORT = 5005

# Create a socket object
rover_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port number
rover_socket.bind((IP_ADDRESS, PORT))

# Listen for incoming connections
rover_socket.listen()

while True:
    # Accept incoming connection requests
    connection, address = rover_socket.accept()

    while True:
        # Receive data from the control computer
        data = connection.recv(1024)

        if not data:
            # If no data is received, break the loop
            break

        # Process the received data
        print("Received data:", data)

        # Send a response to the control computer
        response = b'Response from the rover'
        connection.send(response)

    # Close the connection
    connection.close()

# Close the socket
rover_socket.close()

