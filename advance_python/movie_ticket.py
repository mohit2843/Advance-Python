#check showtimes, book tickets, select seats, and print
class movie_ticket:
    def __init__(self, movie_name, showtime, book_ticket, select_seat, print_ticket):
        self.movie_name = movie_name
        self.showtime = showtime
        self.book_ticket = book_ticket
        self.select_seat = select_seat
        self.print_ticket = print_ticket
        
    def display(self):
        print("movie name:",self.movie_name)
        print("showtime:",self.showtime)
        print("book ticket:",self.book_ticket)
        print("select seat:",self.select_seat)
        print("print ticket:",self.print_ticket)
        
        
movie = []

m =input("enter the movie name:")
s= input("enter the showtime:")
b = input("do you want to book ticket? (yes/no):")
if b == "yes":
    print("ticket booked successfully")
else:
    print("ticket not booked")
    
seat = input("which type of seat you want(standard/premium):")
if seat == "standard":
    print("you have selected standard seat")
elif seat == "premium":
    print("you have selected premium seat")
else:
    print("invalid seat type")
    
p = input("do you want to print ticket? (yes/no):")
if p == "yes":  print("ticket printed successfully")
else:
    print("ticket not printed")
    
obj = movie_ticket(m,s,b,seat,p)
movie.append(obj)
print("\nMovie Ticket Details:")
for m in movie:
    m.display()