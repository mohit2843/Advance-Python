# 1.Student Grade Management System
# Program that records, updates, and deletes student grades.
# Handle exceptions like invalid student ID, empty grade inputs, and type
# mismatches.

class StudentGradeSystem:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student_id, grade):
        try:
            if not student_id:
                raise ValueError("Student ID cannot be empty.")
            
            grade = float(grade) 
            
            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100.")
                
            self.grades[student_id] = grade
            print(f"Grade for {student_id} updated to {grade}.")
            
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print("An unexpected error occurred:",e)

sys = StudentGradeSystem()
sys.add_grade("S101", "95")
sys.add_grade("S102", "abc")