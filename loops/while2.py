counthello = 1
while counthello <= 5:
    print('Hello')
    counthello += 1
 
 
 
counthello2 = 0
while counthello2 <=6:
    print(counthello2, ".hello")
    counthello2 += 1
   
counthi = 0

while counthi < 6:
    print(counthi, 'hi')
    counthi += 1

reverseHello = 5
hellodata = 'hello'
while reverseHello >= 1:
    print( reverseHello,    'hello')
    reverseHello -= 1


college = 1

while college <= 100:
    print(college, 'apna college')
    college += 1


    
#for reverse :  1 to 100 print

ayoncollege = 100

while ayoncollege > 0:
    print(ayoncollege, 'college')
    ayoncollege -= 1



#print the number 1 to 100

number = 1

while number <= 100:
    print(number)
    number += 1


#print the number 100 to 1

number2 = 100

while number2 > 1:
    print(number2)
    number2 -= 1

#print multipication number with n
n = int(input('Enter the number : '))
i = 2

while i <=10:
    print(n*i)
    i += 1



#print out the index

nums = [1 , 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx <= len(nums):
    print(idx)
    idx += 1

#search for x numbers in the tuple

x = int(input("Enter the numbers : "))
nums =(1 , 4, 9, 16, 25, 36, 49, 64, 81, 100)

if x in nums:
    print('found')
else:
    print('not found')

