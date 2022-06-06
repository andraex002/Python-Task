import mysql.connector
 

con = mysql.connector.connect(
    host="localhost", user="root", password="Denisalore100", database="task_python")
 

def Add_user():
 
    id = input("Enter userid : ")
     
    
    if(check_user(id) == True):
        print("User aready exists\nTry Again\n")
        menu()
         
    else:
        name = input("Enter Department name : ")
        user = input("Enter User id : ")
        
        
        data = (id, name, user)
     
       
        sql = 'insert into department values(%s,%s,%s)'
        c = con.cursor()
         
        
        c.execute(sql, data)
         
        
        con.commit()
        print("User was added")
        menu()
 



def Remove_user():
    id = input("Enter User Id : ")
     
 
    if(check_user(id) == False):
        print("User does not  exists\nTry Again\n")
        menu()
    else:
         
        
        sql = 'delete from department where id=%s'
        data = (id,)
        c = con.cursor()
         
        
        c.execute(sql, data)
         
        
        con.commit()
        print("User Removed")
        menu()
 
 
def check_bonus(bonus_id):
     
  
    sql = 'select * from employer where id=%s'
     
   
    c = con.cursor(buffered=True)
    date = (bonus_id,)
     
    
    c.execute(sql, date)
     
 
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

 
def salarybonus():

    id = int(input("Enter Employ's Id"))
     
    
    if(check_bonus(id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
         
       
        sql = 'select salary from employer where id=%s'
        date = (id,)
        c = con.cursor()
         
        
        c.execute(sql, date)
         
        
        r = c.fetchone()
        t = r[0]+Amount
         
        
        sql = 'update employer set salary=%s where id=%s'
        d = (t, id)
         
       
        c.execute(sql, d)
         
        
        con.commit()
        print("Employee Bonus=", t)
        menu()

def check_user(user_id):
     
  
    sql = 'select * from department where id=%s'
     
   
    c = con.cursor(buffered=True)
    data = (user_id,)
     
    
    c.execute(sql, data)
     
 
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

 
        
def menu():
    print("Manage some random company employer")
    print("Press ")
    print("1 to Add User")
    print("2 to Remove User ")
    print("3 to Salary Bonus")
    
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_user()
    elif ch == 2:
        Remove_user()
    elif ch == 3:
        salarybonus()
    
    else:
        print("Invalid Choice")
        menu()
 

menu()
