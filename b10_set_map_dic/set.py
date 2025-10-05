# Khai báo set {}
fruit_basket = {"apple", "banana", "orange"}

# Truy cập phần tử trong set
for fruit in fruit_basket:
    print(fruit)

# Thêm 1 phần tử vào set
fruit_basket.add("mango")  # 0(1) - Thêm một phần tử
print("After add:", fruit_basket)

# Thêm nhiều phần tử vào set
fruit_basket.update(["grape", "kiwi"])  # 0(k) - Thêm nhiều phần tử
print("After update:", fruit_basket)

# Xoá 1 phần tử khỏi set
fruit_basket.remove("melon")  # 0(1) - Xoá một phần tử, lỗi nếu phần tử không tồn tại
print("After remove:", fruit_basket)

fruit_basket.discard("melon")  # 0(1) - Xoá một phần tử, không lỗi nếu phần tử không tồn tại
print("After discard:", fruit_basket)

A = {"bóng đá", "cầu lông", "bơi lội"}
B = {"cầu lông", "bóng rổ", "tennis"}

# Phép hợp
C = A | B 
print("Phép hợp A và B:", C)
C = A.union(B)
print("Phép hợp A và B:", C)

# Phép giao
C = A & B
print("Phép giao A và B:", C)
C = A.intersection(B)
print("Phép giao A và B:", C)

# Phép trừ
C = A - B
print("Phép trừ A và B:", C)
C = A.difference(B)
print("Phép trừ A và B:", C)