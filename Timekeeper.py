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
        self.root.geometry('2600x1680')
        self.root['bg']=RestrictedEntry.bg
        self.root.title(RestrictedEntry.title)
        self.ticket_number = StringVar()
        
        Label(self.root,text="Enter Ticket number:",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=100,y=50)
        Entry(self.root,textvariable=self.ticket_number,width=30,bd=5).place(x=350,y=50)
        Button(self.root,text="IN",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.In).place(x=200,y=100)
        Button(self.root,text="OUT",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command = self.Out).place(x=300,y=100)
        
        self.fullname = StringVar()
        self.department = StringVar()
        Label(self.root,text="Full Name :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=200)
        Label(self.root,text="Department :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=250)
        Label(self.root,text="Shift :",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=300)
        
        Label(self.root,text="Photo ",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=50,y=350)
        
        self.memo = StringVar()
        Label(self.root,text="Reason for memo: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=430,y=350)
        
        Button(self.root,text="Update",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.update).place(x=600,y=550)
        Button(self.root,text="Print",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.Print).place(x=400,y=550)
        Button(self.root,text="Clear",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg,command=self.clear).place(x=200,y=550)
        
        ################################################################################
        Label(self.root,text="Remark: ",bg=RestrictedEntry.bg,fg=RestrictedEntry.fg,font=RestrictedEntry.allfont).place(x=500,y=400)
        self.remark=Text(self.root,font=('Times',15,'bold'),wrap=WORD,height=5,width=30)
        self.remark.propagate(0)
        self.remark.place(x=610,y=400)
        #self.remark.insert('end',text)
        ################################################################################
        
        self.cardLost = StringVar()
        Label(self.root,text="Card Lost: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=500,y=300)
        self.date = StringVar()
        self.time = StringVar()
        self.shift = StringVar()
    def In(self):
        self.check = DataBase.LoadCheck(self.ticket_number.get())
        
        if(self.UploadInfo()):
            Entry(self.root,textvariable=self.fullname,width=40,bd=5).place(x=200,y=200)
            Entry(self.root,textvariable=self.department,width=30,bd=5).place(x=200,y=250)
            Entry(self.root,textvariable=self.shift,width=30,bd=5).place(x=200,y=300)
            Entry(self.root,bd=5,width=40,textvariable=self.memo).place(x=610,y=350)
            
            Entry(self.root,bd=5,width=20,textvariable=self.cardLost).place(x=610,y=300)
                # check in update into database
            Label(self.root,text="Check in Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=50)
            Label(self.root,text="Check in Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=100)
            Label(self.root,textvariable = self.date,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=50)
            self.td = datetime.datetime.now()
            Label(self.root,textvariable = self.time,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=100)
            self.date.set(self.td.date())
            self.time.set(self.td.time())
            print("value of check in:{}".format(self.check))
            if(self.check==1):
                tkinter.messagebox.showwarning('','The worker is already inside the premises')
        else:
            tkinter.messagebox.showwarning('','User not enrolled')
    def Out(self):
        # check the value of flag from database
        self.check = DataBase.LoadCheck(self.ticket_number.get())
        if(self.UploadInfo()):
            Label(self.root,textvariable=self.fullname,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=200,y=200)
            Label(self.root,textvariable=self.department,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=200,y=250)
            Label(self.root,textvariable=self.memo,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=610,y=350)
            Label(self.root,textvariable=self.shift,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=200,y=300)
            self.check_in = StringVar()
            self.date_in = StringVar()
            
            Label(self.root,textvariable=self.cardLost,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=610,y=300)
            Label(self.root,text="Check in Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=50)
            Label(self.root,text="Check in Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=100)
            Label(self.root,text="Check out Date: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=150)
            Label(self.root,text="Check out Time: ",font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=600,y=200)
            Label(self.root,textvariable = self.date,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=150)
            self.td = datetime.datetime.now()
            Label(self.root,textvariable = self.time,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=200)
            self.date.set(self.td.date())   # set check_out time
            self.time.set(self.td.time())   # set check_out date
            Label(self.root,textvariable = self.check_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=100)
            Label(self.root,textvariable = self.date_in,font=RestrictedEntry.allfont,bg=RestrictedEntry.bg).place(x=800,y=50)
            
            self.check_in.set(self.dictionarydata['check_in'])  #set check_in time
            self.date_in.set(self.dictionarydata['date_in'])    #set check_in date
            self.shift.set(self.dictionarydata['shift'])
            if(self.check==0):  #if the user is outside the premises bt admin hit in button so to avoid errors care is taken
                tkinter.messagebox.showwarning('','The worker is not present inside the premises')
            else:
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
            DataBase.update(self.ticket_number.get(),self.memo.get(),self.remark.get('1.0','end'),self.date.get(),self.time.get(),self.cardLost.get(),self.shift.get())
            self.dictionarydata = DataBase.load(self.ticket_number.get())
            pdf = FPDF()
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.set_font('arial', 'B', 26)
            pdf.cell(ln=0, h=50, align='C', w=0, txt="Century Rayon", border=0)
            
            pdf.set_font('arial','',18)
            
            # Printing full name in pdf
            pdf.set_xy(20,40)
            pdf.cell(ln=0, h=0, w=0, txt="Name : ", border=0)
            
            pdf.set_xy(60,40)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['full_name'] , border=0)
            
            # printing department in pdf
            pdf.set_xy(20,60)
            pdf.cell(ln=0, h=0, w=0, txt="Department :  ", border=0)
            
            pdf.set_xy(60,60)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['department'] , border=0)
            
            #printing memo in pdf
            pdf.set_xy(20,80)
            pdf.cell(ln=0, h=0, w=0, txt="Memo : ", border=0)
            
            pdf.set_xy(60,80)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['reason_for_memo'] , border=0)
            
            # printing remark in pdf
            pdf.set_xy(20,100)
            pdf.cell(ln=0, h=0, w=0, txt="Remark : ", border=0)
            
            pdf.set_xy(60,100)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['remark'], border=0)
            
            #printing check in time
            pdf.set_xy(10,120)
            pdf.cell(ln=0, h=0, w=0, txt="Check in Time : ", border=0)
            
            pdf.set_xy(60,120)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['check_in'], border=0)
            
            # printing check in date
            pdf.set_xy(10,140)
            pdf.cell(ln=0, h=0, w=0, txt="Check in Date : ", border=0)
            
            pdf.set_xy(60,140)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['date_in'], border=0)
            
            #printing shift
            pdf.set_xy(20,160)
            pdf.cell(ln=0, h=0, w=0, txt="Shift : ", border=0)
            
            pdf.set_xy(60,160)
            pdf.cell(ln=0, h=0, w=0, txt=self.dictionarydata['shift'], border=0)
            
            
            #printing photo
            pdf.set_xy(20,180)
            pdf.cell(ln=0, h=0, w=0, txt="Photo : ", border=0)
            try:
                pdf.image(str(self.ticket_number.get())+'.png', 60, 180, 33)
            except Exception:
                pdf.set_xy(60,180)
                pdf.cell(ln=0, h=0, w=0, txt="Photo not available", border=0)
            
            # sign
            pdf.set_font('arial', 'B', 18)
            pdf.set_xy(50,240)
            pdf.cell(ln=0, h=0, w=0, txt="SIGN", border=0)
            
            
            pdf.output('Timekeeper.pdf')
            wb.open('timekeeper.pdf')
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
            self.img=PhotoImage(file=ticket)
            self.img=self.img.zoom(25,25)
            self.img=self.img.subsample(50)
            Label(self.root,image=self.img).place(x=50,y=400)
        except Exception:
            Label(self.root,text="unable to load image").place(x=50,y=400)
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
    def update(cls,ticket_number,memo,remark,date,time,cardLost,shift): #updating only in time
        #print(memo,remark,date,time,cardLost)
        cls.db.execute('''UPDATE LABOURS SET
                            Remark=?,card_lost=?,check_in=?,check_out=null,date_in=?,date_out=null,reason_for_memo=?,
                            flag=1,shift=?  WHERE TicketNo=?; ''',(remark,cardLost,time,date,memo,shift,ticket_number))
        cls.db.commit()
        pass
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
    
root=Tk()
re = RestrictedEntry()
re.MainPage(root)
root.mainloop()