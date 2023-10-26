
class MobileMoneyApp:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        self.transaction_history = []

    def check_balance(self):
        return f"Your account balance is {self.account_balance} GHS."

    def deposit(self, amount):
        self.account_balance += amount
        self.transaction_history.append(f"Deposited {amount} GHS.")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.transaction_history.append(f"Withdrew {amount} GHS.")
        else:
            return "Insufficient funds."

    def view_transaction_history(self):
        return self.transaction_history

def main():
    mobile_money_app = MobileMoneyApp()

    while True:
        print("\nMobile Money App")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            print(mobile_money_app.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            mobile_money_app.deposit(amount)
            print("Deposit successful.")
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            result = mobile_money_app.withdraw(amount)
            if result == "Insufficient funds.":
                print(result)
            else:
                print("Withdrawal successful.")
        elif choice == "4":
            history = mobile_money_app.view_transaction_history()
            for transaction in history:
                print(transaction)
        elif choice == "5":
            print("Exiting the Mobile Money App.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()