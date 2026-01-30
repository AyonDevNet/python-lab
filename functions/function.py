def addnmbr(a,b):
    result = a+b
    print(result)
addnmbr(2,3)


def numbers(a,b):
    return a+b
sumthenm= numbers(2,4)
print(sumthenm)



def myname(a,b):
    result2=a+b
    #print(result2)

 #myname(f'josim' 'kasem')


#Write a Python function to find the maximum of three numbers.


def maxim():
    a= input('Enter the number')
    b= input('Enter the number')

    if a > b:
        print(' a the big number')
    elif b>a:
        print('b is the big number')
    elif a == b:
        print('both are equal')
    else:
        print('input not valid')
         

maxim()


#Write a Python function to sum all the numbers in a list.

# Define a function named 'sum' that takes a list of numbers as input
def sumed(numbered):
    result=0
    for x in numbered:
        result+=x
    
    return result
sumlist=[8, 2, 3, 0, 7]
print("The sum is:", sumed(sumlist))

      

def mathed(additioned):
    tested=0
    for i in additioned:
        tested+=i
        
    return tested

subtract= [4, 7, 1, 9, 3]
print('this the result : ', mathed(subtract))
 
#find the biggest number : 4, 7, 1, 9, 3
def find_max(numbers):
    biggest = numbers[0]   # assume first number is the largest

    for num in numbers:
        if num > biggest:
            biggest = num

    return biggest

values = [4, 7, 1, 9, 3]
print("The biggest number is:", find_max(values))






