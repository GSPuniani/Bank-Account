# Bank-Account

<i>Make School CS 1.1: Homework #1</i>

This project uses Python 3.7.4.

This project contains only one Python file, `BankAccount.py`. In that file is a class called `BankAccount`, which contains 1 class attribute (a 9-digit integer called `routing_number`) and 3 instance attributes (`full_name`, `account_number`, and `balance`). `account_number` is a randomly generated integer with exactly 8 digits and is unique to each account. `balance` is initialized to 0, since each account balance begins at $0. 

The `BankAccount` class also has 5 methods: 
`deposit()`, which takes in a parameter called `amount`, adds that to the balance, and displays a message to the user on the amount deposited; 
`withdraw()`, which takes in a parameter called `amount`, subtracts that from the balance or subtracts $10 for an attempted overdraft, and displays a message to the user on the amount withdrawn or on the overdraft fee; 
`get_balance()`, which prints to the user and returns the account balance;
`add_interest()`, which adds 0.083% (monthly interest rate) of the balance to the balance; and 
`print_receipt()`, which prints out the full name, a censored version of the account number, the routing number, and the account balance in a user-friendly way.

`BankAccount.py` also includes 3 examples of the `BankAccount` object to demonstrate the functionality of the properties and methods.

