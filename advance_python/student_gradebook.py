#student gradebook
def calculate_gradebook(name, marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    grade = ""
    
    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 80:
        grade = "B"
    elif average_marks >= 70:
        grade = "C"
    elif average_marks >= 60:
        grade = "D"
    else:
        grade = "F"
    print("student name:", name)
    print("Total Marks:", total_marks)
    print("Average Marks:", average_marks)
    print("Grade:", grade)

student_name = input("Enter the student's name: ")
marks = []
num_subjects = int(input("Enter the number of subjects: "))
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark) 
calculate_gradebook(student_name, marks)