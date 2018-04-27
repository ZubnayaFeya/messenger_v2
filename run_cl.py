# coding: utf8
#! /usr/bin/python3
from subprocess import Popen
import sys
import os


path = os.getcwd()
#client1 = sys.argv[1]
#client2 = sys.argv[2]
p = Popen("{}/client.py".format(path))
#Popen('python3 {}'.format(client2))

