#event tracker system
entered_std = set()
entered_date_time=set()
rejected_std = set()

n = int(input("Enter entry attempts: "))
for i in range(n):
    name= input("enter the name of student:")
    new_name = name.lower()
    if new_name in entered_std:
        print(name,"name already exists, enter a different name")
        new_name =new_name.upper()
        rejected_std.add(name)
    date = input("enter the date of entry:")
    if name in entered_std:
        print(name,"name already exists, enter a different name")
        
        rejected_std.add(name)
    else:
        print(name,"is allowed to enter")
        entered_std.add(name)
        
print("event tracker") 

print("total people entered:") 
for name in entered_std:
    print(name)      
print("allowed people:", entered_std) 
print("rejected people:", rejected_std)