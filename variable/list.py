deep_list = [1, [2, [3, 4]], 5]
print(deep_list[1][1][0])  # Output: 3

#Syntax: list_name[start:stop:step]

#Example: numbers = [10, 20, 30, 40, 50, 60]

#Index →
#0   1   2   3   4   5
#-6  -5  -4  -3  -2  -1

# Slice from index 1 to 3 -> print(numbers[1:4])   # Output: [20, 30, 40]

# Slice from start to index 2 -> print(numbers[:3])   # Output: [10, 20, 30]

# Slice all alternate elements -> print(numbers[0::2])   # Output: [10, 30, 50]

# Slice with negative indices -> print(numbers[-4:-1])   # Output: [30, 40, 50]

# Reverse list -> print(numbers[::-1])   # Output: [60, 50, 40, 30, 20, 10]

#reserves the lsit 

list2 = [1,2,3,4,5,6]

print(list2[::-1])


#replace the list 

mylist = ['orange', 'apple']
mylist[0]= 'strawberry'
print(mylist)


#pop() which is helps to remove from list

device = ['router', 'switch', 'firewall']

remove = device.pop(1) #add index to delete the str
print(remove)
print(device)

#sort() reorders the list in place (it changes the original list).
 
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)


#count() tells you how many times a value appears in a list.
roles = ["admin", "user", "user", "admin", "guest"]
print(roles.count("user"))



#extended the list 


callist1=['a', 'b', 'c']
callist2=['1','2']
resultoflist = callist1 + callist2
print(resultoflist)



for x in callist1:
    callist2.append(callist1)
    print(callist2)

#callist1.extend(callist2)


squre = [x**2 for x in range(1,6)]
print(squre)

even_list = [x for x in range(1, 10) if x % 2 == 0]
print(even_list)

nested = [[1, 2], [3, 4], [5, 6]]

flat=[]

for sublist in nested:
    for item in nested:
        flat.append(item)
print(flat)


servers = [
    ("web-01", 68),
    ("db-01", 85),
    ("cache-01", 92),
    ("backup-01", 55)
]

for usage, ratio in servers:
    if ratio <= 80:
        print('memory in denger range')
    else:
        print('this is ok') 




