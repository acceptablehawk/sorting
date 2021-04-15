import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/IMG'

for file in os.listdir(primarypath):
    if file.endswith('.jpeg') or file.endswith('jpg') or file.endswith('png'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file)
        os.rename(filepath,newname)