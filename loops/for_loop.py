#A for loop is a control flow statement that allows you to execute a block of code repeatedly for each item in a sequence 
#(like a list, string, or range) a predetermined number of times. 
#It is used when the number of iterations is known or fixed.

#range(start, stop, step)


nums = [1,2,3,4,5]

for variable in nums:
    print(variable)


name = "mohammedayon"

for admin in name:
    if(admin == 'a'):
        print('found')
        continue
    print(admin)




nums = [1 , 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0

for idx in range(len(nums)):
    print(idx)