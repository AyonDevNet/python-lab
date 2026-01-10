#even-odd number

number=int(input('Give you number : '))

if number % 2 ==0:
    print('this is even')
else:
    print('this is odd')



#if the number is 40 of more then pass

passMark = int(input("Enter your number : "))

if passMark >= 40:
    print('you result is passed')
else:
    print('you are fail')


#If age is 18 or above, print “Eligible to vote”, else print “Not eligible”.

age=int(input('Enter you age : '))

if age>= 18: 
    print('you are eligable for vote')
else:
    print('you are not for vote')

#Given two numbers, print which one is larger.

a=int(input('Enter the number : '))
b=int(input('Enter the number : '))

if a > b:
    print('a number is greater than b')
elif b>a :
    print('b is larger than a')
else:
    print('both number is equal')

#Find the largest number among three numbers using if–else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is the largest")
elif b >= a and b >= c:
    print("Second number is the largest")
else:
    print("Third number is the largest")

#1Network latency check

latency = int(input("Enter network latency in ms: "))

if latency < 50:
    print("Good")
elif 50 <= latency <= 100:
    print("Average")
else:
    print("Poor")


#Temperature Status
 
temperature = int(input("Enter temperature: "))

if temperature > 70:
    print("Overheating")
elif 40 <= temperature <= 70:
    print("Normal")
else:
    print("Cold")
    
#Check Character Type

char = input("Enter a character: ")

if char.isdigit():
    print('digit')
else:
    print('not a digit')
    