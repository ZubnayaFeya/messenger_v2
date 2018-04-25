from subprocess import Popen, CREATE_NEW_CONSOLE
import sys




client1 = sys.argv[1]
client2 = sys.argv[2]
Popen('python3 {}'.format(client1), creationflags=CREATE_NEW_CONSOLE)
Popen('python3 {}'.format(client2), creationflags=CREATE_NEW_CONSOLE)
