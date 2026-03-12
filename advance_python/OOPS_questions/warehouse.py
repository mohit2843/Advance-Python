# Warehouse Automation System
# Track goods movement, generate inventory report and forecast demand

class Warehouse:
    def __init__(self):
        self.inventory = {}
        self.movement_log = []

    def add_goods(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

        self.movement_log.append(f"Added {quantity} of {item}")

    def remove_goods(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            self.movement_log.append(f"Removed {quantity} of {item}")
        else:
            print(f"Not enough {item} in inventory to remove.")

    def generate_inventory_report(self):
        report = "Inventory Report:\n"
        for item, quantity in self.inventory.items():
            report += f"{item}: {quantity}\n"
        return report

    def forecast_demand(self, historical_data):
        if historical_data:
            return sum(historical_data) / len(historical_data)
        return 0

    def display(self):
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

        print("\nMovement Log:")
        for log in self.movement_log:
            print(log)

        print("\nInventory Report:")
        print(self.generate_inventory_report())

warehouse = Warehouse()

n = int(input("Enter number of items to add: "))
for _ in range(n):
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    warehouse.add_goods(item, qty)

remove = input("Do you want to remove goods? (yes/no): ")
if remove.lower() == "yes":
    item = input("Enter item name to remove: ")
    qty = int(input("Enter quantity: "))
    warehouse.remove_goods(item, qty)

warehouse.display()

item = input("\nEnter item to forecast demand: ")
historical_data = input("Enter historical demand data (space separated): ")
historical_data = list(map(int, historical_data.split()))
forecast = warehouse.forecast_demand(historical_data)
print(f"\nForecasted demand for {item}: {forecast}")