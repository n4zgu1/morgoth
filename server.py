import threading
import socket
from datetime import datetime
from time import strftime
import os

f = open('LOG.txt', 'a')
folder = 'data/'


def log(string):
    t = datetime.now()
    timestemp = t.strftime("%H:%M:%S")
    if string == 'start new session':
        f.write(f'\n{timestemp} {string}\n')
        return None
    f.write(f'{timestemp} {string}\n')



def handle(conn, addr, buffer):
    try:
        data = conn.recv(buffer).decode('iso-8859-1')   # receive DATA
        data = data.split('#FNAME#')
        filename = data[0]
        file_data = data[1].encode('iso-8859-1')
        with open(f'{folder}{filename}', 'wb') as file:  # write file
            file.write(file_data)
        size = os.path.getsize(filename)
        log(f'Received file {filename} size {size} bytes')
    except Exception as e:
        log(e)


def receive():
    buffer = 1000000000
    host = '0.0.0.0'
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    log('start new session') # write LOG
    print(f'{host}\nWaiting  for connections...')
    while True:
        conn, addr = s.accept() # accept every client
        print(f'{addr} connected')
        log(f'conection from {addr}')
        thread = threading.Thread(target=handle, args=(conn, addr, buffer))
        thread.start()
try: receive()
except KeyboardInterrupt: exit(00)