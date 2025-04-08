# PYTHON PROJECTS (Easy)

**Python projects for academic purposes and also for learning how this language works.**


#NOT_COMMERCIAL


_Clean , readbale code and **explaination available** for the entire code in the readme file of each code_


This is a simple project made just for academic purposes such as projects etc..



****1. WEATHER APPLICATION (ALONG WITH SOME OTER FUCNTIONS WHICH ARE TERMINAL BASED)****


Dependencies :

- geopy

  `pip install geopy`

- pytz

  `pip install pytz`

- timezonefinder

  `pip install timezonefinder`

- requests

  `pip install requests`

  - some UI files
 
    `Included in the .rar file`




 ```python

from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import datetime
import time
import requests
import pytz
import math
import sys
import random
import string

#--------------Console Features--------------#



intro='''
  ------------------------------------------------------

   -------- B   .   A   .   S   .   I   .   X ----------
   
  ------------------------------------------------------
  

  ADDITIONAL FEATURES
  *-----------------------------------*

  1.Calculator
  
  2.Password Generator
  
  3.Hangman Game

  4.Weather App

  5.Help'''

for i in intro:
    
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)

print()
print()
print("------------------------------------------------------")
print()

user_choice=int(input("  What would you like to do? : "))
print()
print()



def calculator():
    
    print("Select operation.")
    print("-----------------------")
    print("1.Add")
    print()
    print("2.Subtract")
    print()
    print("3.Multiply")
    print()
    print("4.Divide")
    print()
    print("5.Square root")
    print()

    while True:
        
        
        choice = int(input("Enter choice : "))
        print()
        

        


        if choice ==1:
            
            a = float(input("Enter first number: "))
            print()
            b = float(input("Enter second number: "))
            print()
            
            print(a, "+", b, "=", a+b)

        elif choice ==2:
            
            a = float(input("Enter first number: "))
            print()
            b = float(input("Enter second number: "))
            print()
            
            print(a, "-", b, "=", a-b)

        elif choice ==3:
            
            a = float(input("Enter first number: "))
            print()
            b = float(input("Enter second number: "))
            print()
            print(a, "*", b, "=", a*b)

        elif choice ==4:
            
            a = float(input("Enter first number: "))
            print()
            b = float(input("Enter second number: "))
            print()
            
            print(a, "/", b, "=", a/b)
            
        elif choice ==5:
            
            c=int(input("Enter number"))
            print()
                  
            print("Square root = " ,math.sqrt(c))
        else:
            print("ERROR")
            print()
            print("Enter valid choice")
            print()
            continue
        
        retry= input("Want to Continue?? (yes/no): ")
        print()
        if retry == "no":
            
            exit()
        else:
            calculator()

def game():
    


    words = ['rainbow', 'computer', 'science', 'programming','galaxy', 'mathematics', 'player', 'condition',
                    'reverse', 'jamaica', 'board', 'amusing', 'geography']


    word = random.choice(words)
    print()

    print("Make sure CAPS LOCK is off")
    print()
    print("Guess the characters")

    guesses = ''


    turns = 12


    while turns > 0:


            failed = 0


            for char in word:


                    if char in guesses:
                            print(char, end=" ")

                    else:
                            print("_")

                            failed += 1

            if failed == 0:
                

                    print("You Win")
                    print()

                    print("The word is: ", word)
                    print()
                    break


            print()
            guess = input("----guess a character-----: ")
            print()


            guesses += guess

            if guess not in word:

                    turns -= 1



                    print("*** Wrong ****")
                    print()

                    print("You have", + turns, 'more guesses')
                    print()

                    if turns == 0:
                        print()
                        print("*** You Loose ***")
                        print()
                

    retry= input("Want to Continue?? (yes/no): ")
    print()
    if retry == "no":
         
        exit()
    else:
        
        game()
    


def passwordgen():
    

    char = string.ascii_letters + string.digits
    


    length = int(input("Enter the length of the password: "))


    password = ''.join(random.choices(char, k=length))


    print("Your password is:", password)

    retry= input("Want to Continue?? (yes/no): ")
    if retry == "no":
         
        exit()
    else:
        
        passwordgen()
    
def Help():
    
    error_text='''
   #----------Data Analysis------------#


    PROJECT NAME: B.A.S.I.X

    ERROR - CODE: 001


    #-------Weather Application---------#

    > No issues with the code as per analysis.
    > Error resides to openweathermaps.org ;

    >>>>> Error code: 403 HTTP {Server side response error} {#----------Reasons----------#}
    
                                                        {Failed to authenticate API}
                                                    {Couldn't give a response back}


    >>>>> Error Code: Unknown {'Weather'} { Couldn't Identify the root cause of this error }


    >>>>> Error Code: API limit exceeded { Need an API replace for the app to work } '''

    for j in error_text:
        sys.stdout.write(j)
        sys.stdout.flush()
        time.sleep(0.01)

        api_reset='''
    -------Open BASIX.py-----------

    -------Replace Manually--------

    app_id="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d3497364cab839aaebaa3f774a5a4b66"
  
                                                                                                                                       |-------------------Replace this------------------|'''
    for k in api_reset:
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(0.01)




if user_choice==1:
    calculator()
elif user_choice==3:
    game()
elif user_choice==2:
    passwordgen()
elif user_choice==4:
    None
elif user_choice==5:
    Help()



def weather():


    #----------Weather Application----------#
        
    root=Tk()
    root.title("B . A . S . I . X")
    root.geometry("900x500+300+200")
    root.resizable(False, False)
    root.configure(bg="#FFFFFF")
    appicon=PhotoImage(file="bing.png")
    root.iconphoto(False,appicon)


    def getweather():
        
        try:
            
            city=srcbox.get()
            geolocator=Photon(user_agent="trial")
            location=geolocator.geocode(city)
            obj=TimezoneFinder()
            result=obj.timezone_at(lng=location.longitude , lat=location.latitude)

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            print({city})


            app_id="d3497364cab839aaebaa3f774a5a4b66"


            api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}"
            
            json_data=requests.get(api).json()

            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind_speed = json_data['wind']['speed']
            temp_box.config(text=(temp,"°"))

               
            wind_box.config(text=wind_speed)
            pressure_box.config(text=pressure)
            moreinfo_box.config(text=description)

            
            
        except Exception as e:
            

            messagebox.showerror("Error", "City not found")
            messagebox.showerror("Error", "Try || Reset API || in the console")
            



    srcbar = PhotoImage(file="searchbar.png")
    img_bar = Label(image=srcbar, border=0)
    img_bar.place(x=10, y=10)

    srcbox = Entry(root, width=14, border=0, justify="center", font=("bahnschrift", 25), bg="#F0F0F0", fg="#000000")
    srcbox.place(x=40, y=13)

    srcicon = PhotoImage(file="searchicon.png")
    img_icon = Button(image=srcicon, borderwidth=0, cursor="hand2", border=0, bg="#F0F0F0", command=getweather)
    img_icon.place(x=300, y=15)

    s = PhotoImage(file="bottombox.png")
    l = Label(image=s, border=0)
    l.place(x=10,y=380)

    wind = Label(root, text="Wind", font=("bahnschrift", 20, 'bold'), fg="#FFFFFF", bg="#2A2A2A")
    wind.place(x=70, y=385)

    info = Label(root, text=" More Info", font=("bahnschrift", 20, 'bold'), fg="#FFFFFF", bg="#2A2A2A")
    info.place(x=370, y=385)

    pressure =Label(root, text="Pressure", font=("bahnschrift", 20, 'bold'), fg="#FFFFFF", bg="#2A2A2A")
    pressure.place(x=725, y=385)

    clock =Label(root, font=("bahnschrift", 20 ), bg="#FFFFFF")
    clock.place(x=770, y=10)

    clock_text = Label(root, text= "C U R R E N T   T I M E " ,font=("bahnschrift", 6, "bold"), bg="#2A2A2A",fg="#FFFFFF")
    clock_text.place(x=780,y=50)

    current_time=Label(root,font=("bahnschrift", 8 ), bg="#FFFFFF")
    current_time.place(x=780,y=0)


    temp_box=Label (font=("bahnschrift", 70, "bold"), fg="#2A2A2A",bg="#FFFFFF")
    temp_box.place(x=400,y=150)

    elab=Label (font=("bahnschrift", 15, 'bold'),fg="#2A2A2A",bg="#FFFFFF")
    elab.place(x=410,y=260)

    wind_box=Label(text="_ . _", font=("bahnschrift", 15, "bold"),justify="center", bg="#2A2A2A",fg="#FFFFFF")
    wind_box.place(x=80,y=435)

    moreinfo_box=Label (text="_ . _", font=("bahnschrift", 15, "bold"), bg="#2A2A2A",fg="#FFFFFF")
    moreinfo_box.place(x=410,y=435)

    pressure_box=Label(text="_ . _", font=("bahnschrift", 15, "bold"),justify="center", bg="#2A2A2A",fg="#FFFFFF")
    pressure_box.place(x=770,y=435)


    root.mainloop()



if user_choice==4:
    
    weather()

```







****2. To-Do List using python and mysql connectivity****


Dependencies :

- mysql connector

  `pip install mysql-connector-python`





```python

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

```
