class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def transfer(self, amount, recipient_acc):
        try:
            if amount > self.balance:
                raise ArithmeticError("Insufficient funds.")
            
            self.balance = self.balance - amount
            print("Successfully transferred.",amount)
            
        except (ArithmeticError) as e:
            print("Transaction Failed:", e)

my_acc = BankAccount("123", 500)
my_acc.transfer(100, "456")
