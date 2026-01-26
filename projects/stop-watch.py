import time

my_time =  int(input('Enter the time : '))

for x in range(my_time, 0, -1):
    second= x % 60
    minutess = int(x/60) % 60
    hours = int(x / 3600)
    print(f'{second:02}:{minutess:02}:{hours:02}')
    time.sleep(1)
print('times is up')