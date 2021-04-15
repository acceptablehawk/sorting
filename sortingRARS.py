import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/ZIPS&RARS'

for file in os.listdir(primarypath):
    if file.endswith('.rar'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file) + '.rar'
        os.rename(filepath,newname)