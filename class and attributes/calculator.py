class calculator:
    brand = 'Casio MS990'
    def cal(self, num1, num2):
        addition = num1+num2
        multipication = num1*num2
        substraction = num1 % num2
        deduction = num1 - num2
        return addition, multipication, substraction, deduction


#When we use a class with parentheses (),
#  we usually create an instance (object) of that class.
my_cal = calculator()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# result = my_cal.cal(10,20)
result = my_cal.cal(num1, num2)
print(result)
           

    