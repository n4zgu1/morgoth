import threading
import socket
from datetime import datetime
from time import strftime
import os

f = open('LOG.txt', 'a')

def log(string):
    t = datetime.now()
    timestemp = t.strftime("%H:%M:%S")
    f.write(f'{timestemp} {string}\n')

def handle(conn, addr, buffer):
    try:
        data = conn.recv(buffer).decode('utf-8')
        data = data.split('#FNAME#')
        filename = data[0]
        file_data = data[1]
        with open(filename, 'w') as file:
            file.write(file_data)
        size = os.path.getsize(filename)
        log(f'Received file {filename} size {size} bytes')
        data = conn.recv(buffer).decode('utf-8')    
        print(f'X{data}x') 
    except data:
        print('Client left!')
        print(e)

def receive():
    buffer = 1000000000
    host = '0.0.0.0'
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    log('\nstart new session')
    print(host)
    print('Waiting  for connections...')
    while True:
        conn, addr = s.accept()
        print(f'{addr} connected')
        log(f'conection from {addr}')
        thread = threading.Thread(target=handle, args=(conn, addr, buffer))
        thread.start()
try: receive()
except KeyboardInterrupt: exit(00)