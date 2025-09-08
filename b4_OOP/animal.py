# Tinh đa hình

# Class cha
class Animal:
    def speak(self):
        return "Unknown"

# Class dog
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Class cat
class Cat(Animal):
    def speak(self):
        return "Meow"
    
# Class cow
class Cow(Animal):
    def speak(self):
        return "Moo"


dog = Dog()
print("dog", dog.speak())
cat = Cat()
print("cat", cat.speak())
cow = Cow()
print("cow", cow.speak())
