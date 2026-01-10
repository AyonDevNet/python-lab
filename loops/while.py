#A while loop is a control flow statement in programming 
# that repeatedly executes a block of code as long as a certain condition is true

#when we write the code you have to put here something until it donot work
#while 1==1:
    #print('i am stuck in the loop')


name = ''
while len(name) == 0:
  name=input('Enter your name ')

print('Hello bro' +name)


name = None
while not name:
  name=input('Enter the name is ')

print('hello broo ' +name)




#Count from 1 to 10

count = 1
while count <= 10:
 print(count)
count+=1
