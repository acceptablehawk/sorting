import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/PDF'


for file in os.listdir(primarypath):
    if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.doc'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file)
        os.rename(filepath,newname)