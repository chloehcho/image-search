from pathlib import Path
from PIL import Image
import os

def readBytes(fileName):
    f = open(fileName, "rb")
    byte = f.read(1)
    while byte:
        print(byte)
        byte = f.read(1)
    f.close()


def createImageList(fileName):
    if(not os.path.exists('./keyimage')):
        print("keyimage directory not found")
        return
    outF = open(fileName, "w")
    basepath = Path('keyimage/')
    for entry in basepath.iterdir():
        if entry.is_dir():
            outF.write(entry.name + "\n")
            nextpath = Path('keyimage/' + entry.name + '/')
            entryLen = len(entry.name)
            entryID = entry.name[entryLen-2 :]
            outF.write(entryID)
            files_in_nextpath = nextpath.iterdir()
            for img in files_in_nextpath:
                if img.is_file():
                    outF.write(img.name + "\n")
    outF.close()

def openImage(fileName):
    path = Path.cwd()
    newpath = Path("/keyimage/EntryItemA0")
    pathname = str(path) + str(newpath)
    os.chdir(pathname)
    try:
        img = Image.open(fileName)
        img.show()
    except IOError:
        pass

class Image:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
