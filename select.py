import socket
import select


def read_requests(r_clients, all_clients):
    responses = {}  # Словарь ответов сервера вида{сокет: запрос}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        for s, message in requests.items():
            try:
                resp = requests[sock].encode('utf-8')
                test_len = sock.send(resp.upper())
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def mainloop():
    ADDRESS = ('', 7777)
    clients = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDRESS)
    s.listen(10)
    s.timeout(0.2)
    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
                print(w, r)
            except:
                pass

            requests = read_requests(r, clients)
            write_responses(requests, w, clients)


print('Эхо-сервер запущен!')
mainloop()