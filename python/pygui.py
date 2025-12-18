from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert_data():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id == "" or name == "" or phone == "":
        MessageBox.showwarning("Status", "All fields are required")
        return

    con = None
    try:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="password",      # put password if exists
            port='3307',        # change to 3307 if needed
            database="data"
        )

        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO details (id, name, phone) VALUES (%s, %s, %s)",
            (id, name, phone)
        )
        con.commit()

        MessageBox.showinfo("Status", "Inserted Successfully")

    except mysql.Error as e:
        MessageBox.showerror("MySQL Error", str(e))

    finally:
        if con and con.is_connected():
            con.close()

# ---------- GUI ----------
root = Tk()
root.title("Tkinter + MySQL")
root.geometry("350x220")   # 🔑 IMPORTANT

Label(root, text="Enter ID").place(x=20, y=30)
Label(root, text="Enter Name").place(x=20, y=60)
Label(root, text="Enter Phone").place(x=20, y=90)

e_id = Entry(root)
e_id.place(x=150, y=30)

e_name = Entry(root)
e_name.place(x=150, y=60)

e_phone = Entry(root)
e_phone.place(x=150, y=90)

insert=Button(root,text="insert",font=('italic'),bg="white",command='insert')
insert.place(x=20,y=140)

#Button(root, text="Insert", command=insert_data).place(x=150, y=140)

root.mainloop()
