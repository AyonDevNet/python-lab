import random

print('I will make your password strong')
print('#######################################')

password = input('Enter your password: ')

if password:
    # Generate random numbers between 1 and 4
    random_number = random.randint(1, 4)
    
    # Add symbols and numbers to make password strong
    strong_password = password + "##@@" + str(random_number)
    
    print('\n✅ Your original password:', password)
    print('🔐 Your strong password:', strong_password)
    print('#######################################')
else:
    print('❌ Password cannot be empty!')