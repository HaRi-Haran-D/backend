#GUI: Graphicla User interface

'''
import tkinter#library
a=tkinter.Tk()#to create creation window
a.mainloop()#close output show


#methods in tkinter

1. pack() method --> top, right, left
2. grid() method --> row and column
3. place() method --> x-axis and y-axis
'''

'''
from tkinter import *
a=Tk()
b=Label(a,text='Welcome to GUI screen')
b.pack()
a.mainloop()
'''
'''
from tkinter import *
a=Tk()
b=Label(a,text='Welcome to GUI screen')
b=Label(a,text='FirstName').grid(row=1)
b=Label(a,text='LastsName').grid(row=2)
c=Label(a,text='Address').grid(row=3)
d=Label(a,text='DOB').grid(row=4)
e1=Entry(a)
e2=Entry(b)
e3=Entry(c)
e4=Entry(d)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)

a.mainloop()
'''

'''
import tkinter
def click():
    label.config(text='Button Clicked')

window=tkinter.Tk()
window.title('Gui with action added in label')

label=tkinter.Label(window,text='Hello World')
label.pack(pady=15)

button=tk.Button(window,text='Click',command=click)

button.pack()
 
window.mainloop()
'''

import tkinter
def click():
    label.config(text='Form Submitted')

window=tkinter.Tk()
window.title('Register Form')

label1=tkinter.Label(window,text='First Name').grid(row=1)
label2=tkinter.Label(window,text='Last Name').grid(row=2)

a=Entry(label1)
b=Entry(label2)
a.grid(row=1,column=1)
b.grid(row=2,column=1)

button=tk.Button(window,text='Click',command=click)

button.pack()

window.mainloop()
















