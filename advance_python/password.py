#password manager
#securely store, add , edit, and retrieve user password using encryption
class password_manager:
    def __init__(self):
        self.passwords = {}
    
    def add_password(self, account, password):
        self.passwords[account] = password
    
    def edit_password(self, account, new_password):
        if account in self.passwords:
            self.passwords[account] = new_password
        else:
            print("Account not found.")
    
    def retrieve_password(self, account):
        return self.passwords.get(account, "Account not found.")
    
    def display_passwords(self):
        for account, password in self.passwords.items():
            print(f"{account}: {password}")
manager = password_manager()
manager.add_password("email", "12345")
manager.add_password("bank", "bank_password")
account = input("Enter account to edit password: ")
new_password = input("Enter new password: ")
manager.edit_password(account, new_password)
manager.display_passwords()
account = input("Enter account to retrieve password: ")
print(manager.retrieve_password(account))