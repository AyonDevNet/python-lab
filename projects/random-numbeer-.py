import random

secret_number = random.randint(1, 20)
tries = 0

while True:
    guess = int(input('Enter the number: '))
    tries = tries + 1

    if guess < secret_number:
        print('Number is too low')
    elif guess > secret_number:
        print('The number is too high')
    else:
        print(f'You guessed right in {tries} tries!')  # Added 'f' here
        break