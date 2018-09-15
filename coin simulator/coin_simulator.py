'''
    @author : Ashutosh Dhondkar
    Created on : 14th September 2018
    
'''

import tkinter as tk
from tkinter import messagebox as msg
import random as r
from PIL import ImageTk,Image
from playsound import playsound
class CoinFlip():
    # list to count number of occurrences
    listOfData = []
    def __init__(self,root):
        self.root = root
        self.back = '#a8e6cf'
        self.root['bg'] = self.back
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0')
        self.root.title("Coin Flip Simulation")
        self.FrontEnd()
        self.root.mainloop()
    
    def FrontEnd(self):
        
        tk.Label(self.root,text="Welcome to coin flip simulator",bg=self.back,font=('Bookman old style',30,'bold italic underline')).pack(side=tk.TOP,pady=20)
        tk.Label(self.root,text= "Select Option for each player",bg=self.back,font=('Normal',25,'bold'),pady=20).pack(side = tk.TOP)
         
        tk.Label(self.root,text = "Player 1 : ",bg=self.back,font=('Normal',20,'bold')).place(x=500,y=200)
    
#         self.MidFrame = tk.Frame(self.root,bg = self.back).pack(side = tk.TOP)
        self.choice = ['Heads','Tails']
        
        # created for player 1
        self.player1 = tk.Spinbox(self.root,width=10,values=self.choice,font=('Normal',20),justify = 'center',bd=5,
                             state = 'readonly')
        self.player1.place(x = 650,y=200)
        
        # created for player 2
        tk.Label(self.root,text = "Player 2 : ",bg=self.back,font=('Normal',20,'bold')).place(x=500,y=300)
        self.player2 = tk.Spinbox(self.root,width=10,values=self.choice,font=('Normal',20),justify = 'center',bd=5,
                             state = 'readonly')
        self.player2.place(x = 650,y=300)
        
        # enter number of trials
        tk.Label(self.root,text = "Number of Trials : ",bg=self.back,font=('Normal',20,'bold')).place(x=380,y=400)
        self.iterations = tk.Entry(self.root,font = ('Normal',20),justify='center',width=11,bd=5)
        self.iterations.place(x = 650,y=400)
        
        # create a button to go to main game
        self.gobutton = tk.Button(self.root,text="PLAY!",width=30,font=('Normal',20),bg="#64a1f4",bd=5,activebackground = "red",
                                  command = self.CheckValidity)
        self.gobutton.place(x = 450,y=500)
        
        # create copyright label
        tk.Label(self.root,text = "(C) Copyright 2018",font = ('Monotype Corsiva',30,'bold'),bg=self.back).pack(side = tk.BOTTOM,pady=50)
        

    def CheckValidity(self):
        
        
        if(self.player1.get() != self.player2.get()):
            # msg.showerror('ERROR', "Both the players cannot select same option")
            if(self.iterations.get() == None):
                msg.showerror('ERROR', 'please enter number of trials')
            else:
                try:
                    self.iterations = int(self.iterations.get())
                except Exception:
                    msg.showerror('ERROR','Please enter integer only')
                else:
                    # if it is successfull then call the simulation
#                     msg.showinfo('','success')
                    self.player1 = self.player1.get()
                    self.player2 = self.player2.get()
                    self.MainGame()
        else:
            msg.showerror('ERROR', "Both the players cannot select same option")
            
    # The main game begins here
    def MainGame(self):
        self.root.destroy()
        self.newroot = tk.Tk()
        self.newroot.geometry(f"{self.newroot.winfo_screenwidth()}x{self.newroot.winfo_screenheight()}+0+0")
        self.newroot['bg'] = self.back
        self.newroot.title('Coin Flip Simulator')
        self.itercopy = self.iterations
        
        self.NewFrontEnd()
        
        self.newroot.mainloop()
        
    def NewFrontEnd(self):
        self.label = tk.StringVar()
        tk.Label(self.newroot,bg=self.back,textvariable = self.label,font=('Normal',30,'bold italic underline')).place(x = 500,y=10)
        
        if(self.iterations == self.itercopy):
            self.label.set(f"Iterations left = { '0' + str(self.iterations) if(self.iterations <10) else (self.iterations)}")
            self.iterations -= 1
            butt = tk.Button(self.newroot,text="TOSS!",width=30,font=('Normal',20),bg="#64a1f4",bd=5,activebackground = "red",
                                      command = self.NewFrontEnd)
            butt.place(x = 430,y=300)
        elif(self.iterations>0):
            self.label.set(f"Iterations left = { '0' + str(self.iterations) if(self.iterations <10) else (self.iterations)}")
            op = r.randint(0,1)
            if(op == 0):
                self.path = 'tails.png'
                CoinFlip.listOfData.append(0)
            elif(op == 1):
                self.path = 'heads.png'
                CoinFlip.listOfData.append(1)
            playsound('coinflip.mp3')
            self.img = Image.open(self.path)
            self.img = self.img.resize((150,150),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)
            tk.Label(self.newroot,image = self.img,bd=5).place(x = 600,y=100)
            self.iterations -= 1
            butt = tk.Button(self.newroot,text="TOSS!",width=30,font=('Normal',20),bg="#64a1f4",bd=5,activebackground = "red",
                                      command = self.NewFrontEnd)
            butt.place(x = 430,y=300)
        elif(self.iterations==0):
            self.label.set(f"Iterations left = { '0' + str(self.iterations) if(self.iterations <10) else (self.iterations)}")
            op = r.randint(0,1)
            if(op == 0):
                self.path = 'tails.png'
                CoinFlip.listOfData.append(0)
            elif(op == 1):
                self.path = 'heads.png'
                CoinFlip.listOfData.append(1)
            playsound('coinflip.mp3')
            self.img = Image.open(self.path)
            self.img = self.img.resize((150,150),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)
            tk.Label(self.newroot,image = self.img,bd=5).place(x = 600,y=100)

            butt = tk.Button(self.newroot,text="TOSS!",width=30,font=('Normal',20),bg="#64a1f4",bd=5,activebackground = "red",
                                    command = self.NewFrontEnd,state='disable')
            butt.place(x = 430,y=300)
            tk.Label(self.newroot,text='Summary',bg=self.back,font=('Bookman old style',30,'bold italic underline')
                         ).place(x = 570,y=400)
            tk.Label(self.newroot,text='Heads',bg=self.back,font=('Normal',20,'bold')).place(x = 500,y=500)
            tk.Label(self.newroot,text='Tails',bg=self.back,font=('Normal',20,'bold')).place(x = 800,y=500)
            tk.Label(self.newroot,text=CoinFlip.listOfData.count(1),bg=self.back,font=('Normal',20,'bold')).place(x = 520,y=550)
            tk.Label(self.newroot,text=CoinFlip.listOfData.count(0),bg=self.back,font=('Normal',20,'bold')).place(x = 820,y=550)
            self.foot = tk.StringVar()
            tk.Label(self.newroot,textvariable = self.foot,bg=self.back,font = ('Bookman old style',30,'bold italic underline')).pack(side = tk.BOTTOM,pady=60)
            if(CoinFlip.listOfData.count(1) == CoinFlip.listOfData.count(0)):
                self.foot.set("It's a Tie")
                msg.showinfo('','Tie')
            elif(CoinFlip.listOfData.count(1) > CoinFlip.listOfData.count(0)):
                if(self.player1 == 'Heads'):
                    self.foot.set("winner : Player 1")
                    msg.showinfo('','player 1 won')
                elif(self.player2 == 'Heads'):
                    self.foot.set("winner : Player 2")
                    msg.showinfo('','player 2 won')
            elif(CoinFlip.listOfData.count(0) > CoinFlip.listOfData.count(1)):
                if(self.player1 == 'Tails'):
                    self.foot.set("winner : Player 1")
                    msg.showinfo('','player 1 won')
                elif(self.player2 == 'Tails'):
                    self.foot.set("winner : Player 2")
                    msg.showinfo('','player 2 won')
            
            print(CoinFlip.listOfData)
def main():
    root = tk.Tk()
    
    obj = CoinFlip(root)
    
if __name__ == '__main__':
    main()
    