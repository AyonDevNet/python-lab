import re

def password_check(password):
    length_check = len(password) >= 8
    digit_check = re.search(r'\d', password)
    upper_case = re.search(r'[A-Z]', password)
    lower_case = re.search(r'[a-z]', password)

    if all([length_check, digit_check, upper_case, lower_case]):
        return "Strong password!"
    else:
        errors = []
        if not length_check: errors.append("at least 8 characters")
        if not digit_check: errors.append("at least one digit")
        if not upper_case: errors.append("at least one uppercase letter")
        if not lower_case: errors.append("at least one lowercase letter")
        return f"Weak password. Missing: {', '.join(errors)}"
    

print('Welcome to Password Checker')

while True:
    password = input("Enter a password: ")
    result = password_check(password)
    print(result)
    
    if "Strong" in result:
        break  # Exit loop when password is strong

