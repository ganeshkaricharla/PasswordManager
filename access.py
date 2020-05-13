from hash import hashcount
from emailmgr import send_email
from accounts import *

import os
def signup():
    usr_email=input('Gmail')
    usr_name=input('Name')
    pwd=usr_name+'@'+hashcount(usr_name)+hashcount(usr_email)
    status=send_email(usr_email,usr_name,pwd)
    if status=="OK":
        print("The Details has been sent to "+usr_email)
    with open("pwdmanager.csv",'a') as file:
        file.write(usr_email+','+pwd+','+usr_name+','+'a')
        file.write('\n')
    os.system('cls')
    print('Your Account is Ready to USE!!\n Happy Login :\)')


def login():
    usr_email=input("Email:")
    with open("pwdmanager.csv") as file:
        for i in file.readlines():
            li=i.split(",")
            if li[0]==usr_email:
                code=input("Passcode :")
                if code==li[1]:
                    mainControl(li[0],li[2])
                else:
                    print("password isn't matching correctly")            
            else:
                print("Username not found create an account")
                
                
def AccessControl():
    print('1.{}\n2.{}'.format("Login","SignUP"))
    choice=int(input('\n\nEnter the choice-->'))
    os.system('cls')
    if choice ==1:
        login()
    elif choice ==2:
        signup()
    

AccessControl()
    