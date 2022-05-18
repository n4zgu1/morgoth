import socket
import os
# VERSCHLÜSSELN

def upload(HOST, PORT, keyfile):
    try:
        print(f'connecting to {HOST}')
        dec = 'iso-8859-1'
        buffer = 1000000000
        filename = keyfile
        size = os.path.getsize(keyfile)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            file = open(filename , 'rb')
            file_data = file.read(buffer)
            filename = f'{filename}#FNAME#'
            s.send(filename.encode(dec))
            s.sendall(file_data)
            data = s.recv(buffer).decode(dec)
            print(data)
            if data != f'size:{size}':
                print('some error happened')
                return False
            return True
    except Exception as e: print(e); return False
