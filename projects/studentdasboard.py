grade = float(input("Enter your total result grade: "))

if grade == 33:
    print('You pass the exam')
elif 33 < grade <= 50:
    print("You got C marks")
elif 50 < grade <= 60:
    print('You got B result')
elif 60 < grade <= 69:
    print('You got A-')
elif 70 <= grade <= 79:
    print('You got A')
elif 80 <= grade <= 100:
    print('You got A+')
else:
    print('You fail the exam')
