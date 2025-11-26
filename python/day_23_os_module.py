import os
from datetime import datetime

os.chdir('D:/full_stack/backend/') #to change the path of the directory

#os.mkdir('End') to create a directory
#os.makedirs('End1/end') to create a directory with sub-folders

#os.rmdir('End') to delete a directory
#os.removedirs('End/end') to delete a directory with sub-folders

#print(os.getcwd()) #to find the directory/path where you are working
#print(os.listdir()) #by default it will list the files in the current directory

#os.rename('Existing filename','new name') #to rename a file
#a = os.stat('HariHaran.txt').st_atime
#print(datetime.fromtimestamp(a))
'''
for path,dirs,files in os.walk('D:/full_stack/backend/'):
    print('Current Path:',path) #which file path we are in
    print('Current Directory:',dirs) #which folder we are in
    print('Current File:',files) #files which are inside the folder
    print(' ')
'''

print(os.environ.get('OS'))




