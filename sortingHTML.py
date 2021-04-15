import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/HTML'

for file in os.listdir(primarypath):
    if file.endswith('.html'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file)
        os.rename(filepath,newname)