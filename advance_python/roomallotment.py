rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}
while True:
    print("\n Hostel Room Allocation")
    print("1.Allocate Room")
    print("2.View Room Status")
    print("3.Remove Student from Room")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        allocated = False
        for room_no in rooms:
            if rooms[room_no] is None:
                rooms[room_no] = name
                print(f"Room {room_no} allocated to {name}.")
                allocated = True
                break
        if not allocated:
            print("Sorry! All rooms are occupied.")
    elif choice == 2:
        print("\nRoom Status:")
        for room_no, occupant in rooms.items():
            if occupant is None:
                print(f"Room {room_no}: Free")
            else:
                print(f"Room {room_no}: Occupied by {occupant}")
    elif choice == 3:
        room_no=int(input("enter the room number of student to remove:"))
        if room_no in rooms is not None:
            print(f"Student {rooms[room_no]} removed from Room {room_no}.")
            rooms[room_no] = None
        else:
            print("room is already free.")
    elif choice == 4:
        print("Exiting the program.")
        break        
    else:
        print("Invalid choice.")