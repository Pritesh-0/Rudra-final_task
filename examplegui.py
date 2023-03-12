import socket
import tkinter as tk
import serial
import time

IP_ADDRESS = '192.168.50.157'
PORT = 5004

control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

control_socket.connect((IP_ADDRESS, PORT))

#ser = serial.Serial('/dev/ttyACM0', 9600)
#time.sleep(2)

window = tk.Tk()
window.title('Differential Drive Control')

def move_forward():
	message='fwd'
	control_socket.send(message.encode())

def move_backward():
	message='bwd'
	control_socket.send(message.encode())

def turn_left():
	message='lt'
	control_socket.send(message.encode())

def turn_right():
	message='rt'
	control_socket.send(message.encode())

def stop():
	message='stp'
	control_socket.send(message.encode())


forward_button = tk.Button(window, text='Move Forward', command=move_forward)
backward_button = tk.Button(window, text='Move Backward', command=move_backward)
left_button = tk.Button(window, text='Turn Left', command=turn_left)
right_button = tk.Button(window, text='Turn Right', command=turn_right)
stop_button = tk.Button(window, text='Stop', command=stop)


forward_button.pack()
backward_button.pack()
left_button.pack()
right_button.pack()
stop_button.pack()


window.mainloop()

