from tkinter import *
import webbrowser
import socket
import serial
import time

IP_ADDRESS = '192.168.50.157'
PORT = 5005

control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

control_socket.connect((IP_ADDRESS, PORT))


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

root = Tk()

new=1

e = Entry(root,width=35,borderwidth=5)
e.grid(row=4,column=1,columnspan=3,padx=30)


url = "http://{}:8080/" #Replace with the ip of stream


def openweb():
    ip = e.get()
    url = f"http://{ip}:8080/" 
    url = url.format(ip)
    webbrowser.open(url,new=new)

Button_stream = Button(root, text = "Stream Cam",padx=10,pady=10,command=openweb)
Button_stream.grid(row=5,column=2)


ip_add = Label(root,text ="Enter the ip adress").grid(row=3,column=1,columnspan=3,pady=30)


button_forward  = Button(root , text="forward",padx=20,pady=20,command=move_forward)
button_forward.grid(row=0,column=2)

button_backward  = Button(root , text="backward",padx=20,pady=20,command=move_backward)
button_backward.grid(row=2,column=2)

button_right  = Button(root , text="left",padx=22,pady=20,command=turn_left)
button_right.grid(row=1,column=1)

button_left  = Button(root , text="right",padx=20,pady=20,command=turn_right)
button_left.grid(row=1,column=3)

button_stop  = Button(root , text="stop",padx=20,pady=20,command=stop)
button_stop.grid(row=1,column=2)

root.mainloop()
