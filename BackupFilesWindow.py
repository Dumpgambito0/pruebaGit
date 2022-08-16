import tkinter

class BackupFilesWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='blue', width=600, height=300)
        self.pack(fill='both', expand='true')
        self.pack_propagate(False)
        self.boton()
    
    def boton(self):
        self.boton = tkinter.Button(self, text="Cerar Frame", command=self.destroy)
        self.boton.place(relx=0.45, rely=0.90)
    