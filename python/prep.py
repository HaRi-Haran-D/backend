'''
class Manage:
    def __init__(self):
        self.product=[]
    def add(self,add_product):
        self.product.append(add_product)
        print(add_product, 'Added')
    def delete(self,del_product):
        if del_product in self.product:
            self.product.remove(del_product)
            print(del_product, 'Deleted')
        else:
            print(del_product, 'Dont Exist')

s=Manage()
s.add('Icecream')
s.add('Chocolate')
s.add('Cooldrinks')
s.add('Grapes')
print(s.product)
s.delete('Grapes')
print(s.product)
'''
'''
for i in range(0,5):
    for j in range(5-i):
        print(' ', end="")
    for j in range(0,i+1):
        print('*',end=' ')
    print()

for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for j in range(0,i-1):
        print('*',end=' ')
    print()
'''

a = [0,1,2,4,0,7,0]
b=[]
for i in a:
    if i==0:
        b+=[i]
for j in a:
    if j > 0:
        b+=[j]

print(b)
