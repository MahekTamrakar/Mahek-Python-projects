#Project 3 Contact Book
#mysql connectivity
import mysql.connector as mycon
mydb = mycon.connect(host="localhost" , user="root" , password=" " )
mycur = mydb.cursor()
#creating database
mycur.execute("create database if not exists CB")
mycur.execute("use CB")
#creating table
mycur.execute("create table if not exists numbers(sno int NOT NULL PRIMARY KEY , name varchar(20) NOT NULL , number int(10) NOT NULL )")
mydb.commit()
#displaying choices
print("********** WELCOME TO YOUR CONTACT BOOK **********")
print("Press 1: For Add New Number")
print("Press 2: For Updatation")
print("Press 3: For Look Out All Numbers")
print("Press 4: For Look Out Any Particular Number")
print("Press 5: For Delete All Numbers")
print("Press 6: For Delete Any Particular Number")
print("-------------------------------------------")
press=int(input("Press Any Number: "))
#Choice 1
if press == 1:
    def add():
        sno=int(input("Enter Serial Number: "))
        name=input("Enter Name: ")
        number=int(input("Enter Contact Number: "))
        data=(sno, name, number)
        insert="insert into numbers values(%s, %s, %s)"
        mycur.execute(insert, data)
        mydb.commit()
        print("!!!!!!!!!! Contact Number Added Successfully !!!!!!!!!!")
    add()
#choice 2
elif press == 2:
#asking for what to be update
    ch=int(input("Press 1 For Update Name --- OR --- Press 2 For Update Number:- "))
#choice 1 for update name
    if ch == 1:
        def updatename():
            sno=int(input("Enter Serial Number Whose Name Shoud be Updated:  "))
            name=input("Enter New Name: ")
            upv=(name,sno)
            update = "update numbers set name = %s where sno = %s"
            mycur.execute(update,upv)
            mydb.commit()
            print("!!!!! Name Updated Successfully !!!!!")
        updatename()
#choice 2 for update number
    elif ch == 2 :           
        def updatecon():
            name=input("Enter Name Whose Number should be updated: ")
            number=input("Enter new Number: ")
            uv=(number, name)
            update="update numbers set number=%s where name=%s"
            mycur.execute(update, uv)
            mydb.commit()
            print("!!!!! Number Updated Successfully !!!!!" )
        updatecon()
#choice else for wrong input
    else :
        print("Wrong Input")
#choice 3
elif press == 3:
    def lookout():
        print("@@@@@@ Contacts in the Book are @@@@@@ ")
        mycur.execute("select * from numbers")
        for select in mycur.fetchall():
            print(select)
    lookout()
#choice 4
elif press == 4:
    def par_look():
        name = input("Enter Name Whose Number Should Lookout")
        val=(name,)
        par="select number from numbers where name = %s"
        mycur.execute(par, val)
        for select in mycur.fetchone():
            print(select)
    par_look()
#choice 5
elif press == 5:
    def delete():
        deleteall= "truncate table numbers"
        mycur.execute(deleteall)
        mydb.commit()
        print("!!!!! All Numbers are Deleted !!!!!")
    delete()
#choice 6
elif press == 6:
    def delone():
        delperson=input("Enter name whose no should be deleted")
        value=(delperson,)
        deleteone="delete from numbers where name = %s"
        mycur.execute(deleteone,value)
        mydb.commit()
        print("!!!!! One Number Deleted !!!!!")
    delone()
#else statement
else:
    print("!!!!! WRONG INPUT !!!!!")
#code completed  

