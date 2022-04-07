from cgitb import text
from msilib.schema import Icon
from operator import iconcat
from textwrap import fill
from tkinter import *
from tkinter import messagebox
import sqlite3

myDatabase = 'table.db'
conn = sqlite3.connect(myDatabase)
cur = conn.cursor()

class AddPublisher(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+550+200")
        self.title("ADD New Book")
        self.resizable(False,False)
        #frame boxes
        self.topFrame=Frame(self,height=100,bg='white')
        self.topFrame.pack(fill=X)
        self.bottomFrame=Frame(self,height=550,bg='#CCFFE5')
        self.bottomFrame.pack(fill=X)
        #heading
        heading=Label(self.topFrame,text='Add New Book',font='arial 15 bold',fg='black',bg='white')
        heading.place(x=220,y=30)
        #input boxes
        #ISBN
        self.lbl_id=Label(self.bottomFrame,text='pubID:',font='arial 14 bold',fg='black', bg='#CCFFE5')
        self.lbl_id.place(x=40,y=40)
        self.ent_id = Entry(self.bottomFrame,width=30,bd=4)
        #self.ent_id.insert(0,'Please Enter the ISBN of the book')
        self.ent_id.place(x=150,y=45)
        #Name
        self.lbl_name=Label(self.bottomFrame,text='Name:',font='arial 14 bold',fg='black', bg='#CCFFE5')
        self.lbl_name.place(x=40,y=65)
        self.ent_name = Entry(self.bottomFrame,width=30,bd=4)
        #self.ent_name.insert(0,'Please Enter the Name of the book')
        self.ent_name.place(x=150,y=70)
        #pub Name
        self.lbl_email=Label(self.bottomFrame,text='Email:',font='arial 14 bold',fg='black', bg='#CCFFE5')
        self.lbl_email.place(x=40,y=90)
        self.ent_email = Entry(self.bottomFrame,width=30,bd=4)
        #self.ent_author.insert(0,'Please Enter the author Name')
        self.ent_email.place(x=150,y=95)
        #add Button
        submitButton=Button(self.bottomFrame,text='Add',command=self.addPub)
        submitButton.place(x=300,y=240)
    
    #get the data and then append into the table
    def addPub(self):
        name=self.ent_name.get()
        email=self.ent_email.get()
        genre=self.ent_id.get()
        if(name and email and genre !=""):
            try:
                query="INSERT INTO 'publisher' (publisher_id,name,email) VALUES(?,?,?)"
                cur.execute(query,(genre,name,email))
                conn.commit()
                messagebox.showinfo("Success","Successfully added the publisher",icon="info")
            except:
                messagebox.showerror("Failed to add to DB","Cannot add to DB",icon="warning")
        else:
            messagebox.showerror("Failed to add to DB","Cannot add to DB",icon="warning")

