import random

class BankAccount:
    # The routing number is a 9-digit number that is the same for all bank account
    routing_number = 987654321

    def __init__(self, full_name):
        # Pass in the function argument for the full name of the bank account number
        self.full_name = full_name
        # Each account has its own unique randomly generated 8-digit number
        # Line below inspired from this post: https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python
        self.account_number = f'{random.randrange(1, 10**8):08}'
        # The account balance starts at $0
        self.balance = 0

    # The `deposit()` method adds the input `amount` to `balance` and prints out the amount deposited
    def deposit(self, amount):
        self.balance += amount
        # Use .2f below to specify the float to have exactly 2 digits after the decimal point
        print(f"Amount Deposited: ${amount:.2f}")

    # The `withdraw()` method subtracts the input `amount` from `balance` and prints out the amount withdrawn
    # Attempted overdrafts will result in a printed message alerting the user and a charge of $10
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10
            print("Insufficient funds. Your account has been charged an overdraft fee of $10.")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount:.2f}")

    # The `get_balance()` method prints a user-friendly message with the account balance and also returns the balance
    def get_balance(self):
        print(f"Current account balance: ${self.balance:.2f}")
        return self.balance

    # The `add_interest()` method adds montly interest to the account balance (0.083% per month)
    def add_interest(self):
        self.balance *= 1.00083

    # The `print_receipt()` method prints a receipt with the full name, sensitzied account number, routing number, and balance
    def print_receipt(self):
        print(self.full_name)
        # Sensitize the account number before printing by displaying the first four digits as asterisks
        self.account_number = str(self.account_number)
        print(f"Account No.: ****{self.account_number[4:]}")
        print(f"Routing No.: {self.routing_number}")
        self.get_balance()


# Example 1
joi = BankAccount("Joi Anderson")
print(joi.full_name)
print(joi.account_number)
joi.deposit(9000.87)
joi.withdraw(145)
joi.get_balance()
joi.add_interest()
joi.print_receipt()
print()

# Example 2
elon = BankAccount("Elon Musk")
print(elon.full_name)
print(elon.account_number)
elon.deposit(70932156.87)
elon.add_interest()
elon.withdraw(69420)
elon.get_balance()
elon.print_receipt()
print()

# Example 3
kanye = BankAccount("Kanye West")
print(kanye.full_name)
print(kanye.account_number)
kanye.add_interest()
kanye.deposit(808.00)
kanye.withdraw(53000000)
kanye.get_balance()
kanye.print_receipt()