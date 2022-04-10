import os
from os import listdir
from os.path import isfile, join
mypath = "c:/Users/radan/Desktop/LOST.DIR/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for a in onlyfiles:
    if(a != "recoverpics.py"):
        os.rename(str(mypath) + a,str(mypath) +a.split(".")[0] + '.jpg')