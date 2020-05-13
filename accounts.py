from hash import encode_pwd,decode_pwd
def add_account(email,name):
    usr_service=input("Service Name")
    usr_Id=input("UserId")
    pwd=input("Password")
    with open("AccountsData.csv",'a')as file:
        file.write(email+','+name+','+usr_service+','+usr_Id+','+encode_pwd(pwd))
        file.write('\n')
        
def view_account(email):
    file=open("AccountsData.csv",'r')
    for i in file.readlines():
        li=i.split(',')
        if email==li[0]:
            show_account(li)
        else:
            continue

def show_account(li):
    print('Email    = {}\n'.format(li[0]))
    print('Name     = {}\n'.format(li[1]))
    print('Service  = {}\n'.format(li[2]))
    print('UserId   = {}\n'.format(li[3]))
    print('Password = {}\n'.format(decode_pwd(li[4])))
    
    
def del_account(service,usr_Id):
    list=[]
    with open("AccountsData.csv",'r') as f:
        for i in f.readlines():
            li=i.split(",")
            lis=[]
            for i in li:
                if '\n' in i:
                    i=i.replace('\n','')
                lis.append(i)
            list.append(lis)
    for i in list:
        if (service in i) and (usr_Id in i):
            list.remove(i)
    with open("AccountsData.csv",'w') as f:
        for i in list:
            f.write(i[0]+','+i[1]+','+i[2]+','+i[3]+','+i[4])

def mainControl(usr_email,usr_name):
    choice=int(input('enter choice'))
    if choice == 1:
        add_account(usr_email,usr_name)
    elif choice == 2:
        usr_service=input('Enter the service name')
        usr_Id=input('Enter the User Id to confirm Your deletion')
        del_account(usr_service,usr_Id)
    elif choice == 3:
        view_account(usr_email)
       
