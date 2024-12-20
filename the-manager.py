#This is the main script
'''
This script as of now only supports scripting, I will be rolling out new versions of this 
in the future, where you need not write any queries to get your things done in an SQLite Database

If you are an expert in TKinter and Python feel free to give me a hand in developing tools
such as this. Or support me in my Github Sponsorship page.
'''
from tkinter import *
from tkinter import Tk
from tkinter import ttk #to access Notebook otherwise showing error
from tkinter import messagebox
from tkinter import filedialog
import os
import sqlite3
#the problem is it is not deteching monitor size
#attributes of main win
_ = None
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
                else:
                     _ = messagebox.askretrycancel("OOPS !","Please select a working directory to continue")
                     if(_!=False):createDBFunc(dbName)

            except Exception as e:
                messagebox.showerror("OOPS !",f"Failed to Create Database File, Try again !{e}")
            slave.destroy()
    entryBox = Entry(slave,relief=SUNKEN)
    entryBox.pack(fill=BOTH)
    
    crtDbButton = Button(slave,text="CREATE",command=lambda:createDBFunc(entryBox.get()),activebackground="green").pack()
    slave.mainloop()
def openDBWin(remote=None):
     #since the variables in createDBWin function are isolated, i.e they are local variables, I will be using th same terminologies for the 
     #variables in this function. This can be done by Classes, which will be done in the future versions of this tool
    if (remote==None):
        directory = os.path.expanduser("~") #to find the home directory of the user
        wFile = filedialog.askopenfile(initialdir=f"{directory}/Desktop",filetypes=[("Data Base Files",".db")])
        if wFile != None:
            
            slave = Toplevel(app)
            slave.title(wFile.name)
            slave.geometry(f"{slaveGeo[0]}x{slaveGeo[1]}")
            slave.iconbitmap(ico)

            def output_win(out): #separate output screen
                 outpt_win = Toplevel(slave)
                 outpt_win.title("OUTPUT")
                 outpt_win.iconbitmap(ico)

                 outputbx = Text(outpt_win)
                 outputbx.pack()
                 outputbx.insert("1.0",out)
                 outpt_win.mainloop()

            def openDBFunc(dbQuery,event=None):
                    if dbQuery.strip() != "":
                        #print(dbQuery)
                        try:
                            db = sqlite3.connect(wFile.name)#called the name object otherwise, it will show <_io.TextIOWrapper name='C:/Users/joshu/Desktop/test.db' mode='r' encoding='cp1252'>

                            cur = db.cursor()

                            cur.execute(dbQuery)
                            output = cur.fetchall()
                            #queryBox.delete("1.0",END)
                            db.commit()
                            db.close()
                            messagebox.showinfo("SUCCESS","Query Executed Successfully !")
                            output_win(output)
                        except Exception as e:
                            messagebox.showerror("OOPS !",f"ERROR CODE:{e}")

                            
                    else:
                        pass
            
            if wFile != "":
                slave.bind("<Control_L>e",lambda event:openDBFunc(queryBox.get("1.0",END),event))
                app.iconify()
                localtitle = wFile
                
                queryBox = Text(slave,background="black",foreground="yellow",font=("Monospace","20"))
                queryBox.pack(fill=BOTH)
                queryBox.insert(END,"Ctrl+E to execute the code !")
            
                crtDbButton = Button(slave,text="EXECUTE",command=lambda:openDBFunc(queryBox.get("1.0",END))).pack()#Get the entire text
                #exeQueryBtn = Button(slave,text="EXECUTE",command=lambda:openDBFunc(queryBox.get("1.0",END)))
                #exeQueryBtn.pack()#Get the entire text
                #blobBtn = Button(slave,text="INSERT BLOB",command=lambda:blobInsert()).pack()


                

            slave.mainloop()
        else:
            _ = messagebox.askretrycancel("CRITICAL ERROR","Select a database file !")
            if(_!=False):openDBWin()

    


     

createBtn = Button(app,text="CREATE A DATABASE",command=lambda:createDBWin(),activebackground="green")
createBtn.pack()
openBtn = Button(app,text="OPEN EXISTING DATABASE",command=lambda:openDBWin(),activebackground="green")
openBtn.pack()

app.mainloop()
