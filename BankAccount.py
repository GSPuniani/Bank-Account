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

    # The `deposit` method adds the input `amount` to `balance` and prints out the amount deposited
    def deposit(self, amount):
        self.balance += amount
        # Use .2f below to specify the float to have exactly 2 digits after the decimal point
        print(f"Amount Deposited: ${amount:.2f}")

    # The `withdraw` method subtracts the input `amount` from `balance` and prints out the amount withdrawn
    # Attempted overdrafts will result in a printed message alerting the user and a charge of $10
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10
            print("Insufficient funds. Your account has been charged an overdraft fee of $10.")
        else:
            self.balance -= amount
            # Use .2f below to specify the float to have exactly 2 digits after the decimal point
            print(f"Amount Withdrawn: ${amount:.2f}")


joi = BankAccount("Joi Anderson")
print(joi.account_number)
joi.deposit(9.87)
joi.withdraw(9)
