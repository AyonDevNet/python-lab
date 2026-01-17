#A nested loop means one loop inside another loop.

#The outer loop runs first
# For each iteration of the outer loop, the inner loop runs completely



#syntax

#outter loop:
#  inner loop:
       #block of code outter loops
#block og ocde outter loop



#print 1 to 3 , three times at onace

for w in range(3):
    for k in range(1, 4):
        print(k)
    print('------ - ' ) #to see break point


#Number of Triangle
for w in range(1, 6):
    for q in range(1, w+1):
        print(q, end='')
    print()


#printer the star with row and column
for q in range(1,7):
    for a in range(1, 7):
        print('*' , end='')
    print()


#print any sign that you take from users
rows=int(input('How many rows : '))
column=int(input('How many column : '))
symbol=input('Enter the input your symbol : ')

for i in range(rows):
    for k in range(column):
        print(symbol , end='')
    print()


#find the prime number 2 to 10

for num in range(2,10):
    for t in range(2,num):
        if num % t ==0:
            break
    else:
        print(num)