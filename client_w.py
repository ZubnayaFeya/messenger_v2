import socket
from type_msg import *
import jim


ADDRESS = ('localhost', 7777)


def echo_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            name = input('Ваше имя или exit: ')
            if name == 'exit':
                break
            msg = jim.f_encode(f_presence(name))
            sock.send(msg)



if __name__ == '__main__':
    echo_client()