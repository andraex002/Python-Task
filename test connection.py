import mysql.connector
 

con = mysql.connector.connect(
    host="localhost", user="root", password="Denisalore100", database="task_python")
 

def Add_Employ():
 
    id = input("Enter Employee id : ")
     
    
    if(check_employee(id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
         
    else:
        firstname = input("Enter Employee Firstname : ")
        lastname = input("Enter Employee Lastname : ")
        age = input("Enter Employee age : ")
        job = input("Enter Employee job : ")
        salary = input("Enter Employee salary : ")
        bonus = input("Enter Employee bonus : ")
        totalsalary = input("Enter Employee totalsalary : ")
        
        data = (id, firstname, lastname, age, job, salary, bonus, totalsalary)
     
       
        sql = 'insert into employer values(%s,%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
         
        
        c.execute(sql, data)
         
        
        con.commit()
        print("Employee Added Successfully ")
        menu()
 

def Bonus_Employee():
    id = int(input("Enter Employ's Id"))
     
    
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
         
       
        sql = 'select salary from employer where id=%s'
        data = (id,)
        c = con.cursor()
         
        
        c.execute(sql, data)
         
        
        r = c.fetchone()
        t = r[0]+Amount
         
        
        sql = 'update employer set salary=%s where id=%s'
        d = (t, id)
         
       
        c.execute(sql, d)
         
        
        con.commit()
        print("Employee Bonus")
        menu()
 

def Remove_Employ():
    id = input("Enter Employee Id : ")
     
 
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
         
        
        sql = 'delete from employer where id=%s'
        data = (id,)
        c = con.cursor()
         
        
        c.execute(sql, data)
         
        
        con.commit()
        print("Employee Removed")
        menu()
 
 

def check_employee(employee_id):
     
  
    sql = 'select * from employer where id=%s'
     
   
    c = con.cursor(buffered=True)
    data = (employee_id,)
     
    
    c.execute(sql, data)
     
 
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 

def Display_Employees():
     
    
    sql = 'select * from employer'
    c = con.cursor()
     
    
    c.execute(sql)
     
    
    r = c.fetchall()
    for i in r:
        print("Employee id : ", i[0])
        print("Employee Firstname : ", i[1])
        print("Employee Lastname : ", i[2])
        print("Employee Age : ", i[3])
        print("Employee Job : ", i[4])
        print("Employee Salary : ", i[5])
        print("---------------------\
        -----------------------------\
        ------------------------------\
        ---------------------")
         
    menu()
 
def salarybonus():

    id = int(input("Enter Employ's Id"))
     
    
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
         
       
        sql = 'select salary from employer where id=%s'
        data = (id,)
        c = con.cursor()
         
        
        c.execute(sql, data)
         
        
        r = c.fetchone()
        t = r[0]+Amount
         
        
        sql = 'update employer set salary=%s where id=%s'
        d = (t, id)
         
       
        c.execute(sql, d)
         
        
        con.commit()
        print("Employee Bonus=", t)
        menu()
def menu():
    print("Manage some random company employer")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Bonus")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Bonus_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        salarybonus()
    else:
        print("Invalid Choice")
        menu()
 

menu()
