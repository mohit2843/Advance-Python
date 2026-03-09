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
        if id in self.customers:
            print("Customer already exists")
        else:
            self.customers[id] = Customer(id, name, email)
            print(f"Customer added: {name}")

    def add_communication(self, customer_id, note):
        if customer_id in self.customers:
            self.customers[customer_id].communications.append(note)
            print("Communication added")
        else:
            print("Customer not found")

    def update_deal(self, customer_id, amount, stage):
        if customer_id in self.customers:
            self.customers[customer_id].deal = Deal(amount, stage)
            print(f"Deal updated for {self.customers[customer_id].name}")
        else:
            print("Customer not found")
    def show_summary(self):
        print("\n----- CRM SALES PIPELINE -----")

        for customer in self.customers.values():
            if customer.deal:
                deal_info = f"${customer.deal.amount} ({customer.deal.stage})"
            else:
                deal_info = "No Deal"

            print(f"\nCustomer ID: {customer.id}")
            print(f"Name: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Deal: {deal_info}")

            print("Communications:")
            if customer.communications:
                for note in customer.communications:
                    print(f" - {note}")
            else:
                print(" No communications yet")
my_crm = CRM()

i = input("Enter customer ID: ")
n = input("Enter customer name: ")
e = input("Enter customer email: ")
my_crm.create_customer(i, n, e)
comm = input("Enter communication note: ")
my_crm.add_communication(i, comm)
amount = float(input("Enter deal amount: "))
stage = input("Enter deal stage: ")
my_crm.update_deal(i, amount, stage)
my_crm.show_summary()
