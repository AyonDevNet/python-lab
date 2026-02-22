def bill():
    num1=int(input('Enter the price product1 : '))
    num2 = int(input('Enter the price product2 : '))
    num3 = int(input('Enter the price product3 : '))
    cupon = input('Is there any cupon yes/no: ')
    
    result = (num1+num2+num3)
    finalResult  = (result * 0.10)

    if cupon == 'yes':
        print("You got discount " , finalResult)
    else:
        print('You total value is : ' , result)

    
bill()
