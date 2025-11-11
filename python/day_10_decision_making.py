#decision making statement
#flow control statement
#break, continue, pass

#break - (while you need to print the value until if the condition is true so you can skip the other values)
#it is used to terminate the loop execution and comes out of the loop when certain test condition is met
#and fullfilled.
'''
for i in 'artificial':
    if i in 'i':
        break
    print(i)
'''
'''
#continue - it is usually checks the given statement instead of terminating the loop execution,
#this statement pause the loop execution and comes out of the loop then prints the remain program
#execution from next element of the ongoing loop iteration and then resumes the loop execution.
name = 'softalogaic@acadeamy'
for i in name:
    if i =='a':
        continue
    print(i)


for i in 'artificial':
    if i in 'i':
        continue
    print(i)
'''

#pass - it does nothing just holds the statement
for i in 'string':
    print(i)
    pass

