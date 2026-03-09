#parking lot management system
#track vehicle entry/exit, available slots, and compute parking fees
class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.available_slots = total_slots
        self.parked_vehicles = {}

    def park_vehicle(self, vehicle_id, entry_time):
        if self.available_slots > 0:
            self.parked_vehicles[vehicle_id] = entry_time
            self.available_slots = self.available_slots - 1
            print("Vehicle parked successfully.")
        else:
            print("Parking lot is full. Cannot park the vehicle.")

    def exit_vehicle(self, vehicle_id, exit_time):
        if vehicle_id in self.parked_vehicles:
            entry_time = self.parked_vehicles.pop(vehicle_id)
            self.available_slots = self.available_slots + 1
            parking_fee = self.calculate_fee(entry_time, exit_time)
            print(f"Vehicle {vehicle_id} exited at {exit_time}. Parking fee: {parking_fee:.2f}")
        else:
            print("Vehicle not found in the parking lot.")

    def calculate_fee(self, entry_time, exit_time):
        hours_parked = (exit_time - entry_time)
        fee_per_hour = 5.0
        return hours_parked * fee_per_hour
    
    def display(self):
        print("Total slots:", self.total_slots)
        print("Available slots:", self.available_slots)
        print("Parked vehicles:", self.parked_vehicles)
        print("Parking fee per hour: 5.0")
        
       
slots = int(input("enter total slots:")) 
vehicle_id = input("enter vehicle id:")
entry_time = int(input("enter entry time (in hours):"))
exit_time = int(input("enter exit time (in hours):"))
obj = ParkingLot(slots)
obj.park_vehicle(vehicle_id, entry_time)
obj.exit_vehicle(vehicle_id, exit_time)
obj.display()
