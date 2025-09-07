class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sound = "Woof!"

    def get_description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self):
        print(self.__sound)

# Them thuoc tinh height
class Shiba(Dog):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def speak(self):
        print("Shiba wolf!")

    
# Them thuoc tinh but
class Corgi(Dog):
    def __init__(self, name, age, but):
        super().__init__(name, age)
        self.but = but