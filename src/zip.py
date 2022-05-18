import os
import zipfile

def zipdir(path, zpname):
    try:
        with zipfile.ZipFile(zpname, 'w', zipfile.ZIP_DEFLATED) as ziph:
            #ziph is zipfile handler
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(root, file),
                                            os.path.join(path, '..')))
            ans = 'ZIP CREATED [x]'
            print(ans)
            return ans
    except Exception as e:
        ans = 'ZIP CREATED [ ]'
        print(ans)
        return ans
                

