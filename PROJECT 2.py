#--------------------------------------------- TO DO LIST ----------------------------------------------------------#


import mysql.connector as sql

def connection():
    try:
        print()
        print("Enter Your Password For Mysql Server !")
        print()

        password=input("ENTER HERE >>> ")

        global database

        database=sql.connect(host='localhost',user='root',password=f'{password}')

        global cursor

        cursor=database.cursor()

        #----Connection Establishing Module----#

        if database.is_connected():
            print("CONNECTION STATUS : SUCCESSFUL")
            print()

        else:
            sql.connect(host='localhost',user='root',passwd=password)

    except:
        print("ERROR : CANNOT CONNECT TO SERVER")
        print()
        print("WRONG MYSQL SERVER PASSWORD !!")
        print()
        connection()
connection()


#----User Redirecting Module----#

def user_redirect():

    print("How Would You Like To Continue ?")
    print()

    print("1. New User")
    print()
    print("2. Existing User")
    print()
    redir=input("Choice >>>> ")
    
    if redir=='1':
        new_user()

    if redir=='2':
        existing_user()

    else:
        print("Invalid Choice, Please Try Again...")
        user_redirect()
    
#----NEW USER MODULE----#

def new_user():

    db=input("Enter Here >>>> ")

    try:
        cursor.execute(f"CREATE DATABASE {db}")
    except:
        print("Database Already Exists...")
        print()
        print("Enter a Different Name For Your Database....!!!!")
        print()
        new_user()
    
    print("Database Created Successfully...")
    print()
    database.commit()

    # >Database-creation< #

    cursor.execute(f"USE {db}")
    
    cursor.execute("""Create table PLANNER(ID int PRIMARY KEY , ACTIVITY varchar(255) , 
                   DATE date , STATUS boolean)""")
    database.commit()

    user_redirect()

#----SEGREGATOR----#

def segregator():

    cursor.execute("SELECT * FROM PLANNER")

    entry_data=cursor.fetchall()

    global id
    global activity
    global date
    global status
            
    id=[]
    activity=[]
    date=[]
    status=[]

    for k in entry_data:
        id.append(k[0])
        activity.append(k[1])
        date.append(k[2])
        status.append(k[3])

#----User-Input Module----#
    
def data_input():

    number=int(input("How Many Entries Would like to Have ? >>> "))

    for i in range(0,number):

        activity_=input("Enter Activity / Habbit >>> ")

        date_=input("Enter Date -- YYYY/MM/DD >>> ")

        status_=input("Enter Status of the Activity(Done / Not Done) >>> ")
        
        if status_.lower()!='done' and status_.lower()!='not done':
            print("Invalid Status, Please Enter 'Done' or 'Not Done'...")
            print()
            i-=1
            continue

        if status_.lower()=='done':
            status_value=1
        
        elif status_.lower()=='not done':

            status_value=0

        segregator()

        if len(id) > 0:
            i = id[-1] + 1
        else:
            i = 1 
                
        cursor.execute(f"INSERT INTO PLANNER (ID, ACTIVITY, DATE, STATUS) VALUES ({i}, '{activity_}', '{date_}', '{status_value}')")
    
    database.commit()

    print()
    print("Taking You to Extisting User Interface !")
    print()

    existing_user()
#----EXISTING USER MODULE----#

def existing_user():

    user_db=input("Enter your Username / Database >>> ")

    try:
    
        cursor.execute(f"Use {user_db}")

    except:
        print("Database Does Not Exist...")
        print()
        print("Enter a Valid Database Name....!!!!")
        print()
        existing_user()

    print("How Would You Like To Continue ?")
    print()
    print("1. View All Entries")
    print()
    print("2. Add New Entries")
    print()
    print("3. Delete Entries")
    print()
    print("4. Update Entries")
    print()
    print("5. Exit")

    print()
    print()

    redir_input=int(input("Enter Your Choice Here >> "))
    
    if redir_input==1:
            
        segregator()

        token=0

        for i in id:


            print(f'''--------------------------------------------------
| {id[token]}        {activity[token]}       {date[token]}     {status[token]}       |  
--------------------------------------------------''')

            token+=1
        
        print()
        print("Taking You Back To Existing User Interface !")
        print()
        existing_user()
        




    elif redir_input==2:

        data_input()

    
    elif redir_input==3:

        while True:
            
            del_id=int(input("Enter the ID of the Entry You Want to Delete >>> "))
            
            cursor.execute(f"SELECT * FROM PLANNER WHERE ID={del_id}")
            
            if cursor.fetchone() is None:
                print("Entry Does Not Exist...")
                print()
                continue
            
            else:
                cursor.execute(f"DELETE FROM PLANNER WHERE ID={del_id}")
                
                database.commit()
                print("Entry Deleted Successfully...")
                print()
                
            loop=input("Would you like to Delete More Entries ? >>>")

            if loop!='yes':
                break
        
        database.commit()

        print()
        print("Taking You To Existing User Interface !")
        print()
        existing_user()
        
    elif redir_input==4:
        
        while True:
            
            update_id=int(input("Enter the ID of the Entry You Want to Update >>> "))
            
            cursor.execute(f"SELECT * FROM PLANNER WHERE ID={update_id}")
            
            if cursor.fetchone() is None:
                print("Entry Does Not Exist...")
                print()
                continue
            
            else:

                update=input("What Do You Want To Update ? >> ")

                if update.lower()=='activity':

                    new_activity=input("Enter New Activity >>> ")
                    cursor.execute(f"UPDATE PLANNER SET ACTIVITY='{new_activity}' WHERE ID={update_id}")

                elif update.lower()=='date':
                    
                    new_date=input("Enter New Date -- YYYY/MM/DD >>> ")
                    cursor.execute(f"UPDATE PLANNER SET DATE='{new_date}' WHERE ID={update_id}")

                elif update.lower()=='status':
                    
                    new_status=input("Enter New Status of the Activity(Done / Not Done) >>> ")
                    cursor.execute(f"UPDATE PLANNER SET STATUS='{new_status}' WHERE ID={update_id}")

                else:
                    print()
                    print("Invalid Choice...")
                    print()
                    continue
                
                database.commit()
                print("Entry Updated Successfully...")
                print()
                print("Taking You To Existing User Interface !")
                print()

    elif redir_input==5:

        database.close()
        exit()
    

user_redirect()


        
        

    







        
    








    

    




    


















