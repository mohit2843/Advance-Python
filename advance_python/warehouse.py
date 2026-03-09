#warehouse automation system
#track goods movement, generate inventory report and forecast demand
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

    def forecast_demand(self, item, historical_data):
        if historical_data:
            average_demand = sum(historical_data) / len(historical_data)
            return average_demand
        else:
            return 0
        
    def display(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print("\nMovement Log:")
        for log in self.movement_log:
            print(log)
        print("\nInventory Report:")
        print(self.generate_inventory_report()) 
        print("\nDemand Forecast for item:")
        
item = input("Enter item to forecast demand: ")
historical_data = input("Enter historical demand data")
historical_data = list(map(int, historical_data.split()))
warehouse = Warehouse()
warehouse.display()
forecast = warehouse.forecast_demand(item, historical_data)
print(f"Forecasted demand for {item}: {forecast}")
