# Trừu tượng là ẩn đi chi tiết cách thực hiện và chỉ cho người dùng thấy hành động cần quan tâm (tên method)
# Trong Python, tính trừu tượng thường được thể hiện qua lớp cha (superclass) có những phương thức “khung” (chưa định nghĩa rõ ràng), để lớp con tự triển khai.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass # phương thức trừu tượng (chưa có nội dung)

# Dog đóng vai trò là lớp cha trừu tượng.
# speak() được định nghĩa nhưng không làm gì (pass). Điều này nói rằng “mọi con chó đều có thể phát ra âm thanh, nhưng cách kêu thế nào thì chưa biết”.

class Shiba(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Woof")

class Husky(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Howl")

# Shiba định nghĩa cụ thể speak() → “Woof”
# Husky định nghĩa cụ thể speak() → “Howl”

# Người dùng chỉ cần biết rằng mọi Dog đều có thể speak(), mà không cần quan tâm cách Shiba hay Husky cài đặt bên trong.
# Đây chính là tính trừu tượng: che giấu phần cài đặt, chỉ để lộ hành vi.