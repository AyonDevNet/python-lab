
operator = input('Enter the operator +, * , - /: ')
num1=float(input('Enter the 1st number : '))
num2=float(input('Enter the 2nd number : '))

if operator == '+':
    result=num1+num2
    print (round(result , 3))  #only add round show round num and , 3 means 3 are float number will
elif operator == '-':
    result=num1-num2
    print (round(result , 3))
elif operator == '*':
    result=num1*num2
    print (round(result , 3 ))
elif operator == '/':
    result=num1/num2
    print (round(result , 3 ))
else:
    print(f'{operator} this is not valid')
