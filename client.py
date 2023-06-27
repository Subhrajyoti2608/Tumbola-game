import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image
import PIL.Image
import tkinter as tk

screen_width= None
screen_height= None

SERVER = None
IP_ADDRESS = None
PORT = None

canvas1 = None
playerName = None
nameEntry = None
nameWindow = None

def saveName():
    global SERVER
    global canvas1
    global playerName
    global nameEntry
    global nameWindow

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())


def askPlayerName():
    global canvas1
    global playerName
    global nameEntry
    global nameWindow
    global screen_height
    global screen_width

    nameWindow = Tk()
    nameWindow.title("Tumbola Game")
    nameWindow.attributes('-fullscreen',True)

    screen_height = nameWindow.winfo_screenheight()
    screen_width = nameWindow.winfo_screenwidth()
    image = PIL.Image.open("C:/Users/subhr/Downloads/C204-project-template-main/assets/background.png")
    bg=ImageTk.PhotoImage(image)

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both",expand=True)
    #Display Image
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2, screen_height/5, text="Enter Name", font=("Chalkboard SE",100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')

    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT

    PORT = 5500
    IP_ADDRESS = "127.0.0.1"

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    askPlayerName()

setup()