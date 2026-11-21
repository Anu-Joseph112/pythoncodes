class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdrawal method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    # Display account details
    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# Creating an object
b = BankAccount(101, "Anu", "Savings", 5000)

# Display account details
b.display()

# Deposit
b.deposit(2000)

# Withdraw
b.withdraw(1000)

# Display updated balance
b.display()
