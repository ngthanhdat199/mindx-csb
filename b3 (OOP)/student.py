# student.py
class Student:
    # Initialize
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def gioi_thieu(self):
        print(f"Ten: {self.name}, Tuoi: {self.age}, Gioi tinh: {self.gender}")