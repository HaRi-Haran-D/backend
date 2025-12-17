from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id=e_id.get();
    name=e_name.get();
    phone=e_phone.get();

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert status","all required")

    else:
        con=mysql.connect(host="localhost",user="root",passwd="",port="3307",database='data')
        cursor=con.cursor()
        cursor.execute("insert into details values('"+id+"','"+name+"','"+phone+"')")
        cursor.execute("commit")
        MessageBox.showinfo("insert status","inserted sucessfully")
        con.close()


root=Tk()

root.title("python+Tkinter+Mysql")

id=Label(root,text='Enter Id',font=('bold',10))
id.place(x=20,y=30)

name=Label(root,text="Enter name",font=('bold',10))
name.place(x=20,y=60)

phone=Label(root,text='Enter Phone',font=('bold',10))
phone.place(x=20,y=90)

e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=60)

e_phone=Entry()
e_phone.place(x=150,y=90)

insert=Button(root,text="insert",font=('italic'),bg="gray",command=insert)
insert.place(x=20,y=140)

#get=Button(root,text="Get",font=('italic',10),bg="white",command=get)
#get.place(x=20,y=140)
root.mainloop()
