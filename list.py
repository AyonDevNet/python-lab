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