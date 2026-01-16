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


count = 0
while count < 11:
     print(count)
     count += 1


#write a number 0 to 3

count1 = 0
while count1 < 4:
  print(count1)
  count1 += 1




#Print numbers from 1 to N Problem: Ask the user for a number N. Print all numbers from 1 to N using a while loop

asknumber = int(input('Enter the number: '))
count2 = 1

while count2 <= asknumber:
    print(count2)
    count2 += 1



# Sum of first N natural numbers Problem: Input: N = 5 Output: 1 + 2 + 3 + 4 + 5 = 15

N = int(input("Enter a number N: "))

sum = 0
count3 = 1
while count3 <= N:
   sum += count3
   count3 += 1 

print(f"The sum of first {N} natural numbers is: {sum}")






#Print all even numbers up to N Problem:  Input: N = 20,  Output: 2 4 6 8 10 12 14 16 18 20
 # Ask the user for input
N = int(input("Enter a number N: "))

# Start from 2 (first even number)
number = 2

# Loop until number is less than or equal to N
while number <= N:
    print(number, end=" ")  # Print number on the same line
    number += 2             # Move to the next even number
