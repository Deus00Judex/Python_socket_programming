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
    try:
        client.connect(addr)
        return True
    except ConnectionError:
        print(f"There is a connection-Problem with {SERVER}")
        return False


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
    except Exception as exeption:
        print("Something went wrong while sending your message!")
        print(exeption)


def main():
    if not connect(addr):
        print("ERROR")
    else:
        msg = ""
        while msg != DISCONNECT_MESSAGE:
            msg = input(str)
            send(msg)


main()
#Test