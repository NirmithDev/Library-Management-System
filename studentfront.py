'''
import sqlite3
myDatabase = 'table.db'
conn = sqlite3.connect(myDatabase)

# Create a cursor
cursor = conn.cursor()

# Get the database_initializer file
sql_file = open("tables.sql")
sql_as_string = sql_file.read()
#print(sql_as_string)
cursor.executescript(sql_as_string)
sql_file.close()
#print(sql_as_string)
'''
#create UI design for the pages 
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter import ttk
from turtle import st
import sqlite3
myDatabase = 'table.db'
conn = sqlite3.connect(myDatabase)
cur = conn.cursor()

#from tkinter import tk

class Main(object):
    def __init__(self,master):
        self.master = master
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
        self.searchBtn = Button(search_bar,text='search',font='arial 12',bg='white',fg='black')
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
        rb4=Radiobutton(list_bar,text='Students',var=self.choice,value=3,bg='orange',fg='white')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        rb4.grid(row=1,column=3)
        self.optBtn = Button(list_bar,text='Display',font='arial 12 bold',bg='orange',fg='white')
        self.optBtn.grid(row=1,column=4,padx=30,pady=10)

        #add book icon
        #self.iconbook=PhotoImage('icons/addbook.png')
        self.btnbook=Button(topFrame,text='Add New Book',compound=LEFT,font='arial 12')
        self.btnbook.pack(side=LEFT,padx=10)
        self.btnPublisher =Button(topFrame,text='Add New Publisher',compound=LEFT,font='arial 12')
        self.btnPublisher.pack(side=LEFT,padx=10)
        #add new member 
        #self.iconmember=PhotoImage('plus.png')
        self.btnmember=Button(topFrame,text='Add New Member',compound=LEFT,font='arial 12')
        self.btnmember.pack(side=LEFT,padx=10)
        #lend book
        self.btnlend=Button(topFrame,text='Lend Book',compound=LEFT,font='arial 12')
        self.btnlend.pack(side=LEFT,padx=10)
        
        #Tabs in main page for accessibility
        self.tabs = ttk.Notebook(centerLeftFrame,width=850,height=660)
        self.tabs.pack()
        #s = ttk.Style()
        # Create style used by default for all Frames
        #s.configure('TFrame', background='green')
        # Create style for the first frame
        #s.configure('Frame1.TFrame', background='red')
        #self.tab1=ttk.Frame(self.tabs,style='Frame1.TFrame')
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





def main():
    root = Tk()
    app = Main(root)
    root.title("Student")
    root.geometry("1400x750+350+200")
    root.mainloop()

if __name__ == '__main__':
    main()