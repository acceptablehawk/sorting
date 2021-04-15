import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/ZIPS&RARS'

for file in os.listdir(primarypath):
    if file.endswith('.zip'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file) + '.zip'
        os.rename(filepath,newname)