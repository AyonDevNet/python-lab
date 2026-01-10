name="ayon"
print(name)
print(type(name))  #this is print what type of data is this 


#this process is show the add two string
first_name="bro"
last_name="code"
fullname=first_name+last_name
print('hello' +fullname)    #concanating process


#create the spaces between them

firstname='ayon'
lastname='devnet'
fullname=firstname+ " " +lastname
print(fullname)



#Split

ip='192.168.10.10'

part=ip.split('.')
print(part)

#split for the one or single latter in here
name='rafi mohammed'
parts2=name.split(' ')
print(parts2)
print(parts2[0][0])

#splite for the first word in the string
username = "admin root"
first_letter = username.split()[0]
print(first_letter)


named = 'ayonDevnet'

print(named.find('D'))
print(len(named))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(isinstance(name, str))
print(name.count('e'))
print(name.replace('a' ,'o'))
print(name*3)


#index slicing
#simiply just with before index what we wanna slicing
name='DevNet'
surname=name[0:2] #this the process of slicing the words
name2=name[0:4]
name3=name[4:6]
fanky_name=name[3:6:2]
print(fanky_name)
#print(surname)
#print(name2)
#print(name3)
#reservce the strings
reserve_name=name[::-1]
print(reserve_name)


#slice object
website = 'https://www.youtube.com/'
slice=slice(12,-5)
print(website[slice])




