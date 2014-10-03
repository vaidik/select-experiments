'''
    multiclient
    ~~~~~~~~~~~

    Creates multiple client for testing non-blocking server.
'''

import socket

COUNT = 10
SERVER_ADDRESS = ('127.0.0.1', 2807)

clients = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in xrange(COUNT) ]

for client in clients:
    client.connect(SERVER_ADDRESS)
    client.send('some message')
    print client.recv(100)
    client.close()

# import ipdb; ipdb.set_trace()
