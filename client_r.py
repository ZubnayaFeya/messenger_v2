import socket
# from type_msg import *
import jim


ADDRESS = ('localhost', 7777)


def echo_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            data = jim.f_decode(sock.recv(1024))
            print('Нам пришло сообщение: ', data)


if __name__ == '__main__':
    echo_client()