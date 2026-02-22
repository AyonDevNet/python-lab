numbers = (1, 2, 3, 4)

print(numbers)
print(numbers[0])
print(numbers[2])



student=('devnet' , 21 , 'male')

for x in student:
    print(x)
if 'devnet' in student:
    print('devnet is here')


# A Python tuple is a collection of ordered and immutable elements. 
# Once created, you cannot change or modify the elements of a tuple. 
# Python programming often uses tuples when fixed data structures are needed, 
# and they're a great tool for beginners exploring different data types in a programming language.

#Tuples and List are prety similar
# tuple declare in (), for example : numbers = (1, 2, 3, 4)


#**** tuple constructor
#  Its primary use is to convert other iterable objects 
# (such as lists, strings, sets, or ranges) into tuples or to create an empty tuple. 


my_list = [1,2,3,4]
result = tuple(my_list)
print(result)


numbers2 = (1, 2, 3, 4)
result2=reversed(numbers2)
print(result2)

numbers3= (1, 2, 3, 4) * 2 #just write 2 times
print(numbers3)

#this is the pack tuple
a = 'devnet'
b = 21
c='engineer'

tuple_pack = a, b, c
print(tuple_pack)


#unpack tuple

anme, ehe, prodess = a,b,c   #during unpack we have to give eaxct same things in here , no more add or less
print(anme)
print(ehe)
print(prodess)