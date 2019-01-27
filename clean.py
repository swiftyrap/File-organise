from config import *

createFolder(tempDataPath)
createFolder(docPath)
createFolder(excelPath)
createFolder(photoPath)
moveFiles()
ctypes.windll.user32.MessageBoxW(0, "Folder is created.", "Title", 1)
