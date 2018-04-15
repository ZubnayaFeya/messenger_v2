import argparse
import json
import sys


def f_sys_args():
    port = sys.argv[1]
    addr = sys.argv[2]
    return port, addr

def f_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='7777')
    parser.add_argument('-a', '--address', default='127.0.0.1')
    return parser.parse_args()

def f_decode(encodet_data):
    bjmessage = encodet_data
    jmessage = bjmessage.decode('utf-8')
    message = json.loads(jmessage)
    return message

def f_encode(decodet_data):
    message = decodet_data
    jmessage = json.dumps(message)
    bjmessage = jmessage.encode('utf-8')
    return bjmessage

def f_check_message():
    pass

### Client function:

def f_send_message(sock, message):
    sock.send(f_encode(message))