'''
    client
    ~~~~~~

    Simple client for testing non-blocking server.
'''

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2807))
client.send('some message')
print client.recv(100)
client.close()
# import ipdb; ipdb.set_trace()
