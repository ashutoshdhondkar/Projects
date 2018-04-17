import threading
import time


# let's create a class wherin all the methods will be stored
class SleepingBarber:
    numberOfSeatsAvailable = 5  #    total number of seats available
    
    seat = 0  # this is the value which will tell us whether there is any customer getting an haircut
    
    def IsBarberBusy(self):
        if(SleepingBarber.seat == 0):
            return 1
        elif(SleepingBarber.seat == 1):        
            return  0
    
    # This method will be taken by thread    
    def ProcessCustomer(self):
        if(SleepingBarber.seat == 1):
            time.sleep(5)
            SleepingBarber.seat = 0  
            #    Then it will take in new customer so number of seats available will increase by 1
            #    but here as we are using this method in threading so there is a possibility that 
            #    number of seat available value may change as we are updating it in two methods
            #    so it's better to use Lock()
            SleepingBarber.lock = threading.Lock()
            
            with SleepingBarber.lock:
                if(SleepingBarber.numberOfSeatsAvailable > 0 and SleepingBarber.numberOfSeatsAvailable <5):
                    # there is someone waiting for haircut
                    # then if seat == 0 then decrease the value of SleepingBarber.numberOfSeatsAvailable by 1
                    # now since seat == 0 as we have written it , then there is no need to check value of seat again
                    SleepingBarber.numberOfSeatsAvailable += 1
                    SleepingBarber.seat =1
                    
    
    @staticmethod
    def EnterCustomer():
        if(SleepingBarber.numberOfSeatsAvailable>0 and  SleepingBarber.numberOfSeatsAvailable <= 5):
            if(cust.IsBarberBusy()):
                # if the barber is sleeping that means there is no customer waiting
                # so the currently entered user will go and sit on the chair for haircut and hence seat =1
                SleepingBarber.seat=1
            else:
                SleepingBarber.numberOfSeatsAvailable -=1   
                # This means that the barber is busy and hence the customer will have to wait
        else:
            print("The customer leaves as no seat is available")
            
            
cust = SleepingBarber()     # object of our class

while(1):
    print("********Main Menu*********")
    print("1. Check Barber Status")
    print("2. Enter Customer")
    print("3. View Number of seats available")

    print("**************************")
    choice = int(input("Enter your choice : "))
    

    
    # let's now initiate a thread
    
    #########################################################
    t = threading.Thread(target = cust.ProcessCustomer)
    if not(cust.IsBarberBusy()):
        t.start()
    #########################################################
        
        
    if(choice == 1):
        a=cust.IsBarberBusy()
        if(a==1):
            print("Barber is sleeping")
        elif(a==0):
            print("Barber is busy")
        
    elif(choice == 2):
        cust.EnterCustomer()
        
    elif(choice == 3):
        print("Available Seats = {}".format(SleepingBarber.numberOfSeatsAvailable))
        
        