#A for loop is a control flow statement that allows you to execute a block of code repeatedly for each item in a sequence 
#(like a list, string, or range) a predetermined number of times. 
#It is used when the number of iterations is known or fixed.

#range(start, stop, step)


for numbers in range(1, 10, 2):
    print(numbers)

language = 'Python'

for lan in language:
    print(lan, end= '')
else:
    print('Ended the for loop stoped')

#print apple nAME 

fruits = ['apple' , 'mango' , 'licchi']

for fruit in fruits:
    print(fruit)


#write a number 1 to 5

for i in range (1,6):
    print(i)

#write a number 1 to 3

for count in range (1,4):
    print(count)

#Print numbers from 1 to N Problem: Ask the user for a number N. 
# Print all numbers from 1 to N using a for loop


N = int(input("Enter a number: "))

for i2 in range (1, N+1,):
    print(i2)


# Sum of first N natural numbers Problem: Input: N = 5 Output: 1 + 2 + 3 + 4 + 5 = 15


# Ask the user for a number N
N = int(input("Enter a number: "))

# Initialize sum variable
total = 0

# Loop from 1 to N and add each number to total
for i in range(1, N + 1):
    total += i  # total = total + i

# Print the result
print(f"Sum of first {N} natural numbers is: {total}")
