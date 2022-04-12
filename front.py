#create UI design for the pages 
from audioop import add
from cgitb import text
from email import message
from itertools import count
from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from turtle import st
import sqlite3
import addBook
import addPublisher
import addMember
import givebook

myDatabase = 'table.db'
conn = sqlite3.connect(myDatabase)
cur = conn.cursor()

#from tkinter import tk

class Main(object):
    def __init__(self,master):
        self.master = master

        #
        def displayStatistics(evt):
            count_book=cur.execute("SELECT count(*) From Books").fetchall()
            count_reserrve=cur.execute(("Select count(*) From Reserve where status=?"),("borrowed",)).fetchall()
            count_staff=cur.execute("Select count(*) from staff").fetchall()
            count_client=cur.execute("Select count(*) from clients").fetchall()
            count_totalBook=cur.execute("SELECT quantity From Maintains").fetchall()
            #print(count_totalBook)
            sum_totalBook=0
            for a in count_totalBook:
                #print(a)
                sum_totalBook+=a[0]
            sum_totalBook+=count_reserrve[0][0]
            #print(sum_totalBook)
            self.lblBookCount.config(text='Total Number of UNIQUE Books: '+str(count_book[0][0]))
            self.lblMemberCount.config(text='Total Number of Members: '+str(count_staff[0][0]+count_client[0][0]))
            self.lblTakenCount.config(text='Total Number of Borrowed Books: '+str(count_reserrve[0][0]))
            self.lblStaffCount.config(text='Total Number of Officers: '+str(count_staff[0][0]))
            self.lblClientCount.config(text='Total Number of Client: '+str(count_client[0][0]))
            self.lblTotalBook.config(text='Total Number of Books: '+str(sum_totalBook))
            displayBooks(self)
            displayStudents(self)

        #display books for admin to view
        def displayBooks(self):
            books=cur.execute("Select * FROM Books").fetchall()
            count=0
            self.list_books.delete(0,END)
            for b in books:
                #print(b)
                self.list_books.insert(count,str(str(b[5])+"-"+b[0]+"-"+b[1]))
                count+=1
            def bookInfo(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id=value.split('-')[1]
                #maybe add an if else condition that checks for students and displays their corresponding data
                book=cur.execute("SELECT * FROM Books WHERE ISBN=?",(id,))
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

            def doubleClick(evt):
                global given_id
                value=str(self.list_books.get(self.list_books.curselection()))
                given_id=value.split('-')[0]
                give_book=self.GiveBook()

            self.list_books.bind('<<ListboxSelect>>',bookInfo)
            self.tabs.bind('<<NotebookTabChanged>>',displayStatistics)
            # self.tabs.bind('<ButtonRelease-1>',displayBooks)
            self.list_books.bind('<Double-Button-1>',doubleClick)

        def displayStudents(self):
            print("Here I Am")
            books=cur.execute("Select * FROM clients").fetchall()
            count=0
            self.list_students.delete(0,END)
            for b in books:
                #print(b)
                self.list_students.insert(count,str(str(b[0])+"-"+b[1]))
                count+=1
            def studentInfo(evt):
                value = str(self.list_students.get(self.list_students.curselection()))
                print("HERE I AM")
                print(value)
                id=value.split('-')[1]
                print(id)
                book=cur.execute("SELECT * FROM clients WHERE name=?",(id,))
                a=book.fetchall()
                print(a[0][0])
                memBorrows=cur.execute("Select * From Reserve where clientID=? and status=?",(a[0][0],"borrowed",))
                b=memBorrows.fetchall()
                print(b)
                #after we get ID we search to see if they have any books borrowed and we display that
                self.list_details2.delete(0,'end')
                self.list_details2.insert(0,"Name: "+a[0][1])
                self.list_details2.insert(1,"ID: "+str(a[0][0]))
                self.list_details2.insert(2,"Borrows: ")
                cou=3
                for c in b:
                    self.list_details2.insert(cou,str("BookID: "+c[2]))
                    cou+=1
                if cou==3:
                    self.list_details2.insert(cou,str("Student Has Not Borrowed any Books"))
                

            self.list_students.bind('<<ListboxSelect>>',studentInfo)
            self.tabs.bind('<<NotebookTabChanged>>',displayStatistics)


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
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
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
        '''self.btnlend=Button(topFrame,text='Lend Book',compound=LEFT,font='arial 12',command=self.giveBook)
        self.btnlend.pack(side=LEFT,padx=10)
        '''
        #Tabs in main page for accessibility
        self.tabs = ttk.Notebook(centerLeftFrame,width=850,height=660)
        self.tabs.pack()
        self.tab1=ttk.Frame(self.tabs)
        self.tab2=ttk.Frame(self.tabs)
        self.tab3=ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text='Library Management',compound=LEFT)
        self.tabs.add(self.tab2,text='Reports',compound=LEFT)
        self.tabs.add(self.tab3,text='Students',compound=LEFT)

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
        self.lblBookCount.grid(row=1,sticky=W)
        self.lblMemberCount=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblMemberCount.grid(row=2,sticky=W)
        self.lblTakenCount=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblTakenCount.grid(row=3,sticky=W)
        self.lblStaffCount=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblStaffCount.grid(row=4,sticky=W)
        self.lblClientCount=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblClientCount.grid(row=5,sticky=W)
        self.lblTotalBook=Label(self.tab2,text="",pady=20,font='Helvetica 12')
        self.lblTotalBook.grid(row=6,sticky=W)
        #students Details
        self.list_students = Listbox(self.tab3,width=40,height=30,bd=5,font='times 12 bold')
        self.sb=Scrollbar(self.tab3,orient=VERTICAL)
        self.list_students.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_students.yview)
        self.list_students.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        self.list_details2 = Listbox(self.tab3,width=60,height=30,bd=5,font='times 12 bold')
        self.list_details2.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)

        displayBooks(self)
        displayStatistics(self)
        displayStudents(self)

    def addBook(self):
        add=addBook.AddBook()
    
    def addPub(self):
        add=addPublisher.AddPublisher()
    
    def addMem(self):
        add=addMember.AddMember()
    
    class GiveBook(Toplevel):
        def __init__(self):
            Toplevel.__init__(self)
            self.geometry("650x750+550+200")
            self.title("Lend Book")
            global given_id
            self.book_id=given_id
            self.resizable(False,False)
            books=cur.execute("SELECT * from Books").fetchall()
            listBook=[]
            for b in books:
                listBook.append(str(str(b[5])+"-"+b[0]+"-"+b[1]))
            members=cur.execute("SELECT * from clients").fetchall()
            listMember=[]
            for m in members:
                listMember.append(str(str(m[0])+"-"+m[1]))
            #frames
            self.topFrame=Frame(self,height=100,bg='white')
            self.topFrame.pack(fill=X)
            self.bottomFrame=Frame(self,height=550,bg='#CCFFE5')
            self.bottomFrame.pack(fill=X)
            #heading
            heading=Label(self.topFrame,text='Give Book',font='arial 15 bold',fg='black',bg='white')
            heading.place(x=220,y=30)
            #input boxes
            #ISBN
            self.book_name=StringVar()
            self.lbl_name=Label(self.bottomFrame,text='Book Name:',font='arial 14 bold',fg='black', bg='#CCFFE5')
            self.lbl_name.place(x=40,y=40)
            self.combo_name=ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
            self.combo_name['values']=listBook
            self.combo_name.current(int(self.book_id)-1)
            self.combo_name.place(x=150,y=45)

            #Name
            self.member_name=StringVar()
            self.lbl_username=Label(self.bottomFrame,text='User Name:',font='arial 14 bold',fg='black', bg='#CCFFE5')
            self.lbl_username.place(x=40,y=65)       
            self.member_name=ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
            self.member_name['values']=listMember
            self.member_name.place(x=150,y=70)
            #add Button
            submitButton=Button(self.bottomFrame,text='Give Book',command=self.lendBook)
            submitButton.place(x=300,y=240)
    
        def lendBook(self):
            bookName=self.book_name.get()
            memberName=self.member_name.get()
            bookID=bookName.split("-")[1]
            memberID=memberName.split("-")[0]
            defStatus="borrowed"
            if bookName and memberName != "":
                a=cur.execute("SELECT * from maintains where quantity>0 and bookID=?",(bookID,)).fetchall()
                b=cur.execute("Select count(*) from reserve where BookID=? and clientID=?",(bookID,memberID,)).fetchall()
                c=cur.execute("Select * from Maintains where bookID=?",(bookID,)).fetchall()
                quantUpd=c[0][0]
                if(len(a)>0):
                    if(b[0][0]==0):
                        try:
                            quantUpd=quantUpd-1
                            query="INSERT INTO reserve (clientID,bookID,status) values (?,?,?)"
                            cur.execute(query,(memberID,bookID,defStatus))
                            conn.commit()
                            quer="UPDATE Maintains SET quantity=? WHERE (bookID)=?"
                            cur.execute(quer,(quantUpd,bookID))
                            conn.commit()
                            messagebox.showinfo("Success","successfully added to database!",icon="info")
                        except:
                            messagebox.showerror("Error","Cannot add to DB",icon="error")
                    else:
                        messagebox.showerror("Error","You already borrowed a Book",icon="error")
                else:
                    messagebox.showerror("Error","NOT AVAILABLE",icon="error")
            else:
                messagebox.showerror("Error","Field is empty",icon="error")
            
    def searchBooks(self):
        value = self.searchEntry.get()
        search=cur.execute("SELECT * FROM Books where title LIKE ?",('%'+value+'%',)).fetchall()
        self.list_books.delete(0,END)
        count=0
        for b in search:
            self.list_books.insert(count,str(str(b[5])+"-"+b[0]+"-"+b[1]))
            count+=1
     
    def listData(self):
        value=self.choice.get()
        if value==1:
            taken=cur.execute("Select * from Reserve where status=?",("borrowed",)).fetchall()
            self.list_books.delete(0,END)
            count=1
            self.list_books.insert(0,str("FORMAT IS BOOKID-STATUS-CLIENTID"))
            for b in taken:
                self.list_books.insert(count,str(f'{b[1]}'+"-"+b[2]+"-"+b[3]))
                count+=1
        elif value==2:
            avail=cur.execute("Select * from Maintains where quantity>?",(0,)).fetchall()
            self.list_books.delete(0,END)
            count=0
            for b in avail:
                self.list_books.insert(count,str(str(count+1)+"-"+b[1]))
                count+=1
        else:
            all=cur.execute("Select * from Books").fetchall()
            self.list_books.delete(0,END)
            count=0
            for b in all:
                #print(b)
                self.list_books.insert(count,str(str(b[5])+"-"+b[0]+"-"+b[1]))
                count+=1




def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1400x750+350+200")
    root.mainloop()

if __name__ == '__main__':
    main()