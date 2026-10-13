#           # 0   1  2   3   4
# numbers = [10, 20, 30, 40, 50]
#          # -5  -4  -3  -2  -1 

# # Access elements
# print(numbers[0])
# print(numbers[2])
# print(numbers[-2])
# print(numbers[-4])



# # Change an element

# numbers[0] = 90
# print(numbers)


# # Add elements — append()
# # append will add the element by the last sides

# numbers.append(100)
# print(numbers)


# # Add at a specific position — insert()
# # we can add the value specfic index by using the insert() value

# numbers.insert(1, 200
#                )
# print(numbers)


# # Remove an element — remove()
# numbers.remove(90)
# print(numbers)

# # 7. Remove using index — pop()
# numbers.pop(2)
# print(numbers)

# # determind the lenth of the array
# print(len(numbers))
# numbers.sort(reverse=True)


# # print(max(numbers)) 
# # print(min(numbers)

# print(numbers[1:4])



# numbers2 = [10, 20, 30, 40, 50, 24, 23, 44]

# odds = []

# for num in numbers2:
#     if num % 2 == 0:
#         odds.append(num)

# print(odds)


name = ['sakib' , 'Mushfiq', 'Mashrafi']
age = [35, 37 , 38]
player = []
for nam in name:
    print("the player names : ", nam)
    for ages in age:
        print(nam, ages)
        player.append([nam, ages])
print(player)
