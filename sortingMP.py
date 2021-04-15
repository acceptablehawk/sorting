import os
import filetype

primarypath = 'D:/Downloads'
transpath = 'D:/Downloads/MP'

for file in os.listdir(primarypath):
    if file.endswith('.mp4') or file.endswith('.mp3') or file.endswith('.mov') or file.endswith('.lvix') or file.endswith('.MP4') or file.endswith('.MOV'):
        filepath = os.path.join(primarypath, file)
        newname = transpath + '/' + str(file)
        os.rename(filepath,newname)