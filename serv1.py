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


servak = CServ()
print('Эхо-сервер запущен!')
mainloop()