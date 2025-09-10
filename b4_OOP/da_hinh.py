# Trong lập trình hướng đối tượng, điều này có nghĩa là cùng một tên phương thức (method) nhưng khi gọi trên những đối tượng khác nhau thì nó có cách thực thi khác nhau.

class Dog:
    tail = "long"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sound = "Woof!"
    def get_description(self):
        return f"{self.name} is {self.age} years old."
    def speak(self):
        return self.__sound

class Corgi(Dog):
    tail = "short"
    def __init__(self, name, age):
        super().__init__(name, age)
    def get_description(self):
        return f"{self.name} is a Corgi and is {self.age} years old."


# Dog có phương thức get_description() → trả về mô tả cơ bản.
# Corgi cũng có get_description() → nhưng được viết lại (override) để trả về thông tin khác.

# Example
dogs = [Dog("Buddy", 5), Corgi("Luna", 3)]
for dog in dogs:
    print(dog.get_description())
