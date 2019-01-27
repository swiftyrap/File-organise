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
excelPath = tempDataPath + "Excel/"
photoPath = tempDataPath + "Photo/"

def moveFiles():
    for file in os.listdir(desktopPath):
        if file.endswith(".txt") or file.endswith(".ppt")or file.endswith(".pdf"):
            if not os.path.exists(docPath+file):
                shutil.move(desktopPath + file, docPath +file)
        elif file.endswith(".xlsx"):
            if not os.path.exists(excelPath+file):
                shutil.move(desktopPath + file, excelPath +file)
        elif file.endswith(".JPG"):
            if not os.path.exists(photoPath+file):
                shutil.move(desktopPath + file, photoPath +file)

createFolder(tempDataPath)
createFolder(docPath)
createFolder(excelPath)
createFolder(photoPath)
moveFiles()
ctypes.windll.user32.MessageBoxW(0, "Folder is created.", "Title", 1)
