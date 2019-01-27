import os
import ctypes
import shutil


def createFolder(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def getUsername():
    return os.getlogin()

desktopPath = "C:/Users/"+ getUsername() +"/Desktop/"
tempDataPath = "C:/Users/"+ getUsername() +"/Desktop/Temp data/"
docPath = tempDataPath + "Doc/"

def moveFiles():
    for file in os.listdir(desktopPath):
        if file.endswith(".txt"):
            if not os.path.exists(docPath+file):
                shutil.move(desktopPath + file, docPath +file)

createFolder(tempDataPath)
createFolder(docPath)
moveFiles()
ctypes.windll.user32.MessageBoxW(0, "Folder is created.", "Title", 1)
