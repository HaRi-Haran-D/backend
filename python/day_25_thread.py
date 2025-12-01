import threading
import time
'''
def number():
    for i in range(1,6):
        print('Numbers:',i)

def alpha():
    for i in ['a','b','c','d','e']:
        print('Alphabets:',i)

t1=threading.Thread(target=number)
t2=threading.Thread(target=alpha)
t1.start()
t2.start()
t1.join()
t2.join()


def table(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i)

t1=threading.Thread(target=table, args=(5,))
t2=threading.Thread(target=table, args=(9,))
t1.start()
t2.start()
t1.join()
t2.join()
'''

'''
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('Thread running',self.name)
            time.sleep(3)

t1=MyThread()
t2=MyThread()        

t1.start()
t2.start()

t1.join()
t2.join()
'''

#def task(name):
 #   for i in range(3):
  #      print(name,'Hii...')

import threading
import time

def print_name(name, delay, repeat):
    for i in range(repeat):
        print(name)
        time.sleep(delay)

t1 = threading.Thread(target=print_name, args=("Hari", 5, 5))
t2 = threading.Thread(target=print_name, args=("Haran", 8, 8))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")


















