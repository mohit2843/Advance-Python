# scan products, apply discount, generate bills, and record transactions
# billing system for a retail store

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
        print("\nTransaction Recorded:")
        print(bill)

    def display(self):
        print("\nAll Transactions:")
        for transaction in self.transactions:
            print(transaction)

i = input("Enter items and prices (item:price, separated by commas): ")

items = {}
for item in i.split(','):
    name, price = item.split(':')
    items[name.strip()] = float(price.strip())

discount = float(input("Enter discount percentage: "))

billing_system = BillingSystem()

bill = billing_system.generate_bill(items, discount)

billing_system.record_transaction(bill)

billing_system.display()