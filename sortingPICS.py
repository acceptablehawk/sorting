import os

path = 'D:/Downloads/RIN'
counter = 0

for file in os.listdir(path):
        filepath = os.path.join(path, file)
        newname = path + '/' +str(counter) + '.png'
        os.rename(filepath,newname)
        counter += 1
