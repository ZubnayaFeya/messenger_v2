import socket
import json
import argparse
#from time import ctime
from type_msg import *
import jim
from threading import Thread


class CClient():

    def __init__(self, name):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name

    def mainloop(self):
        with self.sock.connect(('localhost', 7777)):
            jim.f_send_message(self.sock, f_presence(self.name))

            while 1:
                tr_send = Thread(target=self.recv_data())

    def recv_data(self):
        result = self.sock.recv(1024)
        data = jim.f_encode(result)
        print(data)



cli = CClient('Danila')

res = cli.recv_data()
print(cli.prepare_resalt(res))

