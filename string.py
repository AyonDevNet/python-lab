name = 'Sakib khan'
name2 = "Sakibtkhan"

name3 = """
shakib khan 
number one
"""
# string is the immutable means : it is cannot
# be change
for char in name2:
    print(char)

print(name2[3]) #this only print no:3 index
print(name2[1:6]) #from 1 to 5 will be print 6 will not
print(name[-3])
print(name[::-1]) #we can reverse this totally
print(name.find("t"))
print(name.format(name2))