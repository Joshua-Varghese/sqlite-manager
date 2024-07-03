#This is the main script
'''
This script as of now only supports scripting, I will be rolling out new versions of this 
in the future, where you need not apply any scripting to get your things done in an SQLite Database

If you are an expert in TKinter and Python feel free to give me a hand in developing tools
such as this. Or support me in my Patreon
'''
from tkinter import *
from tkinter import Tk
from tkinter import ttk #to access Notebook otherwise showing error
from tkinter import messagebox
from tkinter import filedialog
import os
import sqlite3

#attributes of main win
ico = "theicon.ico"
geo = (500,500)
ttle = "SQLITE3 DATABASE MANAGER"
resize = [False,False]

#attributes of slaves
slaveGeo = (500,100)

app = Tk()
app.title(ttle)
app.geometry(f"{geo[0]}x{geo[1]}")
app.iconbitmap(ico)
app.resizable(resize[0],resize[1])


#function to create a database
def createDBWin():

    slave = Toplevel(app)
    slave.title(ttle)
    slave.geometry(f"{slaveGeo[0]}x{slaveGeo[1]}")
    slave.iconbitmap(ico)


    def createDBFunc(dbName):

            if dbName != None:
                wDir = filedialog.askdirectory(title="Choose the destination for Database File")
            try:
                if wDir != "":
                    db = sqlite3.connect(f"{wDir}/{dbName}.db")
                    db.close()
                    messagebox.showinfo("SUCCESS",f"You have successfull created a database in {wDir}")
                    slave.destroy()
                else:
                     messagebox.showerror("OOPS !","Please select a working directory to continue")
                     createDBFunc(dbName)
            except Exception as e:
                messagebox.showerror("OOPS !",f"Failed to Create Database File, Try again !{e}")

    entryBox = Entry(slave,relief=SUNKEN)
    entryBox.pack(fill=BOTH)
    
    crtDbButton = Button(slave,text="CREATE",command=lambda:createDBFunc(entryBox.get())).pack()
    slave.mainloop()
def openDBWin():
     #since the variables in createDBWin function are isolated, i.e they are local variables, I will be using th same terminologies for the 
     #variables in this function. This can be done by Classes, which will be done in the future versions of this tool
    directory = os.path.expanduser("~") #to find the home directory of the user
    wFile = filedialog.askopenfile(initialdir=f"{directory}/Desktop",filetypes=[("Data Base Files",".db")])
    if wFile != None:
         
        slave = Toplevel(app)
        slave.title(wFile.name)
        slave.geometry(f"{slaveGeo[0]}x{slaveGeo[1]}")
        slave.iconbitmap(ico)


        def openDBFunc(dbQuery):

                if dbQuery != None:
                    try:
                        db = sqlite3.connect(wFile.name)#called the name object otherwise, it will show <_io.TextIOWrapper name='C:/Users/joshu/Desktop/test.db' mode='r' encoding='cp1252'>

                        cur = db.cursor()

                        cur.execute(dbQuery)
                        output = cur.fetchall()
                        queryBox.delete("1.0",END)
                        queryBox.insert("1.0",output,"outputs")
                        db.commit()
                        db.close()
                        messagebox.showinfo("SUCCESS","Query Executed Successfully !")
                    except Exception as e:
                        messagebox.showerror("OOPS !",f"ERROR CODE:{e}")
                else:
                    pass
        
        if wFile != "":
            localtitle = wFile
            queryBox = Text(slave,relief=SUNKEN)
            queryBox.pack(fill=BOTH)

            #make it look cool
            #queryBox.tag_config("keywords",foreground="red")
            #queryBox.tag_config("output",foreground="green",background="black")
        
            crtDbButton = Button(slave,text="EXECUTE",command=lambda:openDBFunc(queryBox.get("1.0",END))).pack()#Get the entire text
        slave.mainloop()
    else:
         messagebox.showerror("CRITICAL ERROR","Select a database file !")
         lambda:openDBWin()
     

createBtn = Button(app,text="CREATE A DATABASE",command=lambda:createDBWin()).pack()
openBtn = Button(app,text="OPEN EXISTING DATABASE",command=lambda:openDBWin()).pack()
'''







return self.entryBox.get()
textBox = Text(self,bg="white").pack()





try:
def cal(databaseName):
    h = databaseHandler(databaseName)
    h.db.close()
except Exception as e:
messagebox.showerror("FAILED","FAILED TO CREATE DATABASE")
#finally:
#messagebox.showinfo("SUCCESS","DATABASE CREATED SUCCESFULLY !")


sub = Toplevel(app)
sub.title("CREATE DATABASE")
sub.iconbitmap(appinit.ico)
sub.geometry("300x150")
dbname = Entry(sub).grid(row=2,column=2)
dbbutton = Button(sub,text="CREATE",activebackground="green",padx=10,anchor=CENTER,command=lambda:cal(dbname)).grid(row=3,column=1)

def openDB():
pass'''

app.mainloop()
