weight=float(input('Enter your weight : '))
unit = input('Tell us kg or pound (K for kg and L for pound): ')

if unit == 'L':
    weight = weight * 2.205
    unit= "LBS"
elif unit == 'K':
    weight = weight / 2.205
    unit = 'Kg'
else:
    print(f'{unit} this is not valid')
print(f'Your weight is {round(weight, 2 )} {unit}')
