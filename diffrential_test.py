import serial
import time
import socket
#ser = serial.Serial('/dev/ttyACM0', 9600)
#time.sleep(2)

def drive_motors(left_speed, right_speed):
    left_speed = min(127, max(-127, left_speed))
    right_speed = min(127, max(-127, right_speed))
    left_direction = 0b01000000 if left_speed >= 0 else 0b00000000
    right_direction = 0b11000000 if right_speed >= 0 else 0b10000000
    left_speed = abs(left_speed)
    right_speed = abs(right_speed)
    print(left_speed,right_speed)
    command = ([left_direction | left_speed, right_direction | right_speed])
    #ser.write(command)
    print(command)

def stop_motors():
    #ser.write(b'\x00\x00')
    pass


def differential_drive(linear_speed, angular_speed):
    left_speed = linear_speed - angular_speed
    right_speed = linear_speed + angular_speed
    drive_motors(left_speed, right_speed)


IP_ADDRESS = '192.168.50.157'
PORT = 5004

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
        if data==b'fwd':
        	differential_drive(50,0)
        if data==b'bwd':
        	differential_drive(-50,0)
        if data==b'lt':
        	differential_drive(0,50)
        if data==b'rt':
        	differential_drive(0,-50)
        if data==b'stp':
        	differential_drive(0,0)

        # Send a response to the control computer
        response = b'Response from the rover'
        connection.send(response)

    # Close the connection
    connection.close()

# Close the socket
rover_socket.close()







