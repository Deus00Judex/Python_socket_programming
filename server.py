import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ACKNOWLEDGEMENT_OF_RECEIPT_MESSAGE = "Msg received"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    # Logging
    with open("logs.txt", "a") as f:
        f.write(f"[NEW CONNECTION] {addr} connected.\n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "":
                conn.send(ACKNOWLEDGEMENT_OF_RECEIPT_MESSAGE.encode(FORMAT))
                continue
            else:
                print(f"[{addr}] {msg}")
                # Logging
                with open("logs.txt", "a") as f:
                    f.write(f"[{addr}]: '{msg}'\n")

            conn.send(ACKNOWLEDGEMENT_OF_RECEIPT_MESSAGE.encode(FORMAT))

    print(f"[DISCONNECTING {addr}]\n")
    with open("logs.txt", "a") as f:
        f.write(f"[DISCONNECTING {addr}]\n")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #Logging
    with open("logs.txt", "a") as f:
        f.write(f"[LISTENING] Server is listening on {SERVER}\n")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
#Logging
with open("logs.txt", "a") as f:
    f.write("[STARTING] server is starting...\n")
start()