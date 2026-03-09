#scan projects, apply discount, generate bills, and record transactions
#biling system for a retail store
class BillingSystem:
    def __init__(self):
        self.transactions = []
        
    def scan_items(self, items):
        self.items = items
        total_amount = sum(self.items.values())
        return total_amount
        
    def apply_discount(self, total_amount, discount_percentage):
        discount_amount = total_amount * (discount_percentage / 100)
        return total_amount - discount_amount
    
    def generate_bill(self, items, discount_percentage):
        total_amount = self.scan_items(items)
        final_amount = self.apply_discount(total_amount, discount_percentage)
        bill = {
            'items': items,
            'total_amount': total_amount,
            'discount_percentage': discount_percentage,
            'final_amount': final_amount
        }
        self.transactions.append(bill)
        return bill
    
    def record_transaction(self, bill):
        # In a real application, this would save to a database or file
        print("Transaction recorded:", bill)
        
        
    def display(self):
        for transaction in self.transactions:
            print(transaction)
            
obj = BillingSystem()
items = {
    'item1': 100,
    'item2': 200,
    'item3': 300
}
discount_percentage = 10
bill = obj.generate_bill(items, discount_percentage)
obj.record_transaction(bill)
obj.display()
            