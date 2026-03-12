# Simple ATM Transaction System
#using multiple accounts
accounts = {
    "123456": {"pin": 1234, "balance": 1000, "transactions": []},
    "654321": {"pin": 4321, "balance": 500, "transactions": []},
    "111111": {"pin": 1111, "balance": 2000, "transactions": []}
}

def authenticate(account_number, pin):
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return True
    return False

def deposit(account_number, amount):
    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append("deposited: " + str(amount))
    print("Amount Deposited")
    
def withdraw(account_number, amount):
    if amount <= accounts[account_number]["balance"]:
        accounts[account_number]["balance"] -= amount
        accounts[account_number]["transactions"].append(f"Withdrawn: {amount}")
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")
        
def check_balance(account_number):
    print("Current Balance: ", accounts[account_number]["balance"])
def transaction_history(account_number):
    print("\nTransaction History") 
    if len(accounts[account_number]["transactions"]) == 0:
        print("No Transaction Yet")
    else:
        for t in accounts[account_number]["transactions"]:
            print(t)
            
account_number = input("Enter your account number:")
pin = int(input("Enter your PIN:"))
if authenticate(account_number, pin):
    while True:
        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Transaction History")
        print("5.Exit")
        
        choice = int(input("Enter your choice:"))
        if choice == 1:
            amt = int(input("Enter Deposit Amount: "))
            deposit(account_number, amt)
            
        elif choice == 2:
            amt = int(input("Enter Withdrawal Amount: "))
            withdraw(account_number, amt)
            
        elif choice == 3:
            check_balance(account_number)
            
        elif choice == 4:
            transaction_history(account_number)
            
        elif choice == 5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
else:
    print("Authentication Failed. Exiting.")                        