import socket


ADDRESS = ('localhost', 7777)


def echo_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            msg = input('Ваше сообщение: ')
            if msg == 'exit':
                break
            sock.send(msg).encode('utf-8')



if __name__ == '__main__':
    echo_client()