import socket
import select
import json
import sqlalchemy

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

    def mainloop(self):
        clients = []
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


servak = CServ()
print('Эхо-сервер запущен!')
mainloop()