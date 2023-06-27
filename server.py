import socket
from threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

CLIENTS = {}

def acceptConnections():
    global SERVER
    global CLIENTS

    while True:
        player_socket, addr = SERVER.accept()
        playername = player_socket.recv(1024).decode().strip()
        if len(CLIENTS.keys())==0:
            CLIENTS[playername] = {"player_type":"player1"}

        else:
            CLIENTS[playername] ={"player_type":"player2"}

        CLIENTS[playername]["player_socket"]=player_socket
        CLIENTS[playername]["address"]=addr
        CLIENTS[playername]["player_name"]= playername
        CLIENTS[playername]["turn"] = False

        print(f"Connection established with {playername}:{addr}")

        
def setup():
    print("\n")
    print("\t\t\t\t\t\t*** TUMBOLA GAME ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()

setup()