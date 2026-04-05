class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
            Hello can we process our process : 
            1. Enter 1 Create your password
            2. Enter 2 to deposit your money
            3. Enter 3 to withdraw
            4. Enter 4 check the balance
            5. Enter 5 for exit
: """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit_add()
        elif user_input == '3':
            self.withdraw_money()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            print('Thank you! Goodbye.')
        else:
            print('Invalid option. Please try again.')
            self.menu()

    # Create pin
    def create_pin(self):
        self.pin = int(input('Enter your new PIN: '))
        print('PIN created successfully!')
        self.menu()

    # Deposit money
    def deposit_add(self):
        temp_pin = int(input("Enter your PIN: "))
        if temp_pin == self.pin:
            amount = int(input('Enter deposit amount: '))
            self.balance = self.balance + amount
            print(f'Amount ${amount} deposited successfully!')
        else:
            print('Invalid PIN.')
        self.menu()

    # Withdraw money
    def withdraw_money(self):
        give_pin = int(input('Enter your PIN: '))
        if give_pin == self.pin:
            withdraw_amount = int(input('Enter withdrawal amount: '))
            if withdraw_amount <= self.balance:
                self.balance = self.balance - withdraw_amount  
                print(f'${withdraw_amount} withdrawn successfully!')
            else:
                print('Insufficient balance.')
        else:
            print('Invalid PIN.')
        self.menu()

    # Check balance
    def check_balance(self):
        give_pin = int(input('Enter your PIN: '))
        if give_pin == self.pin:
            print(f'Your balance is: ${self.balance}')
        else:
            print('Invalid PIN.')
        self.menu()


Atm()