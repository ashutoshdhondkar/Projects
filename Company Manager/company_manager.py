'''
    @author: Ashutosh Dhondkar
    @created_on : 17th September,2018
    
'''

from abc import ABC,abstractmethod
import pymysql as sql
import os
# abstract class Employee
class Employee(ABC):
    @abstractmethod
    def __init__(self,first_name,last_name,dob,address,phone,dept_id):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.dept_id = dept_id
        
# function to connect to database
def Database():
    try:
        conn = sql.connect('localhost','root','','company_manager')
        curr = conn.cursor()
    except Exception:
        print("Something went wrong")
    else:
        return conn,curr        

@abstractmethod
def InsertIntoEmployee(first_name,last_name,dob,address,phone,dept_id,emp_type,salary):
    insert_employee_sql = f''' 
                    insert into employee(first_name,last_name,dob,address,phone,dept_id,emp_type)
                    values(
                    '{first_name}','{last_name}','{dob}','{address}','{phone}',
                    {dept_id},'{emp_type}'
                    );
     '''
    
    conn,curr = Database()
    try:
        curr.execute(insert_employee_sql)
        conn.commit()
    except Exception as e:
        print("Phone number already in use...")
        conn.rollback()
    else:
        
        curr.execute(f'select emp_id from employee where phone = {phone}')
        res = curr.fetchall()
        emp_id = res[0][0]
        insert_salary = f'''
            insert into permanent_emp(emp_id,salary) values({emp_id},{salary});
        '''
        try:
            curr.execute(insert_salary)
            conn.commit()
        except Exception as e:
            print(e)
            print("Something went wrong")
            conn.rollback()
        else:
            works_query = f'''
                insert into works_in(dept_id,emp_id) values({dept_id},{emp_id});
            '''
            try:
                curr.execute(works_query)
                conn.commit()
            except Exception as e:
                print("Something went wrong")
                print(e)
                conn.rollback()
            else:
                print("\t\t\tEmployee hired successful")

    finally:
        conn.close()
        
        
# table name : permanent_emp(id,emp_id,salary)
class SalariedEmloyee(Employee):
    
    def __init__(self,first_name,last_name,dob,address,phone,dept_id,salary):
        super().__init__(first_name,last_name,dob,address,phone,dept_id)
        self.salary = salary
        self.emp_type = 'Salaried'     
    
        InsertIntoEmployee(self.first_name,self.last_name,self.dob,self.address,
                                self.phone,self.dept_id,self.emp_type,self.salary)
        
# table name : permanent_emp(id,emp_id,salary)
class Manager(Employee):
    def __init__(self,first_name,last_name,dob,address,phone,dept_id,salary):
        super().__init__(first_name,last_name,dob,address,phone,dept_id)
        self.salary = salary
        self.emp_type = 'manager'
        
        InsertIntoEmployee(self.first_name,self.last_name,self.dob,self.address,
                                self.phone,self.dept_id,self.emp_type,self.salary)

        

# table name : permanent_emp(id,emp_id,salary)
class Executive(Employee):
    def __init__(self,first_name,last_name,dob,address,phone,dept_id,salary):
        super().__init__(first_name,last_name,dob,address,phone,dept_id)
        self.salary = salary
        self.emp_type = 'executive'
        
        # insert into table
        InsertIntoEmployee(self.first_name,self.last_name,self.dob,self.address,
                                self.phone,self.dept_id,self.emp_type,self.salary)

# table name : contract_emp(id,emp_id,total_hours,hourly_wages)
class HourlyEmployee(Employee):
    def __init__(self,first_name,last_name,dob,address,phone,dept_id,total_hours,hourly_wages):
        super().__init__(first_name,last_name,dob,address,phone,dept_id)
        self.total_hours = total_hours
        self.hourly_wages = hourly_wages
        self.emp_type = 'contract labours'
        
    def InsertContractLabours(self):
        insert_employee_sql = f''' 
                    insert into employee(first_name,last_name,dob,address,phone,dept_id,emp_type)
                    values(
                    '{self.first_name}','{self.last_name}','{self.dob}','{self.address}','{self.phone}',
                    {self.dept_id},'{self.emp_type}'
                    );
         '''
    
        conn,curr = Database()
        try:
            curr.execute(insert_employee_sql)
            conn.commit()
        except Exception as e:
            print("Phone number already in use...")
            conn.rollback()
        else:
            
            curr.execute(f'select emp_id from employee where phone = {self.phone}')
            res = curr.fetchall()
            emp_id = res[0][0]
            insert_salary = f'''
                insert into contract_emp(emp_id,total_hours,hourly_wages,salary) values({emp_id},{self.total_hours},
                {self.hourly_wages},{self.total_hours*self.hourly_wages});
            '''
            try:
                curr.execute(insert_salary)
                conn.commit()
            except Exception as e:
                print(e)
                print("Something went wrong")
                conn.rollback()
            else:
                works_query = f'''
                    insert into works_in(dept_id,emp_id) values({self.dept_id},{emp_id});
                '''
                try:
                    curr.execute(works_query)
                    conn.commit()
                except Exception as e:
                    print("Something went wrong")
                    print(e)
                    conn.rollback()
                else:
                    print("\t\t\tEmployee hired successful")
    
        finally:
            conn.close()

class Company():
    def Hire_employee(self):
        
        print("\tSelect employee type : ")
        print("\t1: Manager")
        print("\t2: Executive")
        print("\t3: Salaried employee")
        print("\t4: Hourly employee")
        choice = int(input("\tEnter your choice >>>"))
        print("\t\tSelect department")
        print("\t\t1: Finance")
        print("\t\t2: Production")
        print("\t\t3: Marketing")
        print("\t\t4: Service")
        dept_id = int(input("\t\tEnter your choice >>> "))
            
        if(choice == 1):
#           Manager()
            salary = int(input("\t\t\tEnter salary : "))
            first_name,last_name,dob,address,phone = Emp_Info()
            obj = Manager(first_name,last_name,dob,address,phone,dept_id,salary)           
            del obj
            
        elif(choice == 2):
            # Executive()
            salary = int(input("\t\t\tEnter salary : "))
            first_name,last_name,dob,address,phone = Emp_Info()
            obj = Executive(first_name,last_name,dob,address,phone,dept_id,salary)
            del obj
    
        elif(choice == 3):
            # SalariedEmployee()
            salary = int(input("\t\t\tEnter salary : "))
            first_name,last_name,dob,address,phone = Emp_Info()
            obj = SalariedEmloyee(first_name,last_name,dob,address,phone,dept_id,salary)
            del obj
        
        elif(choice == 4):
            # HourlyEmployee()
            total_hours = int(input("\t\t\tEnter total hours of work : "))
            hourly_wages = int(input("\t\t\tEnter hourly wages : "))
            first_name,last_name,dob,address,phone = Emp_Info()
            obj = HourlyEmployee(first_name,last_name,dob,address,phone,dept_id,total_hours,hourly_wages)
            obj.InsertContractLabours()
            del obj
            
        else:
            print("Wrong choice")
    def Fire_employee(self):
        emp_id = int(input("\tEnter employee id to be fired :"))
        conn,curr = Database()
        select_sql = f'''
            select employee.first_name,employee.last_name,employee.emp_type,
            department.dept_name from employee,department where employee.dept_id = department.dept_id and
            employee.emp_id = {emp_id};
        '''
        try:
            curr.execute(select_sql)
            res = curr.fetchall()
        except Exception as e:
            print(e)
        else:
            print("\tDetails".center(40))
            print("\tFull name : ".ljust(20) + str(res[0][0]+"  "+res[0][1]).ljust(20))
            print("\tType : ".ljust(20) + res[0][2].ljust(20))
            print("\tDepartment : ".ljust(20)+res[0][3].ljust(20))
            
            choice = input("\tAre you sure(y/n) ? : ").lower()
            if(choice == 'y'):
                delete_sql = f'''
                    delete from employee where emp_id = {emp_id};,
                    delete from contract_emp where emp_id = {emp_id};, 
                    delete from permanent_emp where emp_id = {emp_id};,
                    delete from works_in where emp_id = {emp_id};
                '''
                 
                for x in delete_sql.split(','):
                    x = x.replace('\n','').strip()
                    try:
                        curr.execute(x)
                        conn.commit()
                    except Exception as e:
                        print(e)
                        conn.rollback()
                else:
                    print("\t\tEmployee fired successfully")    
                    conn.close()
            
#         
    def Raise_employee(self):
        emp_id = int(input("\tEnter employee id for hike raise : "))
        
        select_sql = f"select emp_type from employee where emp_id = {emp_id};"
        
        conn,curr = Database()
        try:
            curr.execute(select_sql)
            res = curr.fetchall()
        except Exception as e:
            print(e)
        else:
            if(res[0][0] == 'contract labours'):
                select_sql = f'''
                    select employee.first_name,employee.last_name,employee.emp_type,
                    department.dept_name,contract_emp.hourly_wages,contract_emp.total_hours
                    from employee,department,contract_emp where 
                    employee.dept_id = department.dept_id and employee.emp_id = {emp_id};
                '''
                try:
                    curr.execute(select_sql)
                    res = curr.fetchall()
                
                    print("\tDetails".center(40))
                    print("\tFull name : ".ljust(40) + str(res[0][0]+"  "+res[0][1]).ljust(20))
                    print("\tType : ".ljust(40) + res[0][2].ljust(20))
                    print("\tDepartment : ".ljust(40)+res[0][3].ljust(20))
                    print("\tCurrent Hourly Salary : ".ljust(40)+str(res[0][4]).ljust(20))
                except Exception :
                    print("No user found")    
                else:
                    choice = input("\tAre you sure(y/n) ? : ").lower()
                    if(choice == 'y'):
                        new_sal = int(input("\tEnter new hourly salary : "))
                        salary = new_sal * res[0][5]
                        print(salary)
                        update = f'''update contract_emp set hourly_wages = {new_sal} ,
                            salary = {salary}  where emp_id = {emp_id};'''
                        try:
                            curr.execute(update)
                            conn.commit()
                        except Exception as e:
                            print(e)
                            conn.rollback()
                            print("Something went wrong")
                        else:
                            print("\t\tSalary updated successfully!")
                        finally:
                            conn.close()
            else:
                select_sql = f'''
                    select employee.first_name,employee.last_name,employee.emp_type,
                    department.dept_name,permanent_emp.salary from employee,department,permanent_emp where employee.dept_id = department.dept_id and
                    employee.emp_id = {emp_id};
                '''
                try:
                    curr.execute(select_sql)
                    res = curr.fetchall()
                except Exception as e:
                    print(e)
                else:
                    print("\tDetails".center(40))
                    print("\tFull name : ".ljust(20) + str(res[0][0]+"  "+res[0][1]).ljust(20))
                    print("\tType : ".ljust(20) + res[0][2].ljust(20))
                    print("\tDepartment : ".ljust(20)+res[0][3].ljust(20))
                    print("\tCurrent Salary : ".ljust(20)+str(res[0][4]).ljust(20))
                    
                    choice = input("\tAre you sure(y/n) ? : ").lower()
                    if(choice == 'y'):
                        new_sal = int(input("\tEnter new salary : "))
                        update = f"update permanent_emp set salary = {new_sal} where emp_id = {emp_id};"
                        try:
                            curr.execute(update)
                            conn.commit()
                        except Exception as e:
                            print(e)
                            conn.rollback()
                            print("Something went wrong")
                        else:
                            print("\t\tSalary updated successfully!")
                        finally:
                            conn.close()
# function to ask for details of new employee
def Emp_Info():
    first_name = input("\t\t\tEnter first name : ")
    last_name = input("\t\t\tEnter last name : ")
    dob = input("\t\t\tEnter date of birth (dd/mm/yyyy) : ")
    address = input("\t\t\tEnter address : ")
    phone = input("\t\t\tEnter phone number : ")
    
    return (first_name,last_name,dob,address,phone)


def main():
    while(True):
        print("Welcome to ABC Company".center(100,'-'))
        print("1: Hire new employee")
        print("2: Fire employee")
        print("3: Raise employee")
        print("4: Clear Screen")
        print("5: exit")
        choice = int(input("Enter your choice >>>"))
        print("".center(100,'*'))
        obj = Company()
        if(choice == 1):
            obj.Hire_employee()
        elif(choice == 2):
            obj.Fire_employee()
        elif(choice == 3):
            obj.Raise_employee()
        elif(choice == 4):
            os.system('clear')
        elif(choice == 5):
            print("Thank you".center(100,'-'))
            break
        else:
            print("Invalid choice")
        
            
if __name__ == '__main__':
    main()
        