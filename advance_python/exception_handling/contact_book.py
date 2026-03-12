class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        try:
            if not name or not phone:
                raise ValueError("Fields cannot be empty.")
            
            if name in self.contacts:
                raise KeyError("Contact already exists.")
                
            self.contacts[name] = phone
            print("Contact saved.", name)
            
        except (ValueError, KeyError) as e:
            print("Contact Error:")

book = ContactBook()
book.add_contact("Alice", "1234567890")
book.add_contact("Alice", "0987654321")