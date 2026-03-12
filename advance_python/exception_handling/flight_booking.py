class FlightBook:
    def __init__(self):
        self.available_seats = 2

    def book_flight(self, name, age):
        try:
            if self.available_seats == 0:
                raise IndexError("No seats available on this flight.")
            
            if not name or age < 1:
                raise AttributeError("Invalid passenger details provided.")
            
            if name.lower() == "fail":
                raise RuntimeError("Payment gateway failed.")
                
            self.available_seats -= 1
            print(f"Booking confirmed for {name}!")
            
        except (IndexError, AttributeError, RuntimeError) as e:
            print(f"Booking Failed: {e}")

flight = FlightBook()
flight.book_flight("John Doe", 30)
flight.book_flight("Jane Doe", 25)
flight.book_flight("Bob", 40)