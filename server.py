import socket
import select
import json
import sqlalchemy
import threading  #Thread

import jim
import type_msg


class CServ():
    def __init__(self, queue=25, timeout=0.2):
        self.sock = None
        self.args = jim.f_parser()
        self.timeout = timeout
        self.queue = queue

    def soc_serv(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.args.address, int(self.args.port)))
        sock.listen(self.queue)
        sock.settimeout(self.timeout)
        self.sock = sock

    def read_requests(self, r_clients, all_clients):
        responses = {}	#Словарь ответов сервера вида{сокет: запрос}
        for sock in r_clients:
            try:
                data = jim.f_decode(self.sock.recv(1024))
                responses[sock] = data
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)
        return responses

    def write_responses(self, requests, w_clients, all_clients):
        for sock in w_clients:
            for s, message in requests.items():
                try:
                    resp = requests[sock].encode('utf-8')
                    test_len = sock.send(resp.upper())
                except:
                    print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                    sock.close()
                    all_clients.remove(sock)

    def mainloop(self):
        clients = []
        #clients_dict = {}
        while True:
            try:
                conn, addr = self.sock.accept()
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

                requests = self.read_requests(r, clients)
                self.write_responses(requests, w, clients)






servak = CServ()
print('Эхо-сервер запущен!')
mainloop()
