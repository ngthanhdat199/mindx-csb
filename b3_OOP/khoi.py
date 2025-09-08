# main.py
# Quan ly hoc sinh (ten, tuoi, gioi tinh)
# OOP: object oriented programming (lap trinh huong doi tuong)

# class: Student
# object: student_1, student_2
from student import Student
student_1 = Student("Khoi", 14, "Nam")
student_2 = Student("An", 16, "Nu")

# Gioi thieu hoc sinh
student_1.gioi_thieu()
student_2.gioi_thieu()