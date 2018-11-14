#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
#from str import join

name_1 = {}
def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Now type your name and press enter! This will be user username", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    print(name,client)	
    name_1[name] = client	
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
#    if(!bool(clients)){}
    present = ''
    for c in clients:
        present = present + clients[c] +", "
    present  = present + " are online"	
    client.send(bytes(present, "utf8"))
				
    msg = "%s has joined the chat!" % name
    broadcast_1(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast_1(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast_1(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    mssg=str(msg)
    mssg = mssg.split()
    prefix_1 = prefix
    name_22 = mssg[-1][:-1]
    print("anynonoymous",name_22[-3:])
    if(name_22[-3:] == "@ay"):
        own_r = prefix
        prefix = "anonymous : "	
        name_22 = name_22[:-3]
#    msg_d = mssg[:-1]
#    print(msg_d)  
    result=''
    ln=len(mssg)
    for x in range(0,ln-1):
        result=result+mssg[x]+' '

	
    print("prefix",prefix)	
    msg = bytes(result[2:], "utf8")		
# own
    own = prefix[:-2]
    print("own",own)
    
    if(prefix == "anonymous : "):
   	     own = own_r[:-2]
    print("again prefix",prefix)
    for a in clients:
        if(clients[a] == own):
            if(prefix == "anonymous : "):
                own = own +"*: "
            else:
                own = own +": "      
            a.send(bytes(own[:-2] + "-> "+ name_22 + ": ", "utf8")+msg)
    print("name given",name_22)
    print("message",result)
    for a in clients:
    	if(clients[a] == name_22):
	        a.send(bytes(prefix, "utf8")+msg)
#	for a in clients:
#    	if(clients[a] == prefix[-2]):
#	        a.send(bytes(prefix, "utf8")+msg) 
			
			
			
 #   mssg=str(msg)
 #   mssg = mssg.split()
 #   name_22 = mssg[-1][:-1]
 #   print("name given",name_22)	
 #   print(name_1[name_22])		
 #   name_1[name_22].send(bytes(prefix, "utf8")+msg)
#    for sock in clients:
#       sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
