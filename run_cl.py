# coding: utf8
#! /usr/bin/python3
from subprocess import Popen
import sys
import os


files = ['client_w.py', 'client_r.py']

for i in files:
    if os.name == 'nt':
        p = Popen("python3 client.py", shell=True)
    elif os.name == 'posix':
        p = Popen("x-terminal-emulator -e python3 {}".format(i), shell=True)

# client1 = sys.argv[1]
# client2 = sys.argv[2]
# p = Popen("x-terminal-emulator -e python3 client.py", shell=True)
# Popen('python3 {}'.format(client2))

