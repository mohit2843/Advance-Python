#2 empty set
my_set1 = set()
my_set2= set()
n= input("enter number of students:")
for i in range(int(n)):
    name = input("enter student name:")
    my_set1.add(name)
    
    if name in my_set1:
        print("name",name)
    else:
        print("name not found")
print("student names are:", my_set1)
print("number of students are:", len(my_set1))
print("empty set is:", my_set2)
