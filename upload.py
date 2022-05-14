import socket

# VERSCHLÜSSELN

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9999  # The port used by the server
buffer = 1000000000
filename = 'test.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    file = open(filename , 'rb')
    file_data = file.read(buffer)
    filename = f'{filename}#FNAME#'
    s.send(filename.encode('utf-8'))
    s.sendall(file_data)
    s.close()