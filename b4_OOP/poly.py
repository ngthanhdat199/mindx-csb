# Trong lập trình hướng đối tượng có một tính chất rất quan trọng gọi là đa hình (polymorphism).
# 👉 Đa hình nghĩa là: cùng một hành động (ở đây là speak) nhưng mỗi đối tượng (con vật khác nhau) sẽ thực hiện theo cách riêng của nó.
class Animal:
    def speak(self):
        pass   # chưa định nghĩa cụ thể, chỉ để chỗ trống

class Dog(Animal):
    def speak(self):
        return "Woof!"   # Chó thì kêu gâu gâu

class Cat(Animal):
    def speak(self):
        return "Meow"    # Mèo thì kêu meo meo

class Cow(Animal):
    def speak(self):
        return "Moo"     # Bò thì kêu ò ò

# Cùng gọi một lệnh: animal.speak().
# Nhưng:
# Nếu animal là chó → kêu "Woof!"
# Nếu animal là mèo → kêu "Meow"
# Nếu animal là bò → kêu "Moo"
# 💡 Đây chính là đa hình: cùng một hàm speak(), nhưng mỗi loài vật lại có cách thực hiện khác nhau.

# Tạo các đối tượng từ các lớp con
dog = Dog() 
cat = Cat()
cow = Cow()

for animal in (dog, cat, cow):
    print(animal.speak())   # Gọi hàm speak() của từng con vật