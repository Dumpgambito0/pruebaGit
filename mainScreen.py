import tkinter
from BackupFilesWindow import BackupFilesWindow

def otroMarco():
    BackupFilesWindow(root)

root = tkinter.Tk()
boton1 = tkinter.Button(root, text="Otro Marco", command=otroMarco).pack()
marco = BackupFilesWindow(root)
root.mainloop()
