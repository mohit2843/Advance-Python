students = {}
courses = {}
enrolment = {}
grades = {}
attendance_record = {}
view_attendance = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    section = input("Enter section: ")
    students[roll] = {"name": name, "section": section}
    print("Student added successfully.")

def add_course():
    code = input("Enter course code: ")
    cname = input("Enter course name: ")
    courses[code] = cname
    print("Course added successfully.")

def enrol_student():
    roll = input("Enter roll number: ")
    code = input("Enter course code: ")

    if roll in students and code in courses:
        enrolment.setdefault(roll, []).append(code)
        print("Student enrolled successfully.")
    else:
        print("Invalid roll number or course code.")

def view_student_report():
    roll = input("Enter roll number: ")

    if roll in students:
        print("\nName:", students[roll]["name"])
        print("Section:", students[roll]["section"])
        print("Enrolled Courses:")

        for code in enrolment.get(roll, []):
            print(code, "-", courses[code])

        print("Grades:")
        for key, value in grades.items():
            if key[0] == roll:
                print(key[1], ":", value)

    else:
        print("Invalid roll number.")

def drop_course():
    roll = input("Enter roll number: ")
    code = input("Enter course code: ")

    if roll in enrolment and code in enrolment[roll]:
        enrolment[roll].remove(code)
        print("Course dropped successfully.")
    else:
        print("Student not enrolled in this course.")

def assign_grade():
    roll = input("Enter roll number: ")
    code = input("Enter course code: ")
    grade = input("Enter grade: ")

    if roll in enrolment and code in enrolment[roll]:
        grades[(roll, code)] = grade
        print("Grade assigned successfully.")
    else:
        print("Student not enrolled in this course.")

def course_wise_report():
    code = input("Enter course code: ")

    if code in courses:
        print("\nCourse:", courses[code])
        print("Enrolled Students:")

        for roll, course_list in enrolment.items():
            if code in course_list:
                print(roll, "-", students[roll]["name"])
    else:
        print("Invalid course code.")

def record_attendance():
    roll = input("Enter roll number: ")
    code = input("Enter course code: ")
    status = input("Enter attendance (Present/Absent): ")

    if roll in enrolment and code in enrolment[roll]:
        attendance_record[(roll, code)] = status
        print("Attendance recorded successfully.")
    else:
        print("Student not enrolled in this course.")
        
def view_attendance():
    roll = input("Enter roll number: ")
    code = input("Enter course code: ")

    if (roll, code) in attendance_record:
        print("Attendance for", students[roll]["name"], "in", courses[code], ":", attendance_record[(roll, code)])
    else:
        print("No attendance record found for this student and course.")
                

while True:
    print("\n1. Add Student")
    print("2. Add Course")
    print("3. Enrol Student")
    print("4. View Student Report")
    print("5. Drop Course")
    print("6. Assign Grade")
    print("7. Course Wise Report")
    print("8. Record Attendance")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enrol_student()
    elif choice == "4":
        view_student_report()
    elif choice == "5":
        drop_course()
    elif choice == "6":
        assign_grade()
    elif choice == "7":
        course_wise_report()
    elif choice == "8":
        record_attendance()
    elif choice == "9":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")