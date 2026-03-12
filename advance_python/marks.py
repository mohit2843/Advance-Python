n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
highest_marks = max(students.values())
for name, marks in students.items():
    if marks == highest_marks:
        topper = name
        break
print("Highest Marks:", highest_marks)
print("Student with Highest Marks:", topper)