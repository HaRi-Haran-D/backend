#for loop - execute a block of code a fixed number of times
#           you can iterate over a range, string, sequence, etc.

card_no = "1234-5678-9012-3456"
for i in card_no:
    print(i)
    
for i in range(1,11):
    print(i)

#to reverse
for i in reversed(range(1,11)):
    print(i)

for i in range(1,11,2):
    print(i)

#to skip any no in the runtime
for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)
#continue is used so that for loop will run continously until its true
#if break is given the progrom stops until 12 and escapes the loop

#nested loop - a loop within another loop(outer, inner)
#       outer loop:
#            inner loop:

for i in range(6):
    for n in range(0,i):
        print(i,"*")
    print()
