#create UI design for the pages 
from audioop import add
from cgitb import text
from itertools import count
from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter import ttk
from turtle import st
import sqlite3
import addBook
import addPublisher
import addMember

myDatabase = 'table.db'
conn = sqlite3.connect(myDatabase)
cur = conn.cursor()

#from tkinter import tk

class Main(object):
    def __init__(self,master):
        self.master = master

        #display books for admin to view
        def displayBooks(self):
            books=cur.execute("Select * FROM Books").fetchall()
            count=0
            for b in books:
                print(b)
                self.list_books.insert(count,str(b[0]+"-"+b[1]))
                count+=1
            def bookInfo(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id=value.split('-')[0]
                #print(id)
                book=cur.execute("SELECT * FROM Books WHERE ISBN=?",(id,))
                #print(book)
                book_information=book.fetchall()
                bookQ=cur.execute(f"SELECT quantity FROM Maintains WHERE bookID=?",(id,))
                bookQ=cur.fetchall()
                #print("here",bookQ)
                #print(book_information)
                self.list_details.delete(0,'end')
                self.list_details.insert(0,"ISBN: "+book_information[0][0])
                self.list_details.insert(1,"Book Name: "+book_information[0][1])
                self.list_details.insert(2,"Author: "+book_information[0][2])
                self.list_details.insert(3,"Genre: "+book_information[0][3])
                self.list_details.insert(4,"Pages: "+book_information[0][4])
                self.list_details.insert(5,"Qty: "+str(bookQ[0][0]))
                #add quantity
                #print(type(bookQ[0][0]))
                if bookQ[0][0] == 0 or bookQ[0][0]<0:
                    self.list_details.insert(6,"BOOK IS NO LONGER AVAILABLE")
                else:
                    self.list_details.insert(6,"BOOK IS AVAILABLE")


            self.list_books.bind('<<ListboxSelect>>',bookInfo)

        mainFrame = Frame(self.master)
        mainFrame.pack()
        #top
        topFrame = Frame(mainFrame,width=1400,height=110,bg='#CCFFE5',padx=20,relief=SUNKEN,borderwidth=3)
        topFrame.pack(side=TOP,fill=X)
        #center
        centerFrame = Frame(mainFrame,width=1400,relief=RIDGE,bg='#FFFF99',height=680)
        centerFrame.pack(side=TOP)
        #contents of center
        centerLeftFrame = Frame(centerFrame,width=900,height=700,bg='#FFFF99',borderwidth=2,relief='sunken')
        centerLeftFrame.pack(side=LEFT)
        centerRightFrame = Frame(centerFrame,width=500,height=400,bg='#FFFF99',borderwidth=5,relief='sunken')
        centerRightFrame.pack()

        #search bar
        search_bar =LabelFrame(centerRightFrame,width=440,height=75, text='search',bg='white')
        search_bar.pack(fill=BOTH)
        self.search=Label(search_bar,text='search',font='arial 12',fg='white',bg='orange')
        self.search.grid(row=0,column=0,padx=10,pady=10)
        self.searchEntry =Entry(search_bar,width=30,bd=10)
        self.searchEntry.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.searchBtn = Button(search_bar,text='search',font='arial 12',bg='white',fg='black',command=self.searchBooks)
        self.searchBtn.grid(row=0,column=4,padx=20,pady=10)
        
        #view by choice
        #1. borrowed
        #2. available
        #3. All Books
        #4. All Students
        list_bar = LabelFrame(centerRightFrame,width=440,height=100,text='Options',bg='orange')
        list_bar.pack(fill=BOTH)
        self.listlabel=Label(list_bar,text='Sort Book By',font='arial 12 bold',fg='white',bg='orange')
        self.listlabel.grid(row=0,column=2)
        #add items to be listed
        self.choice = IntVar()
        rb1=Radiobutton(list_bar,text='Borrowed',var=self.choice,value=1,bg='orange',fg='white')
        rb2=Radiobutton(list_bar,text='Available',var=self.choice,value=2,bg='orange',fg='white')
        rb3=Radiobutton(list_bar,text='All Books',var=self.choice,value=3,bg='orange',fg='white')
        rb4=Radiobutton(list_bar,text='Students',var=self.choice,value=4,bg='orange',fg='white')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        rb4.grid(row=1,column=3)
        self.optBtn = Button(list_bar,text='Display',font='arial 12 bold',bg='orange',fg='white',command=self.listData)
        self.optBtn.grid(row=1,column=4,padx=30,pady=10)

        #add book icon
        #self.iconbook=PhotoImage('icons/addbook.png')
        self.btnbook=Button(topFrame,text='Add New Book',compound=LEFT,font='arial 12',command=self.addBook)
        self.btnbook.pack(side=LEFT,padx=10)
        self.btnPublisher =Button(topFrame,text='Add New Publisher',compound=LEFT,font='arial 12',command=self.addPub)
        self.btnPublisher.pack(side=LEFT,padx=10)
        #add new member 
        #self.iconmember=PhotoImage('plus.png')
        self.btnmember=Button(topFrame,text='Add New Member',compound=LEFT,font='arial 12',command=self.addMem)
        self.btnmember.pack(side=LEFT,padx=10)
        #lend book
        self.btnlend=Button(topFrame,text='Lend Book',compound=LEFT,font='arial 12')
        self.btnlend.pack(side=LEFT,padx=10)
        
        #Tabs in main page for accessibility
        self.tabs = ttk.Notebook(centerLeftFrame,width=850,height=660)
        self.tabs.pack()
        self.tab1=ttk.Frame(self.tabs)
        self.tab2=ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text='Library Management',compound=LEFT)
        self.tabs.add(self.tab2,text='Reports',compound=LEFT)

        self.list_books = Listbox(self.tab1,width=40,height=30,bd=5,font='times 12 bold')
        self.sb=Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        self.list_details = Listbox(self.tab1,width=60,height=30,bd=5,font='times 12 bold')
        self.list_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)
        
        #stats
        self.lblBookCount = Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblBookCount.grid(row=0)
        self.lblMemberCount=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblMemberCount.grid(row=1,sticky=W)
        self.lblTakenCount=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblTakenCount.grid(row=2,sticky=W)

        displayBooks(self)

    def addBook(self):
        add=addBook.AddBook()
    
    def addPub(self):
        add=addPublisher.AddPublisher()
    
    def addMem(self):
        add=addMember.AddMember()
    
    def searchBooks(self):
        value = self.searchEntry.get()
        print(value)
        search=cur.execute("SELECT * FROM Books where title LIKE ?",('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)
        count=0
        for b in search:
                print(b)
                self.list_books.insert(count,str(b[0]+"-"+b[1]))
                count+=1
     
    def listData(self):
        value=self.choice.get()
        print(value)
        if value==1:
            taken=cur.execute("Select * from Reserve where status=?",("borrowed",)).fetchall()
            self.list_books.delete(0,END)
            count=1
            self.list_books.insert(0,str("FORMAT IS BOOKID-STATUS-CLIENTID"))
            for b in taken:
                self.list_books.insert(count,str(b[2]+"-"+b[3]+"-"+f'{b[1]}'))
                count+=1
        elif value==2:
            avail=cur.execute("Select * from Maintains where quantity>?",(0,)).fetchall()
            
            self.list_books.delete(0,END)
            count=0
            for b in avail:
                print(b)
                self.list_books.insert(count,str(b[1]))
                count+=1
        elif value==3:
            all=cur.execute("Select * from Books").fetchall()
            self.list_books.delete(0,END)
            count=0
            for b in all:
                self.list_books.insert(count,str(b[0]+"-"+b[1]))
                count+=1
        else:
            all=cur.execute("Select * from clients").fetchall()
            self.list_books.delete(0,END)
            count=0
            for b in all:
                self.list_books.insert(count,str(b[1]))
                count+=1




def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1400x750+350+200")
    root.mainloop()

if __name__ == '__main__':
    main()