n=[10,20]
s=list(map(lambda x:x*x,n))
print(s)

n=8
s=lambda x:x*x
print(s(n))

def func(x):
    return lambda n:n + x

add = func(10)
addi = func(20)

print(add(2))
print(addi(4))
