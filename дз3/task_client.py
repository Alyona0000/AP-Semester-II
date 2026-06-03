import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    file = sock.makefile("r", encoding="utf-8")

    try:
        for line in file:
            print(line.rstrip("\n"))
    except:
        pass

    print("З'єднання з сервером закрито")
    sys.exit()


def send_messages(sock):
    while True:
        try:
            text = input()
            sock.sendall((text + "\n").encode("utf-8"))

            if text == "/quit":
                break
        except:
            break

    try:
        sock.close()
    except:
        pass


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    print("Підключено до сервера")
    print("Введіть команду або повідомлення:")

    receive_thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    send_thread = threading.Thread(target=send_messages, args=(sock,))

    receive_thread.start()
    send_thread.start()

    send_thread.join()


if __name__ == "__main__":
    main()
