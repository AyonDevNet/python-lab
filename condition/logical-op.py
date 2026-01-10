#n Python (and most programming + networking logic), we mainly use: and , or , not.

temp = int(input('Enter the temperature: '))

# Invalid
if temp < 0:
    print('Invalid temperature')

# Freezing cold
elif temp >= 0 and temp <= 8:
    print('This is freezing cold')

# Cold
elif temp >= 9 and temp <= 20:
    print('This is cold')

# Normal (use not + or for fun)
elif not (temp < 0 or temp <= 20):
    print('Temperature is normal')




temp = int(input('Enter the temperature: '))

# Invalid temperature
if not (temp >= 0):
    print('Invalid temperature')

# Freezing cold (0 to 8)
elif not (temp < 0 or temp > 8):
    print('This is freezing cold')

# Cold (9 to 20)
elif not (temp < 9 or temp > 20):
    print('This is cold')

# Normal (> 20)
elif not (temp <= 20):
    print('Temperature is normal')
