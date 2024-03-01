class Bank:
    def __init__(self):
        self.balance = 1500
        print(f"Initial Balance: {self.balance}.")

    def deposit(self):
        self.dep = int(input("Enter the amount to be deposited: "))
        if self.dep <= 0:
            print("Amount to be deposited must be greater than 0.")
        else:
            print(f"Amount deposited is {self.dep}.\nTotal balance is {self.balance + self.dep}.")
            self.balance += self.dep

    def withdraw(self):
        self.withd = int(input("Enter the amount to be withdrawn: "))
        if self.withd > self.balance:
            print("Insufficient Balance!")
        else:
            print(f"Amount withdrawn is {self.withd}.\nTotal balance is {self.balance - self.withd}.")
            self.balance -= self.withd

b1 = Bank()


while True:
    print("Enter 1 for deposit.\nEnter 2 for withdrawal.\nEnter 0 to exit.\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        b1.deposit()
    elif choice == 2:
        b1.withdraw()
    elif choice == 0:
        print("Exiting the program.")
        break  
    else:
        print("Incorrect choice!")
