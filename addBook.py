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

class AddBook(Toplevel):
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
        self.lbl_id=Label(self.bottomFrame,text='ISBN:',font='arial 14 bold',fg='black', bg='#CCFFE5')
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
        #Author
        self.lbl_author=Label(self.bottomFrame,text='Author:',font='arial 14 bold',fg='black', bg='#CCFFE5')
        self.lbl_author.place(x=40,y=90)
        self.ent_author = Entry(self.bottomFrame,width=30,bd=4)
        #self.ent_author.insert(0,'Please Enter the author Name')
        self.ent_author.place(x=150,y=95)
        #genre
        self.lbl_genre=Label(self.bottomFrame,text='Genre:',font='arial 14 bold',fg='black', bg='#CCFFE5')
        self.lbl_genre.place(x=40,y=115)
        self.ent_genre = Entry(self.bottomFrame,width=30,bd=4)
        #self.ent_genre.insert(0,'Please Enter the Genre')
        self.ent_genre.place(x=150,y=120)
        #Publisher --- later on when we figure out drop down boxes for this
        #page
        self.lbl_pageNum=Label(self.bottomFrame,text='Length:',font='arial 14 bold',fg='black', bg='#CCFFE5')
        self.lbl_pageNum.place(x=40,y=140)
        self.ent_pageNum = Entry(self.bottomFrame,width=30,bd=4)
        #self.ent_pageNum.insert(0,'Please Enter the length of Book')
        self.ent_pageNum.place(x=150,y=145)

        #add Button
        submitButton=Button(self.bottomFrame,text='Add',command=self.addBook)
        submitButton.place(x=300,y=240)
    #get the data and then append into the table
    def addBook(self):
        name=self.ent_name.get()
        isbn=self.ent_id.get()
        genre=self.ent_genre.get()
        author=self.ent_author.get()
        pageNum=self.ent_pageNum.get()
        if(name and author and isbn and genre and pageNum !=""):
            try:
                q="SELECT count(*) from Books"
                b=cur.execute(q).fetchall()
                print(b)
                print(type(b))
                c=int(b[0][0])+1
                print(c)
                query="INSERT INTO 'Books' (ISBN,title,author,genre,page_count,id) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(isbn,name,author,genre,pageNum,c))
                quer_for_quantity="INSERT INTO Maintains (quantity,bookID) VALUES(?,?)"
                cur.execute(quer_for_quantity,(1,isbn))
                conn.commit()
                messagebox.showinfo("Success","Successfully added the book",icon="info")
            except:
                messagebox.showerror("Failed to add to DB","Cannot add to DB",icon="warning")
        else:
            messagebox.showerror("Failed to add to DB","Cannot add to DB",icon="warning")