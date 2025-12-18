from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert_data():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id == "" or name == "" or phone == "":
        MessageBox.showinfo("Insert Status", "All fields are required")
        return

    try:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="",      # ✔ correct password
            port=3306,            # ✔ correct port
            database="data"  # ✔ correct database
        )

        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO details (id, name, phone) VALUES (%s, %s, %s)",
            (id, name, phone)
        )
        con.commit()

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_phone.delete(0, END)

    except mysql.Error as e:
        MessageBox.showerror("Database Error", str(e))


root = Tk()
root.title("Python + Tkinter + MySQL")
root.geometry("350x250")

Label(root, text="Enter Id", font=('bold', 10)).place(x=20, y=30)
Label(root, text="Enter Name", font=('bold', 10)).place(x=20, y=60)
Label(root, text="Enter Phone", font=('bold', 10)).place(x=20, y=90)

e_id = Entry(root)
e_id.place(x=150, y=30)

e_name = Entry(root)
e_name.place(x=150, y=60)

e_phone = Entry(root)
e_phone.place(x=150, y=90)

insert_btn = Button(root, text="Insert", font=('italic', 10), bg="grey", command=insert_data)
insert_btn.place(x=20, y=140)

root.mainloop()
