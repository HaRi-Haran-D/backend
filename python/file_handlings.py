#File handling
#file handling means we are gonna work with the python which the help of methods and modes

#syntax
#write(), read(), readline(), readlineofsize(), readlines(), writelines()

#Modes
#r - read only read option the file pointer will be present at the beginning of the file
#w - write operation if the file not present the file will be created
#a - append open existing file and it won't be overriden the existing content
#r+ - it will read and write into the particular file
#w+ - it will write and read data from the existing file
#a+ - append and read the data
#x - exclusive operation file is already present it will
     #throw an error as file exist

#rb - reading binary data
#wb - writing the binary data
#r+b - read and write binary data
#w+b - write and read the binary data
#a+b - append and read the binary data

#a=open(filename,mode)
#open()
#read()
#readline()
#readlinesize()
#write()
#writelines()
#close()

import os
#os.mkdir('date512')

n= open('tnt','w')
print('filename is',n.name)
print('Filemode is',n.mode)



'''
file handling means working with files in python
with the help of methods and modes

syntax:
open(parameter,filename,mode)

modes:
r=read
a=append
w=write
x=create the specific files 
if not exists returns error 
rb
wb

#File handling in python
text files:.txt,.doc,.pdf

Binary Files
images/video/audio

f=open(filename,mode)

r=read mode (file pointer)
file is not present--->filenotfounderror
w=write mode (existing content of the file will be overriden)
file is not present--->This will create a new file
a=append (existing data will be added)
r+=reading (read and write data into a file.existing
content will not get deleted)
w+=write and read data from the file.it will override the existing content
a+=append and read data
x=exclusive operation
-->if file is already present,it will throw error

rb,wb,r+b,w+b,a+b,xb-binary files


closing file :
f.open('demo.txt',w)
f.read()
f.readline
f.readlines(5)
f.write(sdjkhfsdjfhdjf)
f.close()

1,filename
2,mode
3,readable
4,writeable
5,closed--true/false

import os
os.mkdir('date81225')

f=open('datenow81225','w')
print('filename is',f.name)
print('filemode is',f.mode)
print('fileproperty is',f.readable())
print('fileproperty is',f.writable())
print('file is closed',f.closed)
f.close()
print('file is closed or not',f.name)


f=open('pythoncreate','w')
f.write('python class \n')
f.write('taken in crr \n')
#if it is more data
list=['one'',','two','three','four','five']
f.writelines(list)
f.close()
print('file is closed',f.closed)

#read
f=open('datenow81225','r')
output=f.read()
print(output)
f.close()
print('file is closed',f.closed)

#readsize
f=open('datenow81225','r')
output=f.read(5)
print(output)
f.close()
print('file is closed',f.closed)

#readlines
f=open('datenow81225','r')
output=f.readlines()
print(output)
f.close()
print('file is closed',f.closed)

#convert the str
f=open('datenow81225','r')
output=f.readlines()
info=str(output)
print(type(info))
print(info)
print(output)
f.close()
print('file is closed',f.closed)

#file is there or not to check
import os
filename=input('enter the name')
if os.path.isfile(filename):
    print('yes,present')
    f=open(filename,'r')
else:
    print('no not present')

#images read aand write
f1 = open(r"C:\frontend\project\static\images\k1.jpg", "rb")
f2 = open(r"C:\frontend\project\static\images\k1_copy.jpg", "wb")

data = f1.read()
f2.write(data)

f1.close()
f2.close()

#comma seperated values
import csv

with open('trainees.csv', 'w', newline='') as f:
    w = csv.writer(f)

    # write header row
    w.writerow(['TNO', 'TraineeName', 'Qualification'])

    no = int(input('Enter the number of trainees: '))

    for trainee in range(no):
        tno = int(input('Enter trainee number: '))
        tName = input('Enter trainee name: ')
        tQuali = input('Enter qualification: ')
        w.writerow([tno, tName, tQuali])
'''


#pandas
#series 1D, 2D, dsa in pandas
#dataframe
#why pandas
