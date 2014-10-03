'''
    server
    ~~~~~~

    A non-blocking server purely written using `select` module.
'''

import select
import socket
import time

SERVER_ADDRESS = ('127.0.0.1', 2807)
READ_CHUNK_SIZE = 10

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(SERVER_ADDRESS)
server.listen(5)

read_socks = set([server])
write_socks = set()
x_socks = set()

i = 0
try:
    while True:
        readable, writable, exceptional = select.select(
            read_socks, write_socks, read_socks)
        i += 1
        # print 'Iteration number: %s' % i

        for sock in readable:
            if sock is server:
                conn, _ = server.accept()
                read_socks.add(conn)
            else:
                data = sock.recv(READ_CHUNK_SIZE)
                if data == '':
                    sock.close()
                    try:
                        read_socks.remove(sock)
                    except KeyError:
                        pass
                    try:
                        write_socks.remove(sock)
                    except KeyError:
                        pass
                    try:
                        writable.remove(sock)
                    except ValueError:
                        pass
                else:
                    print '%s Reading: %s' % (sock.getpeername(), data)
                    write_socks.add(sock)

        for sock in writable:
            msg = time.time()
            print '%s Writing: %s' % (sock.getpeername(), msg)
            sock.send('Message: %s' % msg)
            write_socks.remove(sock)

except KeyboardInterrupt:
    server.close()
