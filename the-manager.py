#This is the main script
from tkinter import *
from tkinter import ttk #to access Notebook otherwise showing error
import sqlite3

class appinit(Tk):
    ico = "theicon.ico"
    geo = "500x500"
    ttle = "SQLITE3 DATABASE MANAGER"
    def __init__(self):
        super().__init__()
        self.title(appinit.ttle)
        self.geometry(appinit.geo)
        self.iconbitmap(appinit.ico)
        self.resizable(False,False)

        #self.notebook = ttk.Notebook(self)
        #self.notebook.grid(row=0,column=0)

    def buttons(self,buttonText,buttonCommand):
        btn = Button(self, text=buttonText, command=buttonCommand)
        btn.pack()
    
    def frames(self):
        frame = Frame(self)
        return frame
    
    def topWin(self,slave,commandReturnText):
        self.slave = Toplevel(self)
        self.slave.title(commandReturnText)
        self.slave.geometry(appinit.geo)
        self.slave.iconbitmap(appinit.ico)
        self.slave.mainloop()

    #def tabs(self,tabText,frm):
        #self.notebook.add(frm,text=tabText)
    def entry(self,entryBox):
        self.entryBox = Entry(self,padx=10)
        self.entryBox.pack()



app = appinit()
entry = app.entryBox(entry)


app.mainloop()