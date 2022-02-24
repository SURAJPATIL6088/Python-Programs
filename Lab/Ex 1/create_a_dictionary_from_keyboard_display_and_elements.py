a = int(input("Enter the size : "))

marks = {}

for i in range(a):
    student_name = input("Enter student name: ")
    student_mark = input("Enter student mark: ")
    marks = {student_name.title():student_mark}

print(marks)