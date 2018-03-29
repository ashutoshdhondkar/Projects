# this program will create our main window!
from tkinter import *   # imported for using gui

import MySQLdb  #imported this module for database connectivity


class MyGUI:
   
    # Home() will display the homepage that contains
    # login , forgot password,new entry,etc   
    def Home(self):
        
        self.root=Tk()  # created a main window
        self.frame=Frame(self.root,height=700,width=1000,bg="orange")
        
        # created a frame for home window
        self.frame.pack()
        self.frame.propagate(0)
        # this is done to avoid shrinking of our frame
        
        #let's create a label for our project
        self.label=Label(self.frame,text="Welcome to Moodle",font=('Times',30,'bold italic underline'),bg="orange",fg="black")
        self.label.pack(pady=30)
        
        self.root.title("Sies Moodle log in")
        
        # created a button for signing up 
        self.insert=Button(self.frame,text="Not registered yet?",bg="orange",fg="black",activebackground="red",font=('Times',15,'bold'),command=lambda :self.CommonMethod(1,self.root))
        self.insert.place(x=800,y=120)
        
        # creating a frame for our login and password
        self.nameLabel=Label(self.frame,text="Username",bg="orange",fg="black",font=('Times',15,'bold'))
        self.usernameEntry=Entry(self.frame,width=50)
        self.nameLabel.place(x=250,y=245)
        self.usernameEntry.place(x=370,y=250)
        
        self.passwordLabel=Label(self.frame,text=" Password",bg="orange",fg="black",font=('Times',15,'bold'))
        self.passwordLabel.place(x=250,y=295)
        self.passwordEntry=Entry(self.frame,width=50,show="@")
        self.passwordEntry.place(x=370,y=300)
        
        # creating a login button
        self.loginButton=Button(self.frame,text="Log In",font=('Times',15,'bold italic'),fg="black",bg="orange",activebackground="red",command=lambda : self.CheckRecord(self.root,self.frame,self.usernameEntry,self.passwordEntry))
        self.loginButton.place(x=450,y=350)
        
        # creating a forgot password button
        self.forgotPasswordButton=Button(self.frame,text="forgot password",font=('Times',15,'bold italic'),bg="orange",fg="black",activebackground="red",command=lambda : self.CommonMethod(3,self.root))
        self.forgotPasswordButton.place(x=415,y=420)
        
        # creating a visit website button for using php 
        self.gotoWebsiteButton=Button(self.frame,text="visit our website",font=('Times',15,'bold italic'),bg="green",fg="black",activebackground="red",command=lambda:self.CommonMethod(4,self.root))
        self.gotoWebsiteButton.pack(fill=X,side=BOTTOM,pady=180)
        
        self.refreshButton=Button(self.frame,text="Refresh",font=('Times',15,'bold italic') ,bg="orange",activebackground="red",command=lambda: self.gohome(self.root))
        self.refreshButton.place(x=100,y=120)
        
        self.root.mainloop()
    
        

    # this method will check if the user's info is present in database or not    
    @staticmethod
    def CheckRecord(root,frame,usernameEntry,passwordEntry):
        
        username=usernameEntry.get()
        passwd=passwordEntry.get()          
         
        # let's connect to our database
        db=MySQLdb.connect('localhost','root','','ostl')
        
        #let's now create a cursor for our db
        cursor=db.cursor()
                
        sql="SELECT * FROM moodle"
        try:
            cursor.execute(sql)  
            result=list(cursor.fetchall())
            print(result)
            
            # checking all the entries from database
            # if the particular username and password is found
            # then we'll set our flag to 1 and immediately come out of for loop
            for row in result:
                flag=0
                PRN=row[0]
                FNAME=row[1]
                LNAME=row[2]
                USERNAME=row[3]
                BRANCH=row[4]
                PASSWORD=row[5]
                if(username==USERNAME and passwd==PASSWORD):
                    prn=PRN
                    firstName=FNAME
                    lastName=LNAME
                    branch=BRANCH
                    flag=1
                    break
                    
            # if entry is found then open the user's logged in page
            # this page is defined in openLoggedInPage() method below
            if(flag==1):
                gui.openLoggedInPage(root,prn,firstName,lastName,username,branch,passwd)
            
            elif(flag==0):
                # if user is not found then print "username and password didn't matched!"
                label=Label(frame,text="username and password didn't matched!")
                label.pack()                 
                    
                                
        except:
            lbl=Label(frame,text="sorry we are unable to connect")
            lbl.pack()
            
        # create a notice board
        # enable scroll bar
        # create a feedback form
        # view attendance
    
    # this method will print user's details
    @staticmethod
    def openLoggedInPage(root,prn,firstName,lastName,username,branch,passwd):
        
        # let's close the previous window
        root.destroy()
        
        # let's create a new window to display user's stuffs
        new_root=Tk()
        
        # let's create a frame for our new window!
        newFrame=Frame(new_root,height=700,width=1000,bg="orange")
        newFrame.pack()
        newFrame.propagate(0)
        # so that our new frame will not shrink
        
        # welcoming message
        label=Label(newFrame,text="Welcome",font=('Times',30,'bold italic underline'),bg="orange",fg="black")
        label.pack(pady=30)
        
        # displaying user's info
        fullName=Label(newFrame,text = "Full Name : "+firstName+" "+lastName,font=('Monotype Corsiva',30,'bold italic'),bg="orange",fg="blue")
        fullName.place(x=250,y=200)
        
        prnLabel=Label(newFrame,text= "prn number : " ,font=('Monotype Corsiva',30,'bold italic'),bg="orange",fg="blue")
        prnLabel.place(x=250,y=300)
        
        prnnumber=Label(newFrame,text=prn ,font=('Normal',30,'bold'),bg="orange",fg="blue")
        prnnumber.place(x=450,y=300)
        
        if(branch=='ce' or branch=='CE'):
            branch='Computer Engineering'
        
        branchLabel=Label(newFrame,text=" Branch : "+branch,font=('Monotype Corsiva',30,'bold italic'),bg="orange",fg="blue")
        branchLabel.place(x=250,y=400)
        
        # create a view attendance button
        attendance=Button(newFrame,text="View My Attendance",font=('Times',30,'bold italic'),bg="green",activebackground="red")
        attendance.pack(side=BOTTOM,pady=100)
        
        
        # creating facilities for users such as log out and open notice board
        logout=Button(newFrame,text="Log Out",bg="orange",font=('Times',15,'bold italic'),command=lambda: gui.gohome(new_root))
        logout.place(x=900,y=100)
                
        noticeBoardButton=Button(newFrame,text="Notice Board",bg="orange",font=('Times',15,'bold italic'),command=lambda:gui.viewNoticeBoard(new_root,newFrame,prn,firstName,lastName,username,branch,passwd))
        noticeBoardButton.place(x=50,y=100)
    
    
    # this method will view noticeboard
    @staticmethod
    def viewNoticeBoard(new_root,frame,prn,firstName,lastName,username,branch,passwd):
        # destroyed previously openend window
        new_root.destroy()
        
        rootNoticeBoard=Tk()
        
        noticeBoardFrame=Frame(rootNoticeBoard,height=700,width=1000,bg="orange")
        noticeBoardFrame.pack()
        noticeBoardFrame.propagate(0)
        label=Label(noticeBoardFrame,text="welcome to notice board",bg="orange",font=('Times',30,'bold italic underline'))
        label.pack()
        
        back=Button(noticeBoardFrame,text="Back",bg="orange",font=('Times',15,'bold italic'),command=lambda: gui.openLoggedInPage(rootNoticeBoard,prn,firstName,lastName,username,branch,passwd))
        back.place(x=50,y=100)
        
        # now the notice will be written in file and our project will read stuffs from file
        # and display it under notice board section
        # thus to do so, we are making use of file handling
        
        filePointer=open("notice board.txt","r")
        
        notice=filePointer.read()
    
        t=Text(noticeBoardFrame,bg="orange",font=('Monotype Corsiva',15,'bold italic'))
        t.insert('end',notice)
        t.place(x=100,y=150)    
        
        #let's now create a scroll bar
        v=Scrollbar(noticeBoardFrame,orient=VERTICAL,command=t.yview)
        t.configure(yscrollcommand=v.set)
        v.pack(side=RIGHT)
        
        
        
    # a common method that will contain all methods related to home page
    # 1-> inserting;   3->forgot password    4-> website
    # let's declare this method as static as we are done using all attributes of class myGui
    # this method will create pages depending upon parameters passed
    
    @staticmethod
    def CommonMethod(num,root):
        
        # let's now destroy the previous home window
        root.destroy()
        
        new_root=Tk()  # created a new window
        # let's create a frame for our new window!
        newFrame=Frame(new_root,height=700,width=1000,bg="orange")
        newFrame.pack()
        newFrame.propagate(0)
        # so that our new frame will not shrink
            
        if(num==1):
            new_root.title("Create a new account ?")
            label=Label(newFrame,text="Creating a new account",bg="orange",fg="black",font=('Times',30,'bold italic underline'))
            label.pack(pady=30)
            
            # taking all the data before inserting
            
            firstNameLabel=Label(newFrame,text="First Name ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            firstNameLabel.place(x=200,y=145)
            
            firstNameEntry=Entry(newFrame,width=30)
            firstNameEntry.place(x=310,y=150)
            
            lastNameLabel=Label(newFrame,text="Last Name ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            lastNameLabel.place(x=200,y=195)
            
            lastNameEntry=Entry(newFrame,width=30)
            lastNameEntry.place(x=310,y=200)
            
            usernameLabel=Label(newFrame,text="Username ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            usernameLabel.place(x=200,y=245)
            
            usernameEntry=Entry(newFrame,width=30)
            usernameEntry.place(x=310,y=250)
            
            prnLabel=Label(newFrame,text="PRN ID",bg="orange",fg="black",font=('Times',15,'bold italic'))
            prnLabel.place(x=200,y=290)
            
            prnEntry=Entry(newFrame,width=20)
            prnEntry.place(x=310,y=295)
            
            branchLabel=Label(newFrame,text="Branch ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            branchLabel.place(x=200,y=340)
            
            branchEntry=Entry(newFrame,width=10)
            branchEntry.place(x=310,y=345)
            
            passLabel=Label(newFrame,text="Password ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            passLabel.place(x=200,y=385)
            
            passEntry=Entry(newFrame,width=30,show="@")
            passEntry.place(x=310,y=390)
            
            
            # creating a button
            createAccountButton=Button(newFrame,text="Create Account",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.InsertRecord(firstNameEntry,lastNameEntry,usernameEntry,prnEntry,branchEntry,passEntry,newFrame,new_root))
            createAccountButton.pack(side=BOTTOM,pady=180)
        
            homepage=Button(newFrame,text="Go back to log in page ?",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.gohome(new_root))
            homepage.place(x=350,y=580)          
            
        elif(num==3):
            new_root.title("Forgot password")
            label=Label(newFrame,text="Fill your Account Details",bg="orange",fg="black",font=('Times',30,'bold italic underline'))
            label.pack(pady=30)
            
            firstNameLabel=Label(newFrame,text="First Name ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            firstNameLabel.place(x=200,y=145)
            
            firstNameEntry=Entry(newFrame,width=30)
            firstNameEntry.place(x=310,y=150)
            
            lastNameLabel=Label(newFrame,text="Last Name ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            lastNameLabel.place(x=200,y=195)
            
            lastNameEntry=Entry(newFrame,width=30)
            lastNameEntry.place(x=310,y=200)
            
            usernameLabel=Label(newFrame,text="Username ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            usernameLabel.place(x=200,y=245)
            
            usernameEntry=Entry(newFrame,width=30)
            usernameEntry.place(x=310,y=250)
            
            prnLabel=Label(newFrame,text="PRN ID",bg="orange",fg="black",font=('Times',15,'bold italic'))
            prnLabel.place(x=200,y=290)
            
            prnEntry=Entry(newFrame,width=20)
            prnEntry.place(x=310,y=295)
            
            branchLabel=Label(newFrame,text="Branch ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            branchLabel.place(x=200,y=340)
            
            branchEntry=Entry(newFrame,width=10)
            branchEntry.place(x=310,y=345)
            
            passLabel=Label(newFrame,text="NEW Password ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            passLabel.place(x=150,y=385)
            
            passEntry=Entry(newFrame,width=30,show="@")
            passEntry.place(x=310,y=390)
            
            findAccountButton=Button(newFrame,text="Change Password ?",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.updateRecord(firstNameEntry,lastNameEntry,usernameEntry,prnEntry,branchEntry,passEntry,newFrame,new_root))    
            findAccountButton.pack(side=BOTTOM,pady=180)
            
            homepage=Button(newFrame,text="Go back to log in page ?",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.gohome(new_root))
            homepage.place(x=350,y=580)
            
   
    # this method will change the password on user's request 
    @staticmethod
    def updateRecord(firstNameEntry,lastNameEntry,usernameEntry,prnEntry,branchEntry,passEntry,newFrame,new_root):
        
        
        # data is taken from Entry widget using get() method
        
        fname=firstNameEntry.get().lower()
        lname=lastNameEntry.get().lower()
        # converted into lower case as we want it to use for updating new password
        
        username=usernameEntry.get()
        prn=prnEntry.get()
        branch=branchEntry.get().lower()
        passwd=passEntry.get()
        
        # let's create a tupple of the enterd data in same format as in database
        enteredDetails=prn+'-'+fname+'-'+lname+'-'+username+'-'+branch
        print(enteredDetails)
        
        # let's connect to our database
        db=MySQLdb.connect('localhost','root','','ostl')
        
        #let's now create a cursor for our db
        cursor=db.cursor()
        completeRecord=[]
        sql="SELECT PRN,FNAME,LNAME,USERNAME,BRANCH FROM moodle"
        try:
            cursor.execute(sql)
            result=list(cursor.fetchall())
            for row in result:
                PRN=row[0]
                FNAME=row[1].lower()
                LNAME=row[2].lower()
                USERNAME=row[3]
                BRANCH=row[4].lower()
                stringEntry=PRN+'-'+FNAME+'-'+LNAME+'-'+USERNAME+'-'+BRANCH
                completeRecord.append(stringEntry)
        except:
            lbl=Label(newFrame,text="Sorry we are unable to connect").pack()
            
        # completeRecord is a list of records in form of string
        # this will help us to identify whether a user is present in database or not
        # actually the update query will take care of the record
        # but it will not raise an error if specified detail is not found
        # thus to do so , we are checking the entered details in completeRecord
        # if entry is found we'll print "password changed successfully"
        # and if it is not found then print " Account not found"
        print(completeRecord)
        
        sql="UPDATE moodle SET PASSWORD = '%s' WHERE PRN = '%s' AND USERNAME = '%s' AND FNAME = '%s' AND LNAME='%s' AND BRANCH='%s' " %(passwd,prn,username,fname,lname,branch)          
                      
        try:
            cursor.execute(sql)
            db.commit()
            # checking data is present in database or not
            if(enteredDetails in completeRecord):
                lbl=Label(newFrame,text="password changed successfully!",font=('Times',15,'bold'))
                lbl.pack()
            else:
                lbl=Label(newFrame,text="Account not found!",font=('Times',15,'bold'))
                lbl.pack()
        except:
            db.rollback()
            
        db.close()
        
    # this method will always throw us to home window
    @staticmethod
    def gohome(root):
        root.destroy()
        gui.Home()
            
    
    # this method will help us to add new members into database
    @staticmethod        
    def InsertRecord(firstNameEntry,lastNameEntry,usernameEntry,prnEntry,branchEntry,passEntry,newFrame,new_root):
        
        # data is taken from Entry widget using get() method
        
        fname=firstNameEntry.get().lower()
        lname=lastNameEntry.get().lower()
        # converted into lower case as we want it to use for updating new password
        
        username=usernameEntry.get()
        prn=prnEntry.get()
        branch=branchEntry.get()
        passwd=passEntry.get()        
        
        # this is a list of a particular batch
        # only these members are allowed to create an account in moodle
        studentList=['116A1001','116A1002','116A1003','116A1004','116A1005','116A1006','116A1007','116A1008','116A1009','116A1010','116A1011','116A1012','116A1013','116A1014','116A1015','116A1016','116A1017','116A1018','116A1019']

        # let's connect to our database
        db=MySQLdb.connect('localhost','root','','ostl')
        
        #let's now create a cursor for our db
        cursor=db.cursor()
        
    
        #print(prn)
            
        # now it's time for us to insert this data into database if prn no is in list
        # but let's first check whether the prn is from our batch or not
        if (prn in studentList):
            
            # enter into database
            sql="SELECT username, FROM moodle"
            try:
                cursor.execute(sql)
                    
                # let's now create a list of our stored records
                result=cursor.fetchall()
                
                myusernameList=[list(x) for x in result]
                print(myusernameList)
                
                
                # let's create a list of student's username that are currently existing into database
                # this is done to avoid sharing common username
                userlist=[]
                for x in myusernameList:
                    userlist.append(x[0])
                    
                print(userlist)
                
                                        
                # if user is not present into database then insert it
                if(username not in userlist):
                    # then insert into database
                    
                    
                    sql="""INSERT INTO moodle(
                    PRN,
                                FNAME,LNAME,USERNAME,BRANCH,PASSWORD)
                                VALUES('%s','%s','%s','%s','%s','%s')"""%(prn,fname,lname,username,branch,passwd)
                
                    try:
                        cursor.execute(sql)
                        
                        db.commit()
                        
                        lbl=Label(newFrame,text="Account created successfully!",font=('Times',15,'bold'))
                        lbl.pack()
                    except:
                        db.rollback()
                        lbl=Label(newFrame,text="Sorry we are unable to connect!").pack()
                        
                else:
                    lbl=Label(newFrame,text="Sorry this username is already taken",font=('Times',15,'bold'))
                    lbl.pack(side=BOTTOM)
                        
            except:
                lbl=Label(newFrame,text="Unable to connect")
                lbl.pack()
                
        else:
            lbl=Label(newFrame,text="Please fill correct details!",font=('Times',15,'bold italic'),fg="black")
            lbl.pack()
                
                
        db.close()
        
        
gui=MyGUI()
gui.Home()