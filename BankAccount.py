import random

class BankAccount:
    # The routing number is a 9-digit number that is the same for all bank account
    routing_number = 987654321

    def __init__(self, full_name):
        # Pass in the name argument for the full name of the bank account number
        self.full_name = full_name
        # Each account has its own unique randomly generated 8-digit number
        # Line below inspired from this post: https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python
        self.account_number = f'{random.randrange(1, 10**8):08}'
        # The account balance starts at $0
        self.balance = 0

joi = BankAccount("Joi Anderson")
print(joi.account_number)
