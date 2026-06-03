import socket
import threading
import queue

HOST = "127.0.0.1"
PORT = 5000

event_queue = queue.Queue()

clients = {}
tasks = []
next_task_id = 1

clients_lock = threading.Lock()
tasks_lock = threading.Lock()


class Client:
    def __init__(self, sock, address, name):
        self.sock = sock
        self.address = address
        self.name = name
        self.file = sock.makefile("r", encoding="utf-8")


def send_line(client, text):
    try:
        client.sock.sendall((text + "\n").encode("utf-8"))
    except:
        pass


def broadcast(text, except_client=None):
    with clients_lock:
        for client in list(clients.values()):
            if client != except_client:
                send_line(client, text)


def handle_client(client):
    send_line(client, f"Вітаємо! Ваше ім'я: {client.name}")
    send_line(client, "Команди: /nick, /who, /add, /list, /done, /delete, /my, /msg, /quit")

    try:
        for line in client.file:
            line = line.rstrip("\n")
            event_queue.put(("message", client, line))
    except:
        pass
    finally:
        event_queue.put(("disconnect", client, None))


def event_processor():
    global next_task_id

    while True:
        event_type, client, text = event_queue.get()

        if event_type == "disconnect":
            with clients_lock:
                if client.name in clients:
                    del clients[client.name]
                    broadcast(f"[SERVER] {client.name} відключився")
            continue

        if not text:
            send_line(client, "Помилка: порожнє повідомлення")
            continue

        if text == "/quit":
            send_line(client, "Сесію завершено. До побачення!")
            try:
                client.sock.close()
            except:
                pass
            continue

        if not text.startswith("/"):
            broadcast(f"[{client.name}] {text}")
            continue

        parts = text.split(" ", 2)
        command = parts[0]

        if command == "/nick":
            if len(parts) < 2 or not parts[1].strip():
                send_line(client, "Помилка: використання /nick <name>")
                continue

            new_name = parts[1].strip()

            with clients_lock:
                if new_name in clients:
                    send_line(client, "Помилка: таке ім'я вже зайняте")
                    continue

                old_name = client.name
                del clients[old_name]
                client.name = new_name
                clients[new_name] = client

            broadcast(f"[SERVER] {old_name} змінив ім'я на {new_name}")
            send_line(client, f"Ваше нове ім'я: {new_name}")

        elif command == "/who":
            with clients_lock:
                names = ", ".join(clients.keys())
            send_line(client, f"Користувачі онлайн: {names}")

        elif command == "/add":
            if len(parts) < 2 or not parts[1].strip():
                send_line(client, "Помилка: використання /add <text>")
                continue

            task_text = text[len("/add "):].strip()

            with tasks_lock:
                task = {
                    "id": next_task_id,
                    "author": client.name,
                    "text": task_text,
                    "status": "OPEN"
                }
                tasks.append(task)
                created_id = next_task_id
                next_task_id += 1

            send_line(client, f"Завдання створено. ID = {created_id}")
            broadcast(f"[TASK] {client.name} додав завдання #{created_id}: {task_text}", except_client=client)

        elif command == "/list":
            with tasks_lock:
                if not tasks:
                    send_line(client, "Список завдань порожній")
                else:
                    send_line(client, "Список завдань:")
                    for task in tasks:
                        send_line(
                            client,
                            f"#{task['id']} | {task['author']} | {task['status']} | {task['text']}"
                        )

        elif command == "/my":
            with tasks_lock:
                my_tasks = [task for task in tasks if task["author"] == client.name]

            if not my_tasks:
                send_line(client, "У вас немає завдань")
            else:
                send_line(client, "Ваші завдання:")
                for task in my_tasks:
                    send_line(
                        client,
                        f"#{task['id']} | {task['status']} | {task['text']}"
                    )

        elif command == "/done":
            if len(parts) < 2:
                send_line(client, "Помилка: використання /done <id>")
                continue

            try:
                task_id = int(parts[1])
            except:
                send_line(client, "Помилка: id має бути числом")
                continue

            found = False

            with tasks_lock:
                for task in tasks:
                    if task["id"] == task_id:
                        task["status"] = "DONE"
                        found = True
                        break

            if found:
                broadcast(f"[TASK] Завдання #{task_id} виконано")
            else:
                send_line(client, "Помилка: завдання не знайдено")

        elif command == "/delete":
            if len(parts) < 2:
                send_line(client, "Помилка: використання /delete <id>")
                continue

            try:
                task_id = int(parts[1])
            except:
                send_line(client, "Помилка: id має бути числом")
                continue

            deleted = False

            with tasks_lock:
                for task in tasks:
                    if task["id"] == task_id:
                        tasks.remove(task)
                        deleted = True
                        break

            if deleted:
                broadcast(f"[TASK] Завдання #{task_id} видалено")
            else:
                send_line(client, "Помилка: завдання не знайдено")

        elif command == "/msg":
            msg_parts = text.split(" ", 2)

            if len(msg_parts) < 3:
                send_line(client, "Помилка: використання /msg <name> <text>")
                continue

            target_name = msg_parts[1]
            private_text = msg_parts[2]

            with clients_lock:
                target = clients.get(target_name)

            if target is None:
                send_line(client, "Помилка: користувача не знайдено")
            else:
                send_line(target, f"[PRIVATE від {client.name}] {private_text}")
                send_line(client, f"[PRIVATE до {target_name}] {private_text}")

        else:
            send_line(client, "Помилка: невідома команда")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Сервер запущено на {HOST}:{PORT}")

    processor_thread = threading.Thread(target=event_processor, daemon=True)
    processor_thread.start()

    counter = 1

    while True:
        client_sock, address = server.accept()

        name = f"user{counter}"
        counter += 1

        client = Client(client_sock, address, name)

        with clients_lock:
            clients[name] = client

        broadcast(f"[SERVER] {name} підключився")

        thread = threading.Thread(target=handle_client, args=(client,), daemon=True)
        thread.start()


if __name__ == "__main__":
    main()