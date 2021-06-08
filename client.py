import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ACKNOWLEDGEMENT_OF_RECEIPT_MESSAGE = "Msg received"
SERVER = "192.168.188.39"
addr = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(addr):
    client.connect(addr)


def send(msg):
    try:
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        response = client.recv(2048).decode(FORMAT)
        print(response)
    except Exception:
        print("Something went wrong!")


def main():
    connect(addr)
    msg = ""
    while msg != DISCONNECT_MESSAGE:
        msg = input(str)
        send(msg)

main()
