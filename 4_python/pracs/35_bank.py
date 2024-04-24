#Write a python program to create a Bank class where deposits and withdrawals can be handled by using instance methods.

class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid amount. Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")


# Create a bank account with initial balance of $0
bank_account = Bank()

# Continuous loop to handle deposits, withdrawals, and balance display
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Deposit
        amount = float(input("Enter amount to deposit: "))
        bank_account.deposit(amount)
    elif choice == '2':
        # Withdraw
        amount = float(input("Enter amount to withdraw: "))
        bank_account.withdraw(amount)
    elif choice == '3':
        # Display Balance
        bank_account.display_balance()
    elif choice == '4':
        # Exit the program
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
