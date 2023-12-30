import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root123",database="himanshu")
cur=conn.cursor()
# cur.execute("create table auth(name varchar(50) not null,email varchar(50) unique not null,contact bigint unique not null,password varchar(50) unique not null)")
# conn.commit()
# print("created")


def main():
    print("1.registration \n2.Login")
    choice=int(input("enter your choice "))
    if choice==1:
        reg()
    elif choice==2:
        log()
    else:
        print("select from the option")

def reg():
    print("#####REGISTRATION#####")
    while True:
        a=int()
        name=input("enter your name: ")
        for i in name:
            if(65<=ord(i)<=90 or 97<=ord(i)<=122):
                a=a+1
        if(a==len(name)):
            print(name)
            break
        else:
            print("enter valid name")

    while True:
        global email
        email=input("enter your email id: ")
        if email.endswith('@gmail.com'):
            print(email)
            break
        else:
            print('enter valid email id')

    while True:
        contact=input("enter your contact number: ")
       
        if len(contact)==10:
            print(contact)
            break
        else:
            print("enter valid contact number")
    
    while True:
        global password
        A,a,n,s=int(),int(),int(),int()
        print("your password must have atleast one upper case one lower case one special case character and at least one integer value")
        password=input("enter password: ")
        for i in password:
            if (65<=ord(i)<=90):
                A+=1
            elif(97<=ord(i)<=122):
                a+=1
            elif(48<=ord(i)<=57):
                n+=1
            elif(32<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126):
                s+=1
        if (A>=1 and a>=1 and n>=1 and s>=1):
                print(password)
                q="insert into auth(name,email,contact,password) values(%s,%s,%s,%s)"
                b=(name,email,contact,password)
                cur.execute(q,b)
                # if cur.rowcount==1:
                #     print("OK")
                # else:
                #     print("Wrong")
                conn.commit()
                print("Inserted")
                break
        else:
            print("enter valid password")

        
       
    log()

def log():
    print("#####LOGIN#####")
    email=(input("email: "))
    password=(input("password: "))
    cur.execute("select * from auth")

    #for i in cur:
    if email and password in cur:
        print("login successfull")
    else:
        print("enter valid email and password")
    

main()

