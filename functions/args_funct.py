def sum(*num):
    sum=0
    for number in num:
       sum = sum +number
    return sum
    

total = sum(10, 20 ,30, 40,)
print(total)