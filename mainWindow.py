############################     program Details #########################
#LANGUAGE : Python 3
#PROBLEM STATEMENT:
#    The following code will create a moodle (with gui using tkinter) 
#    This homepage will have options like creating a new account,logging in ,forgot password and link to website
#    Creating a new account :- If the person creating an account is not the member of first 19 students
#                                then he will not be able to create an account as condition based on rollno
#                                is provided. Also duplication of username is not allowed
#    Logging in :- If the account is successfully created then there will be no problem in logging in
#    Forgot password:- If the account's details are correct then there will be no problem in changing the password
#    Link to website:- on clicking "go to our website" button sies's homepage will open in browser

#    If the user is logged in successfully then the following options wil be available for him
#    Notice Board :- Here all the important notices will be viewed. The notice board will be updated only 
#                    by admin and no one else
#    View My Attendance:- Here excel sheet will be read and the attendance record of logged in user will
#                            be displayed
#    log out :- On clicking this the user will be thrown to homepage

#    Admin's access: The admin will have the following powers
#
#    Remove user:- If the admin has all the details of the user i.e. first name,last name,username and prn
#                    then he can anytime delete the user from database
#    Update notice board:- Here we have created a menu bar using filedialog submodule of tkinter.
#                        The admin will open notice board file, write new information and save it .
#                        This updated notice board will now be availabel for registered users to read
#    View registered users:- This will display the list of prn numbers and full name of the rsgistered users

#FEATURES:-
#            1. It would make easy for the student to view his attendance and defaulters subjects
#            2. Easy for everyone to get updated by notice board contents
#            3. Easy for the admin to just update notice board instead of announcing in multiple places,
#                    sending mails to student,etc. All this work can be reduced
#            4. Main thing is that the student can view only his attendance. No other student will know
#                about anyone else's attendance record
#            5.Deleting a particular user will help if the student has left the college or branch due to some
#                reason.
#############################################################################################################################

from tkinter import *   
# imported for using GUI

import MySQLdb  
#imported this module for database connectivity

import xlrd
# imported this module for reading attendance from excel sheet(.xlsx)

from tkinter import filedialog
# this is a sub module in tkinter and hence it should be imported separately

import webbrowser
# this we have imported to open link "http://www.siesgst.edu.in/"

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
        
        #let's create a log in label for adding more fun
        self.loginLabel=Label(self.frame,text="Moodle Login",bg="orange",fg="blue",font=('Monotype Corsiva',30,'bold italic underline'))
        self.loginLabel.place(x=380,y=180)
        
        
        # creating a login button
        self.loginButton=Button(self.frame,text="Log In",font=('Times',15,'bold italic'),fg="black",bg="orange",activebackground="red",command=lambda : self.CheckRecord(self.root,self.frame,self.usernameEntry,self.passwordEntry))
        self.loginButton.place(x=450,y=350)
        
        # creating a forgot password button
        self.forgotPasswordButton=Button(self.frame,text="forgot password",font=('Times',15,'bold italic'),bg="orange",fg="black",activebackground="red",command=lambda : self.CommonMethod(3,self.root))
        self.forgotPasswordButton.place(x=415,y=420)
        
        # creating a visit website button for using php 
        self.gotoWebsiteButton=Button(self.frame,text="visit our website",font=('Times',15,'bold italic'),bg="green",fg="black",activebackground="red",command=gui.OpenWebPage)
        self.gotoWebsiteButton.pack(fill=X,side=BOTTOM,pady=180)
        
        self.refreshButton=Button(self.frame,text="Refresh",font=('Times',15,'bold italic') ,bg="orange",activebackground="red",command=lambda: self.gohome(self.root))
        self.refreshButton.place(x=100,y=120)
        
        self.root.mainloop()
    
        

    # this method will check if the user's info is present in database or not   
    # also it will check whether the admin is logging in or a normal user 
    @staticmethod
    def CheckRecord(root,frame,usernameEntry,passwordEntry):
        
        username=usernameEntry.get()
        passwd=passwordEntry.get()          
         
        if(username=='admin' and passwd=='siesgstc1'):
            
            # if admin is logging in then we'll call to this module
            gui.openadminPage(root) 
        else:
            # this section is for normal user
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
    
    
    # admin will have rights to delete a particular user from database
    # also admin will take care of notice board 
    @staticmethod
    def openadminPage(root):
    
        root.destroy()
        #let's create a suitable window for our admin
        
        adminroot=Tk()
        adminFrame=Frame(adminroot,bg="orange",height=700,width=1000)
        adminFrame.pack()
        adminFrame.propagate(0)
        adminroot.title("ADMIN")
        
        logout=Button(adminFrame,text="Log Out",bg="orange",font=('Times',15,'bold italic'),command=lambda: gui.gohome(adminroot))
        logout.place(x=900,y=100)
        
        adminLabel=Label(adminFrame,text="Welcome Admin",bg="orange",font=('Times',30,'bold italic underline'))
        adminLabel.pack()
            
        deleteUser=Button(adminFrame,text="Remove User",bg="orange",activebackground="red",font=('Times',30,'bold italic'),command=lambda:gui.justadminThings(1,adminroot))
        deleteUser.place(x=350,y=200)
        
        updateNoticeBoard=Button(adminFrame,text="update notice board",bg="orange",activebackground="red",font=('Times',30,'bold italic'),command=lambda:gui.justadminThings(2,adminroot))
        updateNoticeBoard.place(x=300,y=350)
        
        viewUsers=Button(adminFrame,text="view all users",bg="orange",activebackground="red",font=('Times',30,'bold italic'),command=lambda:gui.justadminThings(3,adminroot))
        viewUsers.place(x=350,y=500)
    
    # this module will contain all the options that are availabe for admin
    # i.e. deleteing a user, updating notice board and even viewing the list of all registred students
    @staticmethod
    def justadminThings(num,adminroot):
        
        newadminroot=Tk()
        
        newadminFrame=Frame(newadminroot,height=700,width=1000,bg="orange")
        newadminFrame.pack()
        newadminFrame.propagate(0)
        
        adminroot.destroy()
        # num=1 indicates deleting a user
        # num=2 indicates updating notice board
        # num=3 indicates viewing attendance record of evry registered user
        
        if(num==1):
            newadminroot.title("Delete user")
            label=Label(newadminFrame,text="Delete user",bg="orange",font=('Times',30,'bold italic')).pack()
            
            firstNameLabel=Label(newadminFrame,text="First Name ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            firstNameLabel.place(x=200,y=145)
            
            firstNameEntry=Entry(newadminFrame,width=30)
            firstNameEntry.place(x=310,y=150)
            
            lastNameLabel=Label(newadminFrame,text="Last Name ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            lastNameLabel.place(x=200,y=195)
            
            lastNameEntry=Entry(newadminFrame,width=30)
            lastNameEntry.place(x=310,y=200)
            
            usernameLabel=Label(newadminFrame,text="Username ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            usernameLabel.place(x=200,y=245)
            
            usernameEntry=Entry(newadminFrame,width=30)
            usernameEntry.place(x=310,y=250)
            
            prnLabel=Label(newadminFrame,text="PRN ID",bg="orange",fg="black",font=('Times',15,'bold italic'))
            prnLabel.place(x=200,y=290)
            
            prnEntry=Entry(newadminFrame,width=30)
            prnEntry.place(x=310,y=295)
            
            delete=Button(newadminFrame,text="Delete User",font=('Times',15,'bold italic'),bg="green",fg="black",activebackground="red",command=lambda: gui.sureDelete(newadminroot,newadminFrame,firstNameEntry,lastNameEntry,usernameEntry,prnEntry))
            delete.pack(fill=X,side=BOTTOM,pady=250)
            
            goback=Button(newadminFrame,text="Back",bg="green",activebackground="red",font=('Times',15,'bold italic'),command=lambda:gui.openadminPage(newadminroot))
            goback.pack(side=LEFT,padx=20)
            
            #let's create a refresh button to add more fun
            refresh=Button(newadminFrame,text="Refresh",bg="orange",fg="black",font=('Times',15,'bold italic'),command=lambda:gui.justadminThings(1,newadminroot))
            refresh.place(x=800,y=100)
            
            
        elif(num==2):
            newadminroot.title("Update notice board")
            #newadminroot , newadminFrame
            
            #let's create a menu bar for admin to open a text file
            menubar=Menu(newadminroot)
            
            # attach this menu bar to adminroot
            newadminroot.config(menu=menubar)
            
            #let's create an option called as "File"
            # thus we create an object of "File" as file_menu
            file_menu=Menu(newadminroot,tearoff=0)
            
            # now we need to add options like open,save and exit for "File"
            file_menu.add_command(label="Open",command=lambda :gui.open_file(newadminroot,newadminFrame))
            file_menu.add_command(label="Save",command=lambda: gui.save_file(newadminroot,newadminFrame))
            
            # let's add a separator i.e. a dotted line
            file_menu.add_separator()
            
            #now let's create an exit option which will close our window
            file_menu.add_command(label="Exit",command=lambda: gui.gohome(newadminroot))
            
            #now we need to add our object in menubar under name "File"
            menubar.add_cascade(label="File",menu=file_menu)
            
            
            
            
        elif(num==3):
            
            newadminroot.title("List of registered users")
            
            lbl=Label(newadminFrame,text="Registered users",bg="orange",font=('Times',30,'bold'))
            lbl.pack()
            
            #let's create a back button so that the admin can again load his main page
            goback=Button(newadminFrame,text="Back",bg="green",activebackground="red",font=('Times',15,'bold italic'),command=lambda:gui.openadminPage(newadminroot))
            goback.place(x=50,y=40)
            
            
            userlbl=Text(newadminFrame,bg="orange",font=('Times',15,'bold'),wrap=WORD)
            userlbl.place(x=100,y=100)
            
            userlbl.insert('end','PRN'+'            '+'FULL NAME'+'\n')
            # let's connect to our database
            db=MySQLdb.connect('localhost','root','','ostl')
        
            #let's now create a cursor for our db
            cursor=db.cursor()
                
            sql="SELECT * FROM moodle"
            try:
                cursor.execute(sql)  
                result=cursor.fetchall()
                print(result)
                
                # checking all the entries from database
                # if the particular username and password is found
                # then we'll set our flag to 1 and immediately come out of for loop
                for row in result:
                    
                    PRN=row[0]
                    FNAME=row[1]
                    LNAME=row[2]
                    
                    # if fname and lname is not None then insert it into textbox
                    if(FNAME!=None and LNAME!=None):
                        userlbl.insert('end',PRN+'        '+FNAME+' '+LNAME+'\n')
                    
                    
                # scroll bar issue
                '''
                #let's now create a scroll bar for list of users
                #let's now create a scroll bar
                v=Scrollbar(userlbl,orient=VERTICAL,command=userlbl.yview)
                userlbl.configure(yscrollcommand=v.set)
                v.pack(side=RIGHT)
                '''
            except:
                print("Exception")
        
    
    # this method will open a specified file
    @staticmethod
    def open_file(newadminroot,newadminFrame):
        
        # let's open a dialogue box wherein we'll be selecting which file to be opened
        filename=filedialog.askopenfilename(parent=newadminroot,title="open my notice board",filetype=(("text files","*.txt"),("All files","*.*")))
        # filetype specifies which files to be displayed in dialogue box
        # filename will contain name of the file which user has selected
        
        # if the user has not pressed cancel
        if(filename!=None):
            #open that file in read mode
            f=open(filename,"r")
            
            label=Label(newadminFrame,text="Notice Board",bg="orange",font=('Normal',15,'bold')).pack()
            # now lets create a text box
            global textbox
            textbox =Text(newadminFrame,bg="orange",width=800,font=('Monotype Corsiva',15,'bold italic'),wrap=WORD)
            
            # now we need to read the data from specified file
            contents=f.read()
            
            # now its time to display those contents in text box
            textbox.insert('end',contents)
            textbox.place(x=0,y=50)
            
            #let's now close the file
            f.close()
             
    
    
    # this method will save a specified file
    @staticmethod
    def save_file(newadminroot,newadminFrame):
        
        #let's open a dialogue box to save the file
        filename=filedialog.asksaveasfilename(parent=newadminroot,defaultextension=".txt")
        # filename will contain the name of the file where we wish to save the data
        
        # if the user does not press cancel
        if(filename!=None):
            
            # open the file in write mode
            f=open(filename,'w')
            
            # now we need to read data from text box
            # this can be done using following statement 
            contents=str(textbox.get(1.0,END))
            
            # write the data in file
            f.write(contents)
            
            # close the file
            f.close()
    
    
    
    # this method will create a dialogue box whether the admin is sure if he wants to delete
    # a particular user or not
    
    @staticmethod
    def sureDelete(newadminroot,newadminFrame,firstNameEntry,lastNameEntry,usernameEntry,prnEntry):
            
        newframe=Frame(newadminroot,bg="yellow",height=200,width=300)
        newframe.place(x=300,y=200)
        newframe.propagate(0)
            
        lbl=Label(newframe,text="Are you sure you want to delete ?",bg="yellow",fg="black",font=('Times',15,'bold italic'))
        lbl.pack(pady=40)
            
        yes = Button(newframe,text="Yes",bg="blue",fg="white",activebackground="red",font=('Times',15,'bold italic'),command=lambda:gui.deleteUser(newframe,newadminroot,newadminFrame,firstNameEntry,lastNameEntry,usernameEntry,prnEntry))
        yes.pack(side=LEFT,padx=40)
        
        no=Button(newframe,text="No",bg="blue",fg="white",activebackground="red",font=('Times',15,'bold italic'),command=lambda: gui.justadminThings(1,newadminroot))
        no.pack(side=RIGHT,padx=40)
            
            
            
             
    #method to delete a particular user
    @staticmethod
    def deleteUser(newframe,newadminroot,newadminFrame,firstNameEntry,lastNameEntry,usernameEntry,prnEntry):
                
        newframe.destroy()
        
        fname=firstNameEntry.get().lower()
        lname=lastNameEntry.get().lower()
        username=usernameEntry.get()
        prn=prnEntry.get()
    
        
        
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
    
                if(fname==FNAME and lname==LNAME and username==USERNAME and prn==PRN):
                    flag=1;
                    break
            
            if(flag==1):
                
                sql="DELETE FROM moodle WHERE USERNAME = '%s' AND FNAME='%s' AND LNAME='%s' AND  PRN='%s'"%(username,fname,lname,prn)
                
                #sql="UPDATE moodle SET FNAME=NULL,LNAME=NULL,USERNAME=NULL, PASSWORD=NULL,BRANCH=NULL WHERE PRN='%s'"%(prn) 
                
                
                try:
                    cursor.execute(sql)
                    db.commit()
                    lbl=Label(newadminFrame,text="Account deleted successfully",font=('Times',15,'bold'))
                    lbl.pack()
                    
        
                except:
                    db.rollback()
                    lbl=Label(newadminFrame,text="unable to connect").pack()
                    
                
            elif(flag==0):
                    lbl=Label(newadminFrame,text="Account not found",font=('Times',15,'bold')).pack()
            
        except:
            lbl=Label(newadminFrame,text="unable to connect",font=('Times',15,'bold')).pack()
            
        #let's create a refresh button to add more fun
        refresh=Button(newadminFrame,text="Refresh",bg="orange",fg="black",font=('Times',15,'bold italic'),command=lambda:gui.justadminThings(1,newadminroot))
        refresh.place(x=800,y=100)
            
        
        
        
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
        
        new_root.title("Moodle homepage")
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
        attendance=Button(newFrame,text="View My Attendance",font=('Times',30,'bold italic'),bg="green",activebackground="red",command=lambda:gui.ViewMyAttendance(new_root,prn,firstName,lastName,username,branch,passwd))
        attendance.pack(side=BOTTOM,pady=100)
        
        
        # creating facilities for users such as log out and open notice board
        logout=Button(newFrame,text="Log Out",bg="orange",font=('Times',15,'bold italic'),command=lambda: gui.gohome(new_root))
        logout.place(x=900,y=100)
                
        noticeBoardButton=Button(newFrame,text="Notice Board",bg="orange",font=('Times',15,'bold italic'),command=lambda:gui.viewNoticeBoard(new_root,newFrame,prn,firstName,lastName,username,branch,passwd))
        noticeBoardButton.place(x=50,y=100)
    
        loginDisplay=Label(newFrame,text="-: My Profile :-",bg="orange",fg="purple",font=('Times',25,'bold italic underline'))
        loginDisplay.place(x=390,y=140)
        
        
        
    #let's create a method that will read the attendance of a particular student from  an excel sheet with .xlsx extension
    # we'll be using xlrd module for reading data from an excel sheet
    @staticmethod
    def ViewMyAttendance(root,prn,firstName,lastName,username,branch,passwd):
        root.destroy()
        
        #let's create a new window for displaying attendance
        attendanceRoot=Tk()
        attendanceFrame=Frame(attendanceRoot,height=700,width=1000,bg="orange")
        attendanceFrame.pack()
        attendanceFrame.propagate(0)

        #let's create a back button for user to take him back to his profile page
        back=Button(attendanceFrame,text="Back",bg="green",activebackground="red",font=('Times',15,'bold italic'),command=lambda: gui.openLoggedInPage(attendanceRoot,prn,firstName,lastName,username,branch,passwd))
        back.place(x=50,y=100)
        
        label=Label(attendanceFrame,text="Attendance",bg="orange",font=('Times',30,'bold italic underline'))
        label.pack()
        
        label75=Label(attendanceFrame,text="Attendance below 75 % will be given assignments ",bg="orange",fg="brown",font=('Times',25,'bold italic underline'))
        label75.place(x=200,y=100)

        #let's copy the path where our attendance record is stored
        # file name :- Book1.xlsx
        file_location="C:\\Users\\Admin\\My Documents\\LiClipse Workspace\\miniProject\\Book1.xlsx"
        # copied the file location in variabele - file_location
        
        #now let's load our workbook
        workbook=xlrd.open_workbook(file_location)
        
        # now let's load sheet1 of our workbook
        sheet=workbook.sheet_by_index(0)
        # 0-> indicates sheet1
        # 1-> indicates sheet2
        # and so on...
    
        #let's create an empty list than will contain attendance of a specified student 
        # of 6 subjects
        attendanceList=[]
        
        for i in range(1,sheet.nrows):
            #sheet.nrows will return total number of rows in excel sheet
            # here we are starting from 1,as we have headings stored at 0th index
            if(sheet.cell_value(i,0)==prn):
                #sheet.cell_value(i,j) gives the cell value at i-throw and j-th column
                for j in range(1,sheet.ncols):
                    attendanceList.append(sheet.cell_value(i,j))
                    
        
        print(attendanceList)
        
        lblAoa=Label(attendanceFrame,text="Analysis Of Algorithm : ",bg="orange",fg="black",font=('Monotype Corsiva',30,'bold italic'))
        lblAoa.place(x=200,y=200)
        attend = int(attendanceList[0])  # converted attend to int
        # now if attendance is less than 75 then display it with yellow background else display it normally 
        if(attend <75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",fg="yellow",font=('Normal',30,'bold italic underline'))
            lbl.place(x=580,y=200)
        elif(attend >=75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",font=('Normal',30,'italic'))
            lbl.place(x=580,y=200)
        ###############
        attend = int(attendanceList[1])
        lblCoa=Label(attendanceFrame,text="Computer Oraganization And Architecture : ",bg="orange",fg="black",font=('Monotype Corsiva',30,'bold italic'))
        lblCoa.place(x=100,y=250)
        if(attend <75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",fg="yellow",font=('Normal',30,'bold italic underline'))
            lbl.place(x=780,y=250)
        elif(attend >=75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",font=('Normal',30,'italic'))
            lbl.place(x=780,y=250)
        #####################    
            
        attend = int(attendanceList[2]) 
        lblOs=Label(attendanceFrame,text="Operating System : ",bg="orange",fg="black",font=('Monotype Corsiva',30,'bold italic'))
        lblOs.place(x=200,y=300)
        if(attend <75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",fg="yellow",font=('Normal',30,'bold italic underline'))
            lbl.place(x=500,y=300)
        elif(attend >=75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",font=('Normal',30,'italic'))
            lbl.place(x=500,y=300)
        
        attend = int(attendanceList[3])         
        lblOstl=Label(attendanceFrame,text="Python : ",bg="orange",fg="black",font=('Monotype Corsiva',30,'bold italic'))
        lblOstl.place(x=200,y=350)
        if(attend <75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",fg="yellow",font=('Normal',30,'bold italic underline'))
            lbl.place(x=360,y=350)
        elif(attend >=75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",font=('Normal',30,'italic'))
            lbl.place(x=360,y=350)
        
        
        attend = int(attendanceList[4])
        lblMaths=Label(attendanceFrame,text="Mathematics -4 : ",bg="orange",fg="black",font=('Monotype Corsiva',30,'bold italic'))
        lblMaths.place(x=200,y=400)
        if(attend <75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",fg="yellow",font=('Normal',30,'bold italic underline'))
            lbl.place(x=470,y=400)
        elif(attend >=75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",font=('Normal',30,'italic'))
            lbl.place(x=470,y=400)
        
        attend = int(attendanceList[5])
        lblCg=Label(attendanceFrame,text="Computer Graphics : ",bg="orange",fg="black",font=('Monotype Corsiva',30,'bold italic'))
        lblCg.place(x=200,y=450)
        if(attend <75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",fg="yellow",font=('Normal',30,'bold italic underline'))
            lbl.place(x=520,y=450)
        elif(attend >=75):
            lbl = Label(attendanceFrame,text =str(attend) +"%" ,bg="orange",font=('Normal',30,'italic'))
            lbl.place(x=520,y=450)
        
        
        
        
        lblNotice=Label(attendanceFrame,text="NOTE     : CONTACT     CLASS     INCHARGE     FOR     ANY     DOUBTS     RELATED     TO     ATTENDANCE",height=7,bg="orange",fg="blue")
        lblNotice.pack(side=BOTTOM,pady=40)
        
    
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
            
            # we are going to create a spinbox for branch selection
            branchLabel=Label(newFrame,text="Branch ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            branchLabel.place(x=200,y=340)
            #let's create a controller for spinbox
            branchEntry=StringVar()
            
            branchSpinbox=Spinbox(newFrame,values=('Computer Engineering','Mechanical Engineering','Information Technology','EXTC','PPT'),textvariable=branchEntry,width=30)
            branchSpinbox.place(x=310,y=345)
            
            passLabel=Label(newFrame,text="Password ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            passLabel.place(x=200,y=385)
            
            passEntry=Entry(newFrame,width=30,show="@")
            passEntry.place(x=310,y=390)
            
            refresh=Button(newFrame,text="Refresh",bg="orange",fg="black",font=('Times',15,'bold italic'),command=lambda:gui.CommonMethod(1,new_root))
            refresh.place(x=800,y=100)
            
            
            # creating a button
            createAccountButton=Button(newFrame,text="Create Account",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.InsertRecord(firstNameEntry,lastNameEntry,usernameEntry,branchEntry,prnEntry,passEntry,newFrame,new_root))
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
            
            prnEntry=Entry(newFrame,width=30)
            prnEntry.place(x=310,y=295)
          
            
            # we are going to create a spinbox for branch selection
            branchLabel=Label(newFrame,text="Branch ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            branchLabel.place(x=200,y=340)
            #let's create a controller for spinbox
            branchEntry=StringVar()
            
            branchSpinbox=Spinbox(newFrame,values=('Computer Engineering','Mechanical Engineering','Information Technology','EXTC','PPT'),textvariable=branchEntry,width=30)
            branchSpinbox.place(x=310,y=345)
            
            passLabel=Label(newFrame,text="NEW Password ",bg="orange",fg="black",font=('Times',15,'bold italic'))
            passLabel.place(x=150,y=385)
            
            passEntry=Entry(newFrame,width=30,show="@")
            passEntry.place(x=310,y=390)
            
            findAccountButton=Button(newFrame,text="Change Password ?",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.updateRecord(firstNameEntry,lastNameEntry,usernameEntry,prnEntry,branchEntry,passEntry,newFrame,new_root))    
            findAccountButton.pack(side=BOTTOM,pady=180)
            
            homepage=Button(newFrame,text="Go back to log in page ?",bg="green",fg="black",font=('Times',20,'bold italic'),activebackground="red",command=lambda:gui.gohome(new_root))
            homepage.place(x=350,y=580)
            
            refresh=Button(newFrame,text="Refresh",bg="orange",fg="black",font=('Times',15,'bold italic'),command=lambda:gui.CommonMethod(3,new_root))
            refresh.place(x=800,y=100)

    @staticmethod
    def OpenWebPage():
        webbrowser.open("http://www.siesgst.edu.in/")
   
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
        
        sql="UPDATE moodle SET PASSWORD = '%s' WHERE PRN = '%s' AND USERNAME = '%s' AND FNAME = '%s' AND LNAME='%s' AND BRANCH='%s'" %(passwd,prn,username,fname,lname,branch)          
                      
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
    def InsertRecord(firstNameEntry,lastNameEntry,usernameEntry,branchEntry,prnEntry,passEntry,newFrame,new_root):
        # data is taken from Entry widget using get() method
        
        fname=firstNameEntry.get().lower()
        lname=lastNameEntry.get().lower()
        # converted into lower case as we want it to use for updating new password
        
        username=usernameEntry.get()
        prn=prnEntry.get()
        branch=branchEntry.get().lower()
        passwd=passEntry.get() 
        
        #let's connect to our database
        db=MySQLdb.connect('localhost','root','','ostl')
        
        #let's now create a cursor
        cursor=db.cursor()
        
        #let's create a list of prn numbers present in database
        prnList=[]  
        
        #let's create a list of usernames present in database
        usernameList=[]
        
        # create a query to be fired
        sql="SELECT PRN,USERNAME FROM moodle"
        
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            for x in result:
                prnList.append(x[0])
                usernameList.append(x[1])
                
        except:
            lbl=Label(newFrame,text="unable to connect to database",bg="orange")
            lbl.pack()
        
        #let's create a student dictionary
        studentDict={x:y for x,y in zip(prnList,usernameList)}
        print(studentDict)
        
        # if prn is loaded into our database then only insert the rest of the data
        if(prn in prnList):
            
            # if username is none then only update it
            # this is done to prevent hacking of anyone's account
            # if prn no is already present and since we r using update query this hacking might take place
            # hence conditon studentDict[prn] == None is used
            if(studentDict[prn] == None):
                
                if(username not in usernameList):
                    sqlUp="UPDATE moodle SET FNAME='%s', LNAME='%s',USERNAME='%s',BRANCH='%s',PASSWORD='%s' WHERE PRN='%s'"%(fname,lname,username,branch,passwd,prn)
                
                    try:
                        cursor.execute(sqlUp)
                        db.commit()
                    except:
                            db.rollback()
                
                    lbl=Label(newFrame,text="Account Created Successfully!",font=('Times',15,'bold italic'))
                    lbl.pack()
                
                else:
                    lbl=Label(newFrame,text="Sorry this username is already in use",font=('Times',15,'bold italic'))
                    lbl.pack()
            else:
                lbl=Label(newFrame,text="Account already registered",font=('Times',15,'bold italic'))
                lbl.pack()
        else:
            lbl=Label(newFrame,text="Please Fill Correct Details",font=('Times',15,'bold italic'))
            lbl.pack()
               
gui=MyGUI() # object of our class

gui.Home()