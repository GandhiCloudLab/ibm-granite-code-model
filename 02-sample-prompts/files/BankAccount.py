class BankAccount:

    def __init__(self):
        self.balance = 5000.0
        self.name = "demouser"
        self.address = "123 Main Street"
        self.accountnum = "1234567890"
        self.country = "India"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

def main():
    account = BankAccount()
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance inquiry")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            balance = account.get_balance()
            print(f"Current balance is {balance}")
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
