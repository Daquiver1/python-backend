import socket
import threading 

# Port and Ip address we'll run the server on.
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # Gets my ip address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# A socket to open this device to other connections

# created socket and type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT) # Blocking line of code
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f"[{addr}] {msg}")
			conn.send("Message received".encode(FORMAT))

	conn.close()



def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		# When a new connection occurs, give it to handle client with the connection and address.
		conn, addr = server.accept() # blocking line of code
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
	


print("[STARTING] server is starting...")
start()