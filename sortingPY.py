import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/PY'

for file in os.listdir(primarypath):
    if file.endswith('.py'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file)
        os.rename(filepath,newname)