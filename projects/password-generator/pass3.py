while True:
    password = input("Enter a password: ")
    
    # Check 1: Is it 8+ characters?
    if len(password) < 8:
        print("Weak password. Try again.")
        continue  # Go back to start of loop
    
    # Check 2: Does it have at least one number?
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
    
    if not has_number:
        print("Weak password. Try again.")
        continue  # Go back to start of loop
    
    # If we reach here, both checks passed!
    print("Strong password!")
    break  # Exit the loop


  