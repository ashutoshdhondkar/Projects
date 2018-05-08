# calculator that performs basic operations like + , - , * and /
#    The updated version i.e. the scientific calculator will be updated later

from tkinter import *
from math import *



# let's create a class which will contain all methods related to calculator
class Calculator:
    #    this is an empty list which will store operators as well as operand
    value=[]
    
    #    let's create a constructor
    def __init__(self,root):
        #    this will create a title for our calculator window
        root.title("Calculator")
        root['bg']="powder blue"
      
        #    now let's create entry widget that will display entered inputs and result
        #    but before that let's create a string instance of entry widget
        self.entry_instance = StringVar()
        self.entryDisplay=Entry(root,textvariable=self.entry_instance,justify=RIGHT,bd=10,width=30,font=('Times',10,'bold')).grid(ipady=10,columnspan=7)
        #    ipad is internal padding
        
    
        #let's now create buttons from 1 to 10
        butt7=Button(root,text="7",width=5,bd=5,command=lambda: self.PutButtonValues('7')).grid(row=1 , column=0)
        
        butt8=Button(root,text="8",width=5,bd=5,command=lambda: self.PutButtonValues('8')).grid(row=1 , column=1)
        
        butt9=Button(root,text="9",width=5,bd=5,command=lambda: self.PutButtonValues(9)).grid(row=1 , column=2)
        
        butt5=Button(root,text="4",width=5,bd=5,command=lambda: self.PutButtonValues(4)).grid(row=2 , column=0)
        
        butt5=Button(root,text="5",width=5,bd=5,command=lambda: self.PutButtonValues(5)).grid(row=2 , column=1)
        
        butt6=Button(root,text="6",width=5,bd=5,command=lambda: self.PutButtonValues(6)).grid(row=2 , column=2)
        
        butt1=Button(root,text="1",width=5,bd=5,command=lambda: self.PutButtonValues(1)).grid(row=3 , column=0)
        
        butt2=Button(root,text="2",width=5,bd=5,command=lambda: self.PutButtonValues(2)).grid(row=3 , column=1)
        
        butt3=Button(root,text="3",width=5,bd=5,command=lambda: self.PutButtonValues(3)).grid(row=3 , column=2)
        
        butt0=Button(root,text="0",width=5,bd=5,command=lambda: self.PutButtonValues(0)).grid(row=4 , column=0)
        
        #    let's create buttons for decimal point,add,multiply,division,subtract
        buttdot=Button(root,text=".",width=5,bd=5,command=lambda: self.PutButtonValues('.')).grid(row=4,column=1)
        
        buttadd=Button(root,text="+",width=5,bd=5,command=lambda: self.PutButtonValues('+')).grid(row=4 , column=2 )
        
        buttsub=Button(root,text="-",width=5,bd=5,command=lambda: self.PutButtonValues('-')).grid(row=5 , column=0)
        
        buttmul=Button(root,text="*",width=5,bd=5,command=lambda: self.PutButtonValues('*')).grid(row=5 , column=1)
        
        buttdiv=Button(root,text="/",bd=5,width=5,command=lambda: self.PutButtonValues('/')).grid(row=5 , column=2)
        
        buttcal=Button(root,text="ANS",bd=5,width=5,command=self.evaluate).grid(row= 6, column=1)
        
        buttclear=Button(root,text="CLEAR",bd=5,width=5,command=self.clear).grid(row= 6, column=0)
        
        buttdel=Button(root,text="DEL",width=5,bd=5,command=self.delLast).grid(row= 6, column=2)
        
        buttop=Button(root,text="(",width=5,bd=5,command=lambda:self.PutButtonValues('(')).grid(row= 1, column=3,padx=2)
        
        buttclose=Button(root,text=")",width=5,bd=5,command=lambda:self.PutButtonValues(')')).grid(row= 2, column=3,padx=2)
        
        buttclose=Button(root,text="MOD",width=5,bd=5,command=lambda:self.PutButtonValues('%')).grid(row= 3, column=3,padx=2)

        buttPow=Button(root,text="^",width=5,bd=5,command=lambda:self.PutButtonValues('^')).grid(row= 4, column=3,padx=2)

        buttSqrt=Button(root,text="sqrt",width=5,bd=5,command=lambda:self.PutButtonValues('sqrt(')).grid(row= 5, column=3,padx=2)

        buttonLog=Button(root,text="ln",width=5,bd=5,command=lambda:self.PutButtonValues('log(')).grid(row= 6, column=3,padx=2)

        buttonLog10=Button(root,text="Log10",width=5,bd=5,command=lambda:self.PutButtonValues('log10(')).grid(row=7 , column=3,padx=2)
        
        buttonSine = Button(root,text="sin",width=5,bd=5,command=lambda:self.PutButtonValues('sin(')).grid(row=7,column = 0,padx = 2)
        
        buttonCos = Button(root,text="cos",width=5,bd=5,command=lambda:self.PutButtonValues('cos(')).grid(row=7,column = 1,padx = 2)
        
        buttonPie = Button(root,text="PI",width=5,bd=5,command=lambda:self.PutButtonValues('pi')).grid(row=7,column=2,padx=2)
        # math.pi will give the value of constant pie i.e. 3.142

    
    @staticmethod
    def PutButtonValues(numbers):
    
    
        # the values entered will be appended into value list
        calc.value.append(str(numbers))
        
        #    now we have converted the list into a string and put it into entry widget
        calc.entry_instance.set(''.join(calc.value))
        
        
    #    method to delete the last digit
    def delLast(self):
        
        try:
            #    this will delete the last element of the list
            calc.value.pop()
            calc.entry_instance.set(''.join(calc.value))
            #    this button will clear off the last element that the user might have entered by mistake
            #    so instead of clearing off the entire string, lets clear only the last element
        except IndexError:
            # if the user gives pop() command even if the list is empty then this exception may occur
            #    so handled it
            pass
        
    def evaluate(self):
        
        self.ip=self.entry_instance.get()

        
        #    here eval() will evaluate the string that is present in entry widget
        #    exception handling is done for division by zero    
        for x in range(1,len(self.ip)):
            
            #    the user cannot use the operators for power only we can
            if(self.ip[x-1]==self.ip[x]=='*'):
                self.entry_instance.set("ERROR")
                break
            
        else:
            
            try:
                self.entry_instance.set(eval(self.ip))
            except ZeroDivisionError:
                self.entry_instance.set("INFINITY")
            except SyntaxError:
                self.entry_instance.set("ERROR")
            except NameError:
                self.entry_instance.set("ERROR")
            #    if infinity occurs and user does not clears then this exception handling will take care
            
            
    def clear(self):
        #    this will empty the list
        self.value=['']
        #    and display nothing on screen
        self.entry_instance.set(''.join(calc.value))
        
# let's create a root window
root=Tk()

# object of class Calculator
calc=Calculator(root)

root.mainloop()
        