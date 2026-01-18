import random
import string

print('I will make your password strong')
print('#######################################')

password = input('Enter your password: ')

if password:
    # Generate random numbers between 1 and 4
    random_number = random.randint(1, 4)
    
    # Generate 1 or 2 random alphabets (uppercase and lowercase)
    num_alphabets = random.randint(1, 2)
    random_alphabets = ''.join(random.choice(string.ascii_letters) for _ in range(num_alphabets))
    
    # Add symbols, numbers, and random alphabets to make password strong
    strong_password = password + "##@@$" + str(random_number) + random_alphabets
    
    print('\n Your original password:', password)
    print(' Your strong password:', strong_password)
    print('#######################################')
else:
    print(' Password cannot be empty!')