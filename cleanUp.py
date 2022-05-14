import os

def clean(path):
    #walk trough every file
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file = os.path.join(root, name)
            #removing file
            os.remove(file)
        for name in dirs:
            folder = os.path.join(root, name)
            #removing folder
            os.rmdir(folder)
    try:
        os.rmdir(path)
        ans = "REMOVED KEYFILES [x]"
        print(ans)
        return ans
    except:
        ans = "REMOVED KEYFILES [ ]"
        print(ans)
        return ans
