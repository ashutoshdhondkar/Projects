from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime 
from fpdf import FPDF
import webbrowser as wb


'''
    This project will have two options :- in and out
    in: after entering the ticket number, the editable entry widget will appear and the admin
        is free to make any modifications in labour's data and give a copy by printing it.
    out: after entring the ticket number, the admin cannot write anything he can just view the details
        that was provided by him at the the time when the labour was entering.
'''

class RestrictedEntry:
    # the color and title can  be changed as required
    bg="powder blue"    
    title="Restrict Entry"
    allfont=('Normal',15,'bold')
    fg="black"
        
    def MainPage(self,root):
        self.root=root
        self.root.overrideredirect(True)
        self.root.geometry("{}x{}+0+0".format(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.root['bg']=RestrictedEntry.bg
        self.root.title(RestrictedEntry.title)
        self.ticket_number = StringVar()
        
        Label(self.root,text="Century Rayon - Time Office",bg=RestrictedEntry.bg,fg='blue',font=('Normal',18,'bold italic underline')).place(x=500,y=0)
        Label(self.root,text="Enter Ticket number:",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=100,y=50)
        Entry(self.root,textvariable=self.ticket_number,width=30,bd=5).place(x=350,y=50)
        Button(self.root,text="IN",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.In).place(x=200,y=100)
        Button(self.root,text="OUT",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.Out).place(x=300,y=100)
        
        self.fullname = StringVar()
        self.department = StringVar()
        Label(self.root,text="Full Name :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=200)
        Label(self.root,text="Department :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=250)
        Label(self.root,text="Shift :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=300)
        Label(self.root,text="Department code :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=350)
        Label(self.root,text="Photo ",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=400)
        
        self.memo = StringVar()
        Label(self.root,text="Reason for memo: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=350)
        
        Button(self.root,text="Update",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.update).place(x=600,y=600)
        Button(self.root,text="Print",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.Print).place(x=400,y=600)
        Button(self.root,text="Clear",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.clear).place(x=200,y=600)
        Button(self.root,text="Close",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command= lambda: root.destroy()).place(x=800,y=600)
        Button(self.root,text="New Employee",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.newUser).place(x=1000,y=600)
        ################################################################################
        Label(self.root,text="Remark: ",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=600,y=400)
        self.remark=Text(self.root,font=('Times',15,'bold'),wrap=WORD,height=5,width=30)
        self.remark.propagate(0)
        self.remark.place(x=800,y=400)
        #self.remark.insert('end',text)
        ################################################################################
        
        self.cardLost = StringVar()
        Label(self.root,text="Card Lost: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=300)
        self.date = StringVar()
        self.time = StringVar()
        self.shift = StringVar()
        self.dept_code = StringVar()
        
#***********************************************************************************************************
    def newUser(self):
        self.root.destroy()
        self.root = Tk()
        
        self.root.geometry("{}x{}+0+0".format(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.root['bg']=RestrictedEntry.bg
        self.root.title(RestrictedEntry.title)
        
        self.ticket_number = StringVar()
        Label(self.root,text="New Employee",bg=RestrictedEntry.bg,fg="blue",font=('Normal',20,'bold underline')).place(x=550,y=0)
        Label(self.root,text="Enter Ticket number:",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=100,y=100)
        Entry(self.root,textvariable=self.ticket_number,width=30,bd=5).place(x=350,y=100)
        Button(self.root,text="IN",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.NewIn).place(x=200,y=150)
        Button(self.root,text="OUT",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.NewOut).place(x=300,y=150)
        
        
        Label(self.root,text="Full Name :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=250)
        Label(self.root,text="Department :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=300)
        Label(self.root,text="Reason for Memo :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=350)
        Label(self.root,text="Shift :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=400)
        
        Button(self.root,text="Print",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.PrintNew).place(x=200,y=500)
        Button(self.root,text="Main Page",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.temp).place(x=400,y=500)
        Button(self.root,text="Close",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = lambda:self.root.destroy()).place(x=650,y=500)
        Button(self.root,text="Clear",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=lambda:self.newUser()).place(x=750,y=500)
        
        self.fullname = StringVar()
        self.shift = StringVar()
        self.memo = StringVar()
        self.department = StringVar()
        self.check_in = StringVar()
        self.check_out = StringVar()
        self.date_in = StringVar()
        self.date_out = StringVar()
    def temp(self):
        self.root.destroy()
        root=Tk()
        self.MainPage(root)
    
    def NewIn(self):
        if(self.ticket_number.get()):
            self.td = datetime.datetime.now()
            Entry(self.root,textvariable=self.fullname,bd=5,width=40).place(x=250,y=250)
            Entry(self.root,textvariable=self.department,bd=5,width=40).place(x=250,y=300)
            Entry(self.root,textvariable=self.memo,bd=5,width=40).place(x=250,y=350)
            Entry(self.root,textvariable=self.shift,bd=5,width=40).place(x=250,y=400)
            Label(self.root,text="Check in Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=100)
            Label(self.root,text="Check in Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=150)
            Label(self.root,textvariable = self.date_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=100)
            Label(self.root,textvariable = self.check_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=150)
            
            #check whether the ticket no. is present in database
            if(NewDataBase.CheckTicket(self.ticket_number.get())):
                self.dictionarydata = NewDataBase.LoadData(self.ticket_number.get())
                #if(self.dictionarydata['flag']==1):
                self.fullname.set(self.dictionarydata['full_name'])
                self.department.set(self.dictionarydata['department'])
                self.memo.set(self.dictionarydata['reason_for_memo'])
                self.shift.set(self.dictionarydata['shift'])
                print(self.dictionarydata)
                if(self.dictionarydata['flag']==1):
                    self.check_in.set(self.dictionarydata['check_in'])
                    self.date_in.set(self.dictionarydata['date_in'])
                    tkinter.messagebox.showwarning('','The Ticket number is already present inside the company')
                elif(self.dictionarydata['flag']==0):
                    self.check_in.set(self.td.time())
                    self.date_in.set(self.td.date())
            else:
                self.check_in.set(self.td.time())
                self.date_in.set(self.td.date())
        else:
            tkinter.messagebox.showwarning('','Please enter ticket number')
            
    def PrintNew(self):
        if(self.ticket_number.get()):
            if(self.fullname.get() and self.department.get() and self.shift.get() and self.memo.get()):
                if(NewDataBase.CheckTicket(self.ticket_number.get())):
                    NewDataBase.UpdateIn(self.ticket_number.get(),self.fullname.get(),self.memo.get(),self.check_in.get(),self.date_in.get(),self.shift.get(),self.department.get())
                else:
                    NewDataBase.InsertIn(self.ticket_number.get(),self.fullname.get(),self.memo.get(),self.check_in.get(),self.date_in.get(),self.shift.get(),self.department.get())
                self.PrintData()
            else:
                tkinter.messagebox.showwarning('','Fill in all the fields')
        else:
            tkinter.messagebox.showwarning('','Please enter Ticket number')
        
    def PrintData(self):
        self.dictionarydata = NewDataBase.LoadData(self.ticket_number.get())
        pdf = FPDF('P','mm','A5')
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial', 'B', 10)
        pdf.cell(ln=0, h=5, align='C', w=0, txt="Century Rayon", border=0)
                
        pdf.set_font('arial','',10)
                
                #printing ticket numbr
        pdf.set_xy(20,10)
        pdf.cell(ln=0, h=0, w=0, txt="Tkt No. : ", border=0)
                
        pdf.set_xy(60,10)
        pdf.cell(ln=0, h=0, w=0, txt=self.ticket_number.get(), border=0)
                
                
                # Printing full name in pdf
        pdf.set_xy(20,15)
        pdf.cell(ln=0, h=0, w=0, txt="Name : ", border=0)
                
        pdf.set_xy(60,15)
        pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['full_name'] , border=0)
                
                # printing department in pdf
        pdf.set_xy(20,20)
        pdf.cell(ln=0, h=0, w=0, txt="Department :  ", border=0)
                
        pdf.set_xy(60,20)
        pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['department'] , border=0)
                
                # printing department code
        pdf.set_xy(20,25)
        pdf.cell(ln=0, h=0, w=0, txt="Memo:  ", border=0)
                
        pdf.set_xy(60,25)
        pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['reason_for_memo'] , border=0)
                
        pdf.set_xy(10,30)
        pdf.cell(ln=0, h=0, w=0, txt="Check in Time : ", border=0)
                
        pdf.set_xy(60,30)
        pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['check_in'], border=0)
                
                # printing check in date
        pdf.set_xy(10,35)
        pdf.cell(ln=0, h=0, w=0, txt="Check in Date : ", border=0)
                
        pdf.set_xy(60,35)
        pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['date_in'], border=0)
                
                #printing shift
        pdf.set_xy(20,40)
        pdf.cell(ln=0, h=0, w=0, txt="Shift : ", border=0)
                
        pdf.set_xy(60,40)
        pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['shift'], border=0)

        pdf.set_font('arial', 'B', 10)
        pdf.set_xy(50,50)
        pdf.cell(ln=0, h=5, align='C', w=0, txt="SIGN", border=0)
                
        try:
            pdf.output('Timekeeper.pdf')
        except Exception:
            tkinter.messagebox.showerror('','Please close the previous pdf file')
        else:
            wb.open('timekeeper.pdf')
        
        
    
    def NewOut(self):
        if(self.ticket_number.get()):
            if(NewDataBase.CheckTicket(self.ticket_number.get())):
                self.dictionarydata = NewDataBase.LoadData(self.ticket_number.get())
                ###############################################################3
                Label(self.root,textvariable=self.fullname,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=250)
                Label(self.root,textvariable=self.department,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=300)
                Label(self.root,textvariable=self.memo,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=350)
                Label(self.root,textvariable=self.shift,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=400)
                Label(self.root,text="Check in Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=100)
                Label(self.root,text="Check in Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=150)
                Label(self.root,text="Check out Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=200)
                Label(self.root,text="Check out Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=250)
                
                Label(self.root,textvariable = self.date_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=100)
                Label(self.root,textvariable = self.check_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=150)
                
                Label(self.root,textvariable = self.date_out,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=200)
                Label(self.root,textvariable = self.check_out,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=250)
                
                ################################################################
                
                self.fullname.set(self.dictionarydata['full_name'])
                self.department.set(self.dictionarydata['department'])
                self.memo.set(self.dictionarydata['reason_for_memo'])
                self.shift.set(self.dictionarydata['shift'])
                self.check_in.set(self.dictionarydata['check_in'])
                self.date_in.set(self.dictionarydata['date_in'])
                if(self.dictionarydata['flag']==0):
                    self.check_out.set(self.dictionarydata['check_out'])
                    self.date_out.set(self.dictionarydata['date_out'])
                    tkinter.messagebox.showwarning('','The worker has already left')
                elif(self.dictionarydata['flag']==1):
                    self.td = datetime.datetime.now()
                    self.check_out.set(self.td.time())
                    self.date_out.set(self.td.date())
                    NewDataBase.UpdateOut(self.ticket_number.get(),self.check_out.get(),self.date_out.get())
                    self.dictionarydata = NewDataBase.LoadData(self.ticket_number.get())
                    if(self.dictionarydata):
                        fp = open("C:/Users/Ashutosh/My Documents/LiClipse Workspace/Trial/Logs/"+str(self.td.date())+".txt",'a')
                        writedata=[str(self.dictionarydata['date_in']),str(self.dictionarydata['check_in']),str(self.dictionarydata['check_out']),str(self.ticket_number.get())]
                        fp.write('||'.join(writedata))
                        fp.write("\n")
                        fp.close()
            else:
                tkinter.messagebox.showerror('','No such Ticket number entered')
        else:
            tkinter.messagebox.showwarning('','Please enter Ticket number')
    
    
#********************************************************************************************************
    def In(self):
        self.check = DataBase.LoadCheck(self.ticket_number.get())
        
        if(self.UploadInfo()):
            Entry(self.root,textvariable=self.fullname,width=40,bd=5).place(x=250,y=200)
            Entry(self.root,textvariable=self.department,width=30,bd=5).place(x=250,y=250)
            Entry(self.root,textvariable=self.shift,width=30,bd=5).place(x=250,y=300)
            
            #####
            self.choices = ['hello','world','how am i looking?']
            #Spinbox(self.root,values=self.choices,textvariable=self.memo,width=30).place(x=800,y=350)
            OptionMenu(self.root,self.memo,*self.choices).place(x=800,y=350)
            ####
            #Entry(self.root,bd=5,width=50,textvariable=self.memo).place(x=800,y=350)
            Entry(self.root,textvariable=self.dept_code,bd=5,width=30).place(x=250,y=350)
            Entry(self.root,bd=5,width=20,textvariable=self.cardLost).place(x=800,y=300)
                # check in update into database
            Label(self.root,text="Check in Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=50)
            Label(self.root,text="Check in Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=100)
            Label(self.root,textvariable = self.date,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=50)
            self.td = datetime.datetime.now()
            Label(self.root,textvariable = self.time,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=100)
            #self.date.set(self.td.date())
            #self.time.set(self.td.time())
            print("value of check in:{}".format(self.check))
            self.dictionarydata = DataBase.load(self.ticket_number.get())
            if(self.check==1):
                self.date.set(self.dictionarydata['date_in'])
                self.time.set(self.dictionarydata['check_in'])
                tkinter.messagebox.showwarning('','The worker is already inside the premises')
            else:
                self.date.set(self.td.date())
                self.time.set(self.td.time())
        else:
            tkinter.messagebox.showwarning('','User not enrolled')
    def Out(self):
        # check the value of flag from database
        self.check = DataBase.LoadCheck(self.ticket_number.get())
        if(self.UploadInfo()):
            Label(self.root,textvariable=self.fullname,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=200)
            Label(self.root,textvariable=self.department,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=250)
            Label(self.root,textvariable=self.memo,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=350)
            Label(self.root,textvariable=self.shift,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=300)
            Label(self.root,textvariable=self.dept_code,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=250,y=350)
            self.check_in = StringVar()
            self.date_in = StringVar()
            
            Label(self.root,textvariable=self.cardLost,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=300)
            Label(self.root,text="Check in Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=50)
            Label(self.root,text="Check in Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=100)
            Label(self.root,text="Check out Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=150)
            Label(self.root,text="Check out Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=200)
            Label(self.root,textvariable = self.date,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=150)
            self.td = datetime.datetime.now()
            Label(self.root,textvariable = self.time,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=200)
            Label(self.root,textvariable = self.check_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=100)
            Label(self.root,textvariable = self.date_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=50)
            
            self.check_in.set(self.dictionarydata['check_in'])  #set check_in time
            self.date_in.set(self.dictionarydata['date_in'])    #set check_in date
            self.shift.set(self.dictionarydata['shift'])
            if(self.check==0):  #if the user is outside the premises bt admin hit in button so to avoid errors care is taken
                self.date.set(self.dictionarydata['date_out'])
                self.time.set(self.dictionarydata['check_out'])
                tkinter.messagebox.showwarning('','The worker is not present inside the premises')
            else:
                self.date.set(self.td.date())   # set check_out time
                self.time.set(self.td.time())   # set check_out date
                
                #update only time and date of escaping
                DataBase.updateOutDateTime(self.ticket_number.get(),self.date.get(),self.time.get())
                
                self.dictionarydata = DataBase.load(self.ticket_number.get())
                #load all the data of ticket number from database
                if(self.dictionarydata):
                    fp = open("C:/Users/Ashutosh/My Documents/LiClipse Workspace/Trial/Logs/"+str(self.td.date())+".txt",'a')
                    writedata=[self.dictionarydata['date_in'],self.dictionarydata['check_in'],self.dictionarydata['check_out'],self.ticket_number.get()]
                    fp.write('||'.join(writedata))
                    fp.write("\n")
                    fp.close()
                
        else:
            tkinter.messagebox.showwarning('','User not enrolled')
    
    def Print(self):
        if(self.ticket_number.get()):
            if(self.dictionarydata['flag']==0):
                DataBase.update(self.ticket_number.get(),self.memo.get(),self.remark.get('1.0','end'),self.date.get(),self.time.get(),self.cardLost.get(),self.shift.get(),self.dept_code.get())
                self.dictionarydata = DataBase.load(self.ticket_number.get())
                pdf = FPDF('P','mm','A5')
                pdf.add_page()
                pdf.set_xy(0, 0)
                pdf.set_font('arial', 'B', 10)
                pdf.cell(ln=0, h=5, align='C', w=0, txt="Century Rayon", border=0)
                
                pdf.set_font('arial','',10)
                
                #printing ticket numbr
                pdf.set_xy(20,10)
                pdf.cell(ln=0, h=0, w=0, txt="Tkt No. : ", border=0)
                
                pdf.set_xy(60,10)
                pdf.cell(ln=0, h=0, w=0, txt=self.ticket_number.get(), border=0)
                
                
                # Printing full name in pdf
                pdf.set_xy(20,15)
                pdf.cell(ln=0, h=0, w=0, txt="Name : ", border=0)
                
                pdf.set_xy(60,15)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['full_name'] , border=0)
                
                # printing department in pdf
                pdf.set_xy(20,20)
                pdf.cell(ln=0, h=0, w=0, txt="Department :  ", border=0)
                
                pdf.set_xy(60,20)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['department'] , border=0)
                
                # printing department code
                pdf.set_xy(20,25)
                pdf.cell(ln=0, h=0, w=0, txt="Department code:  ", border=0)
                
                pdf.set_xy(60,25)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['department_code'] , border=0)
                
                
                #printing memo in pdf
                pdf.set_xy(20,30)
                pdf.cell(ln=0, h=0, w=0, txt="Memo : ", border=0)
                
                pdf.set_xy(60,30)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['reason_for_memo'] , border=0)
                
                # printing remark in pdf
                pdf.set_xy(20,35)
                pdf.cell(ln=0, h=0, w=0, txt="Remark : ", border=0)
                
                pdf.set_xy(60,35)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['remark'], border=0)
                
                #printing check in time
                pdf.set_xy(10,40)
                pdf.cell(ln=0, h=0, w=0, txt="Check in Time : ", border=0)
                
                pdf.set_xy(60,40)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['check_in'], border=0)
                
                # printing check in date
                pdf.set_xy(10,45)
                pdf.cell(ln=0, h=0, w=0, txt="Check in Date : ", border=0)
                
                pdf.set_xy(60,45)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['date_in'], border=0)
                
                #printing shift
                pdf.set_xy(20,50)
                pdf.cell(ln=0, h=0, w=0, txt="Shift : ", border=0)
                
                pdf.set_xy(60,50)
                pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['shift'], border=0)
                
                
                #printing photo
                pdf.set_xy(20,55)
                pdf.cell(ln=0, h=0, w=0, txt="Photo : ", border=0)
                try:
                    pdf.image(str(self.ticket_number.get())+'.png', 60, 55, 33)
                except Exception:
                    pdf.set_xy(60,55)
                    pdf.cell(ln=0, h=0, w=0, txt="Photo not available", border=0)
                
                # sign
                pdf.set_font('arial', 'B', 10)
                pdf.set_xy(50,100)
                pdf.cell(ln=0, h=5, align='C', w=0, txt="SIGN", border=0)
                
                try:
                    pdf.output('Timekeeper.pdf')
                except Exception:
                    tkinter.messagebox.showerror('','Please close the previous pdf file')
                else:
                    wb.open('timekeeper.pdf')
            else:
                tkinter.messagebox.showwarning('','The print has already been generated')
        else:
            tkinter.messagebox.showwarning('','Enter Ticket number')
        
        
    def update(self):
        if(self.ticket_number.get()):
            DataBase.updateAdmin(self.ticket_number.get(),self.memo.get(),self.remark.get('1.0','end'),self.cardLost.get())
            # based on admin's recommendation if any information is to be modifed later
            tkinter.messagebox.showinfo('','Successfully updated')
        else:
            tkinter.messagebox.showwarning('','Enter Ticket number')
    
    def clear(self):
        self.root.destroy()
        root = Tk()
        self.MainPage(root)
        
    def UploadInfo(self):
        ticket = str(self.ticket_number.get())+".PNG"
        #print(ticket)
        try:
            path="/Photo/"+str(self.ticket_number.get())+".PNG"
            self.img=PhotoImage(file=path)
            #self.img=PhotoImage(file=ticket)
            self.img=self.img.zoom(25,25)
            self.img=self.img.subsample(50)
            Label(self.root,image=self.img).place(x=50,y=450)
        except Exception:
            Label(self.root,text="unable to load image").place(x=50,y=450)
        self.dictionarydata={}
        
        
        #***********************************************************************
        # created object of class DataBase;
        # if we want to use different database then just change DataBase class
        self.db = DataBase()
        
        #************************************************************************
        #print(self.ticket_number.get())
        self.dictionarydata=self.db.load(self.ticket_number.get())
        #print(self.dictionarydata)
        if(self.dictionarydata):
            self.fullname.set(self.dictionarydata['full_name'])
            self.department.set(self.dictionarydata['department'])
            self.cardLost.set(self.dictionarydata['card_lost'])
            self.memo.set(self.dictionarydata['reason_for_memo'])
            self.remark.insert('end',self.dictionarydata['remark'])
            self.shift.set(self.dictionarydata['shift'])
            self.dept_code.set(self.dictionarydata['department_code'])
            return True
        else:
            return False
        #***********************************************************************
        
        #print(self.remark.get(0))
    # add date and time format in window
    # text section for remark
    # decide whether the worker is inside or outside the company premises and at what time he left
    
    
class DataBase:
    db = sqlite3.connect('C:/Users/Ashutosh/My Documents/LiClipse Workspace/Niit project/Century_Rayon.db')
    @classmethod
    def CreateTable(cls):
        pass
    @classmethod
    def update(cls,ticket_number,memo,remark,date,time,cardLost,shift,dept_code): #updating only in time
        #print(memo,remark,date,time,cardLost)
        cls.db.execute('''UPDATE LABOURS SET
                            Remark=?,card_lost=?,check_in=?,check_out=null,date_in=?,date_out=null,reason_for_memo=?,
                            flag=1,shift=?,department_code=?  WHERE TicketNo=?; ''',(remark,cardLost,time,date,memo,shift,dept_code,ticket_number))
        cls.db.commit()
    @classmethod
    def updateAdmin(cls,ticket_number,memo,remark,cardLost):
        cls.db.execute('''UPDATE LABOURS SET
                            Remark=?,reason_for_memo=?  WHERE TicketNo=?; ''',(remark,memo,ticket_number))
        cls.db.commit()
    
    @classmethod
    def updateOutDateTime(cls,ticket_number,date,time):
        cls.db.execute('''UPDATE LABOURS SET flag=0,check_out=?,date_out=?
                              WHERE TicketNo=?; ''',(time,date,ticket_number))
        cls.db.commit()
        
    @classmethod
    def load(cls,ticket_number):
        data = list(cls.db.execute("SELECT * FROM LABOURS WHERE TicketNo='%s';"%(ticket_number)))
        #print(data)
        dictionarydata = {}
        for x in data:
            dictionarydata['full_name'] = x[1]
            dictionarydata['remark'] = x[2]
            dictionarydata['card_lost'] = x[3]
            dictionarydata['reason_for_memo'] = x[4]
            dictionarydata['department'] = x[5]
            dictionarydata['check_in'] = x[6]
            dictionarydata['check_out'] = x[7]
            dictionarydata['date_in'] = x[8]
            dictionarydata['flag'] = x[9]
            dictionarydata['date_out'] = x[10]
            dictionarydata['shift'] = x[11]
            dictionarydata['department_code'] = x[12]
        return (dictionarydata)
    @classmethod
    def LoadCheck(cls,ticket_number):
        try:
            check=list(cls.db.execute("SELECT flag FROM LABOURS WHERE TicketNo='%s';"%(ticket_number)))
            print(check[0][0])
            return (check[0][0])

            # there was problem loading only check so had to do it in this manner
        except Exception:
            pass
        
class NewDataBase(DataBase):
    #db = sqlite3.connect('C:/Users/Ashutosh/My Documents/LiClipse Workspace/Niit project/Century_Rayon.db')
    
    @classmethod
    def InsertIn(cls,ticket_number,fullname,memo,check_in,date_in,shift,department):
        try:
            cls.db.execute('''INSERT INTO new(TicketNo,full_name,reason_for_memo,check_in,date_in,shift,department,flag,check_out,date_out)
                                        VALUES('%s','%s','%s','%s','%s','%s','%s',1,null,null);
                                        '''%(ticket_number,fullname,memo,check_in,date_in,shift,department))
            cls.db.commit()
        except Exception as e:
            print(e)
    
    @classmethod
    def UpdateOut(cls,ticket_number,check_out,date_out):
        try:
            cls.db.execute(''' UPDATE new SET check_out='%s',date_out='%s',flag=0 WHERE TicketNo = '%s';'''%(check_out,date_out,ticket_number))
            cls.db.commit()
        except Exception:
            pass
        
    @classmethod
    def UpdateIn(cls,ticket_number,fullname,memo,check_in,date_in,shift,department):
        try:
            cls.db.execute('''UPDATE new SET full_name='%s',reason_for_memo='%s',check_in='%s',date_in='%s',shift='%s',department='%s',
                                    flag=1,check_out=null,date_out=null WHERE TicketNo='%s';          
                            '''%(fullname,memo,check_in,date_in,shift,department,ticket_number))
            cls.db.commit()
        except Exception:
            pass    
        
    @classmethod
    def LoadData(cls,ticket_number):
        try:
            res = list(cls.db.execute("SELECT * FROM new WHERE TicketNo = '%s';"%(ticket_number)))
            dictionarydata = {}    
            for x in res:
                dictionarydata['full_name'] = x[1]                
                dictionarydata['reason_for_memo'] = x[2]
                dictionarydata['check_in'] = x[3]
                dictionarydata['check_out'] = x[4]
                dictionarydata['date_in'] = x[5]
                dictionarydata['date_out'] = x[6]
                dictionarydata['flag'] = x[7]
                dictionarydata['shift'] = x[8]
                dictionarydata['department'] = x[9]
            return dictionarydata
        except Exception:
            pass
        
    @classmethod
    def CheckTicket(cls,ticket_number):
        Ticket = []
        res = list(cls.db.execute("SELECT TicketNo FROM new;"))
        for x in res:
            Ticket.append(x[0])
        if(ticket_number in Ticket):
            return True
        else:
            return False
        
        
root=Tk()
re = RestrictedEntry()
re.MainPage(root)
root.mainloop()
