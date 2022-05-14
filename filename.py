import os

#checks if filename-file already exists and delete it
if os.path.exists('filenames.txt') == True:
    os.remove('filenames.txt')

def writepath(target, keyfolder, sep):      #write real filenames in 'filenames.txt'
    try:
        for path, dirs, files in os.walk(target):
            with open(f'{keyfolder}/filenames.txt', 'a') as log:
                for file in files:                
                    log.write(f'{path}/{file}{sep}')   #write filename
        ans = 'SAFE PATHS [X]'
        print(ans)
        return ans
    except Exception as e:
        ans = 'SAFE PATHS [ ]'
        print(ans)
        return ans


def encrName(target):       #encrypt filenames in numbers
    count = 0
    try:
        for path, dirs, files in os.walk(target):
            for file in files:
                file_ex = os.path.splitext(file)
                file_ex = file_ex[1]

                targetfile = f'{path}/{file}'    
                newfile = f'{path}/{count}{file_ex}'

                os.rename(targetfile, newfile)
                count += 1
        ans = 'ENCRYPT FILENAMES [X]'
        print(ans)
        return ans
    except Exception as e:
        ans = 'ENCRYPT FILENAMES [ ]'
        print(ans)
        return ans


