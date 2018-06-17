from tkinter import *
import tkinter.messagebox
import sqlite3
class CenturyRayon:
    def HomePage(self,root):
        self.root = root
        self.frame = Frame(self.root,height = 500,width = 900,bg="black")
        self.frame.propagate(0)
        self.frame.pack()
        self.username = StringVar()
        self.password = StringVar()
        #Label(self.frame,text="Century Rayon",bg="black",fg="white",font=('monotype corsiva',50)).pack()
        Label(self.frame,text="USERNAME : ",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=150)
        Entry(self.frame,bd=5,width=50,textvariable=self.username,bg="powder blue").place(x=200,y=150)
        Label(self.frame,text="PASSWORD : ",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=250)
        Entry(self.frame,bd=5,width=50,show='@',textvariable=self.password,bg="powder blue").place(x=200,y=250)
        Button(self.frame,text="Log in",bg="cyan",width="30",command=self.LogInPage).place(x=250,y=350)
        path = "administrator.gif"
        self.img = PhotoImage(file=path)
        Label(self.frame,image=self.img,bg="black").place(x=600,y=120)
        self.username.set('Admin')
        self.passwd = 'test123'
    def LogInPage(self):
        if(self.passwd == self.password.get()):
            self.AdminPage()
        else:
            Label(self.frame,text="The password entered is incorrect",bg="black",fg="white",font=('Normal bold',15)).place(x=200,y=400)
    def AdminPage(self):
        self.frame.destroy()
        self.frame = Frame(self.root,height = 500,width = 900,bg="black").pack()
        self.img=PhotoImage(file="add.png")
        self.img = self.img.zoom(25)
        self.img = self.img.subsample(50)
        self.butt=Button(self.frame,image=self.img,bg="black",height="100",width="100",command=self.AddUser).place(x=0,y=0)
        self.img1 = PhotoImage(file="deleteUser.gif")
        self.img1 = self.img1.zoom(22)
        self.img1 = self.img1.subsample(50)
        Button(self.frame,image = self.img1,command = self.DeleteUser).place(x=1,y=105)
        self.img2 = PhotoImage(file = "blckList.gif")
        self.img2 = self.img2.zoom(22)
        self.img2 = self.img2.subsample(50)
        Button(self.frame,image = self.img2,command=self.BlackList).place(x=1,y=210)
        self.img3 = PhotoImage(file="update.gif")
        self.img3 = self.img3.zoom(22)
        self.img3 = self.img3.subsample(50)
        Button(self.frame,image = self.img3,command = self.update).place(x=1,y=310)
    def update(self):
        pass
    def BlackList(self):
        self.root.destroy()
        self.root = Tk()
        self.frame = Frame(self.root,height = 500,width = 900,bg="black").pack()
        Label(self.frame,text="Black List Section",bg="black",fg="white",font=('Normal',15,'bold underline')).place(x=350,y=0)
        self.block = StringVar()
        Label(self.frame,text="Enter Ticket number : ",bg="black",fg="white",font=('Normal',15)).place(x=100,y=100)
        Entry(self.frame,bg="powder blue",width=30,textvariable=self.block,bd=5).place(x=300,y=103)
        Button(self.frame,text="Blacklist\n",bg="cyan",fg="black",command = self.BlockUser).place(x=250,y=180)
        Button(self.frame,text="Remove\nBlacklist",bg="cyan",fg="black",command = self.UnBlockUser).place(x=350,y=180)
    def BlockUser(self):
        db = sqlite3.connect('Century_Rayon.db')
        db.execute('''CREATE TABLE IF NOT EXISTS BLACKLIST(
                            TicketNo TEXT PRIMARY KEY NOT NULL
                            );'''
                    )
        db.close()
        db = sqlite3.connect('Century_Rayon.db')
        ans=list(db.execute("SELECT TicketNo FROM BLACKLIST"))
        db.close()
        conn = sqlite3.connect('Century_Rayon.db')
        result = conn.execute("SELECT TicketNo FROM LABOURS")
        workers = []
        for x in result:
            workers.append(x[0])
        TicketList = []
        for x in ans:
            TicketList.append(x[0])  
        if(self.block.get() in workers):
            if(self.block.get() in TicketList):
                tkinter.messagebox.showwarning('','Ticket number already blacklisted')
            else:
                db = sqlite3.connect('Century_Rayon.db')
                db.execute("INSERT INTO BLACKLIST(TicketNo) VALUES('%s');"%(self.block.get()))
                db.commit()
                tkinter.messagebox.showinfo('','Successfully blacklisted')
                db.close()
        else:
            tkinter.messagebox.showerror('','Invalid Ticket number')
    def UnBlockUser(self):
        conn = sqlite3.connect('Century_Rayon.db')
        result = conn.execute("SELECT TicketNo FROM LABOURS")
        workers = []
        for x in result:
            workers.append(x[0])  
        conn.close()
        db = sqlite3.connect('Century_Rayon.db')
        res = db.execute("SELECT TicketNo FROM BLACKLIST;")
        black = []
        for x in res:
            black.append(x[0])
        if(self.block.get() in black):
            db.execute("DELETE FROM BLACKLIST WHERE TicketNo = '%s';"%(self.block.get()))
            db.commit()
            tkinter.messagebox.showinfo('','Successfully removed from blacklist')
        elif((self.block.get() in workers) and (self.block.get() not in black)):
            tkinter.messagebox.showinfo('','Not in blacklist')
        else:
            tkinter.messagebox.showerror('','Worker does not exists')
        db.close()
    def DeleteUser(self):
        self.root.destroy()
        self.root = Tk()
        self.ticketno = StringVar()
        self.frame = Frame(self.root,height = 500,width = 900,bg="black").pack()
        Label(self.frame,text="Remove User",bg="black",fg="white",font=('Normal bold',15)).place(x=350,y=0)    
        Label(self.frame,text="Enter Ticket No.",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=50)
        Entry(self.frame,bg="powder blue",width=30,textvariable = self.ticketno,bd=5).place(x=220,y=50)
        Button(self.frame,bg="cyan",text="Delete",command = self.viewData).place(x=500,y=50)
    def viewData(self):
        db = sqlite3.connect('Century_Rayon.db')
        ans = db.execute("SELECT TicketNo FROM LABOURS")
        ticket=[]
        for x in ans:
            ticket.append(x[0])
        db.close()
        if(self.ticketno.get() in ticket):
            Label(self.frame,text="User Info",font=('Normal bold ',15),bg="black",fg="white").place(x=350,y=100)
            db = sqlite3.connect('Century_Rayon.db')
            TicketNo = self.ticketno.get()
            self.res = db.execute("SELECT * FROM LABOURS WHERE TicketNo = '%s'"%(TicketNo))
            for x in self.res:
                Label(self.frame,text="Ticket number : "+str(self.ticketno.get()),font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=140)
                Label(self.frame,text="First Name : "+x[1],font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=180)
                Label(self.frame,text="Last Name : "+x[2],font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=220)
                Label(self.frame,text="Phone no : "+x[3],font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=260)
                Label(self.frame,text="Aadhar no. : "+x[4],font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=300)
                if(x[5]==None):
                    Label(self.frame,text="Worked days : 0",font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=340)
                else:
                    Label(self.frame,text="Worked days : "+x[5],font=('Normal bold ',15),bg="black",fg="white").place(x=10,y=340)
            Button(self.frame,bg="cyan",text="Delete",command = self.SureDelete,width=30).place(x=350,y=400)
        else:
            tkinter.messagebox.showwarning('Error','The Ticket number does not exists')
    def SureDelete(self):
        # create a custom message box to ask whether to delete the user or not!
        self.answer = tkinter.messagebox.askquestion('delete user','Are you sure you want to delete ?')
        try:
            db = sqlite3.connect('Century_Rayon.db')
            #self.ticketno1= self.ticketno.get()
            db.execute("DELETE FROM LABOURS WHERE TicketNo='%s';"%(self.ticketno.get()))
            db.commit()
            db.close()
        except Exception:
            Label(self.frame,text = "Sorry Unable to Delete The User! Try again",bg="black",fg="white",font=('Normal bold',15)).pack()
    def AddUser(self):
        self.root.destroy()
        self.root=Tk()
        self.frame = Frame(self.root,height = 500,width = 900,bg="black").pack()
        Label(self.frame,text="Registration Form",bg="black",fg="white",font=('Normal bold',15)).place(x=350,y=0)
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.phoneno = StringVar()
        self.aadhar = StringVar()
        self.ticketno = StringVar()
        Label(self.frame,text="First name : ",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=50)   
        Entry(self.frame,bg="powder blue",width = 30,textvariable=self.firstname,bd=5).place(x=200,y=50)
        Label(self.frame,text = "Last name : ",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=90)
        Entry(self.frame,bg="powder blue",width = 30,textvariable=self.lastname,bd=5).place(x=200,y=90)
        Label(self.frame,text="Aadhar Card No : ",bg="black",fg="white",font=('Normal bold',15)).place(x=30,y=140)
        Entry(self.frame,bg="powder blue",width=30,textvariable = self.aadhar,bd=5).place(x=200,y=140)
        Label(self.frame,text="Phone no : ",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=180)
        Entry(self.frame,bg="powder blue",width = 30,textvariable = self.phoneno,bd=5).place(x=200,y=180)
        Label(self.frame,text="Ticket no : ",bg="black",fg="white",font=('Normal bold',15)).place(x=50,y=220)
        Entry(self.frame,bg="powder blue",width = 30,textvariable = self.ticketno,bd=5).place(x=200,y=220)
        Button(self.frame,text="Add User",bg="cyan",command=self.Add).place(x=300,y=300)
    def CreateTable(self):
        db = sqlite3.connect('Century_Rayon.db')
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS LABOURS(
                        TicketNo PRIMARY KEY NOT NULL,
                        FirstName TEXT NOT NULL,
                        LastName TEXT NOT NULL,
                        PhoneNo TEXT NOT NULL,
                        Aadhar TEXT NOT NULL,
                        WorkingDays INT
                        );"""
        cursor.execute(sql)
        db.close()
    def Add(self):
        self.CreateTable()
        ticketno = self.ticketno.get()
        firstname = self.firstname.get() 
        lastname = self.lastname.get() 
        phoneno = self.phoneno.get() 
        aadhar = self.aadhar.get()
        if(ticketno and firstname and lastname and phoneno and aadhar):
            db = sqlite3.connect('Century_Rayon.db')
            cursor = db.cursor()
            ans = list(db.execute("SELECT TicketNo FROM LABOURS"))
            ticketList=[]
            for x in ans:
                ticketList.append(x[0])
            if(ticketno in ticketList):
                tkinter.messagebox.showwarning('', 'This Ticket number already exists')
            else:
                cursor.execute('''INSERT INTO LABOURS(TicketNo,FirstName,LastName,PhoneNo,Aadhar)
                                    VALUES(?,?,?,?,?);''',(ticketno,firstname,lastname,phoneno,aadhar))
                db.commit()
                tkinter.messagebox.showinfo('','Worker registered successfully!')
            db.close()
        else:
            tkinter.messagebox.showwarning('', 'Please fill in all the details')
root = Tk()
cr = CenturyRayon()
cr.HomePage(root)
root.mainloop()