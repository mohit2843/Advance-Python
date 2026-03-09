# #crm(customer relationship manager)
# #store customer information, manage communication logs, track sales pipeline.
    
class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.communications = []  
        self.deal = None          

class Deal:
    def __init__(self, amount, stage="Prospect"):
        self.amount = amount
        self.stage = stage

class CRM:
    def __init__(self):
        self.customers = {}

    def create_customer(self, id, name, email):
        new_customer = Customer(id, name, email)
        self.customers[id] = new_customer
        print(f"Added: {name}")

    def update_deal(self, customer_id, amount, stage):
        if customer_id in self.customers:
            self.customers[customer_id].deal = Deal(amount, stage)
            print(f"Updated deal for {self.customers[customer_id].name}")

    def show_summary(self):
        print("\n--- CRM SALES PIPELINE ---")
        for c in self.customers.values():
            deal_info = f"${c.deal.amount} ({c.deal.stage})" if c.deal else "No Deal"
            print(f"Customer: {c.name} | Status: {deal_info}")
            for note in c.communications:
                print(f"  - {note}")

my_crm = CRM()

my_crm.create_customer(101, "Alice", "alice@email.com")
my_crm.create_customer(102, "Bob", "bob@email.com")

my_crm.update_deal(101, 2500, "Negotiation")
my_crm.update_deal(102, 500, "Qualified Lead")

my_crm.show_summary()               