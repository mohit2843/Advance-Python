#teacher enter marks calculate gpa
class CollegeResult:
    def calculate_gpa(self,marks):
        self.marks = marks
        total_marks = sum(self.marks)
        gpa = total_marks / len(self.marks) / 10
        return gpa

marks = []

total_subject = int(input("enter total number of subjects:"))
for i in range(total_subject):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

gpa = CollegeResult().calculate_gpa(marks)
print(f"Your GPA is: {gpa}")