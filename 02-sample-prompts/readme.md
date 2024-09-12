# IBM Granite.code model - Sample Prompts

This documentation showcases the some sample prompts for the IBM Granite.code model.

## Usecase 1 : Code Generation

1. In the Granite.code chatbot, enter the below prompt.

```
Generate a Java program that simulates a bank account. It should include options like deposit an amount, 
withdraw an amount, and balance inquiry. Use classes and methods to define these functionalities.
```

You may get the output like this.

<details><summary>CLICK ME</summary>

```
import java.util.Scanner;
 
public class BankAccount {
    private double balance;
 
    public BankAccount() {
        this.balance = 0;
    }
 
    public void deposit(double amount) {
        this.balance += amount;
    }
 
    public void withdraw(double amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
        } else {
            System.out.println("Insufficient funds");
        }
    }
 
    public double getBalance() {
        return this.balance;
    }
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAccount account = new BankAccount();
 
        while (true) {
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Balance inquiry");
            System.out.println("4. Exit");
 
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 2:
                    System.out.print("Enter amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 3:
                    System.out.println("Current balance is " + account.getBalance());
                    break;
                case 4:
                    return;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}

```
</details>


## Usecase 2 : Enhance existing functions

1. In the Granite.code chatbot, enter the below prompt to enhance the existing function.

```
During inquiry, if balance amount is less than 1000 display a message 
"Please maintain minimum balance of Rs.1000/-" along with balance amount.
```

You may get the output like this.

<details><summary>CLICK ME</summary>

```
import java.util.Scanner;
 
public class BankAccount {
    private double balance;
 
    public BankAccount() {
        this.balance = 0;
    }
 
    public void deposit(double amount) {
        this.balance += amount;
    }
 
    public void withdraw(double amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
        } else {
            System.out.println("Insufficient funds");
        }
    }
 
    public double getBalance() {
        return this.balance;
    }
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAccount account = new BankAccount();
 
        while (true) {
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Balance inquiry");
            System.out.println("4. Exit");
 
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 2:
                    System.out.print("Enter amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 3:
                    if (account.getBalance() < 1000) {
                        System.out.println("Please maintain minimum balance of Rs.1000/-");
                    }
                    System.out.println("Current balance is " + account.getBalance());
                    break;
                case 4:
                    return;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}

```
</details>


## Usecase 3 : Code Explanation

1. In the Granite.code chatbot, enter the below prompt to get the explanation about the code.

```
Explain this program
```

You may get the output like this.

<details><summary>CLICK ME</summary>

```
Sure! This program simulates a bank account with three main functionalities: depositing money, withdrawing money, and checking the balance. It uses a class called BankAccount to encapsulate these functionalities.

The program starts by creating an instance of the BankAccount class and initializing its balance to 0. Then, it enters a loop where it prompts the user for input and performs the appropriate action based on the user's choice.

If the user chooses option 1 (deposit), the program prompts the user to enter an amount and calls the deposit method of the BankAccount instance to add the deposited amount to the balance.

If the user chooses option 2 (withdraw), the program prompts the user to enter an amount and calls the withdraw method of the BankAccount instance to subtract the withdrawn amount from the balance. If the withdrawal amount is greater than the current balance, the program displays a message indicating that there are insufficient funds.

If the user chooses option 3 (balance inquiry), the program calls the getBalance method of the BankAccount instance to retrieve the current balance and displays it to the user.

If the user chooses option 4 (exit), the program exits the loop and terminates.

The program uses a Scanner object to read input from the user and a while loop to repeatedly prompt the user until they choose to exit.
```
</details>


## Usecase 4 : Code Conversion

1. In the Granite.code chatbot, enter the below prompt to convert the Java program into Python.

```
Convert this Java program to python.
```

You may get the output like this.

<details><summary>CLICK ME</summary>

```
class BankAccount:
    def __init__(self):
        self.balance = 0

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

```
</details>

2. In VS Code editor, save the above output with name `BankAccount.py`

## Usecase 5 : Code completion

In VS Code editor, do the following.

1. In `BankAccount.py`, replace the content of the  `def __init__(self):` method with the below content.
```
    def __init__(self):
        self.balance = 5000.0
        self.name = "demouser"
        self.address = "123 Main Street"
        self.accountnum = "1234567890"
        self.country = "India"
```
2. In `BankAccount.py`,  add the new method signature `def display_info(self):`

3. Now press `Option` and `.` for multiline code completion  (In windows, use `Alt` instead of `Option`)

It will generate the below code under the above method.
```
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Account Number: {self.accountnum}")
        print(f"Balance: {self.balance}")
        print(f"Country: {self.country}")
``` 

## Usecase 6 : Comment to Code

1. In the VS code Editor, enter the following.

```
# a function to check if user belongs to country India and return string "Indian" else return "NRI"
```

2. Now press `Option` and `.` for multiline code completion  (In windows, use `Alt` instead of `Option`)

It will generate the below code under the above comment.
```
def check_country(user):
    if user.country == "India":
        return "Indian"
    else:
        return "NRI"
``` 

## Usecase 7 : Generate test case

1. In the VS code Editor, enter the following.

```
Generate python unit test for @BankAccount.py
```

It will generate the below unit test cases.

<details><summary>CLICK ME</summary>

```
import unittest
 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()
 
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)
 
    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50)
 
    def test_insufficient_funds(self):
        with self.assertRaises(Exception):
            self.account.withdraw(100)
 
if __name__ == '__main__':
    unittest.main()

``` 
</details>

## Usecase 8 : Documentation

1. In the Granite.code chatbot, enter the below prompt to generate the documentation.

```
Add documentation for method @withdraw 
```
Here `withdraw` is function name.

It will generate the below code with the documentation.

```
def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds") 
```
