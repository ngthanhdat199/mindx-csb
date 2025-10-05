# danh sách các phần tử ở trong list meters
# meters = list((1, 2, 3))
# centimeters = list()

# for m in meters:
#     centi = m * 100
#     centimeters.append(centi)

# print("List meters (m):", meters)
# print("List centimeters (cm):", centimeters)



# dictionary (từ điển)
# key -> value (map) (1:1)
# tiếng anh -> tiếng việt
# vi du:
# union -> hợp

# meters = [1,2,3]
# def convert_from_m_to_cm(m):
#     return m * 100

# cm = map(convert_from_m_to_cm, meters)
# # cm = map(lambda m: m * 100, meters)
# print("List centimeters (cm):", list(cm))

# Sử dụng hàm map (ánh xạ) để giải 
# map(function, iterable)
# function: hàm xử lý
# iterable: danh sách các phần tử (list, set, dictionary)

names = ["Alice", "Bob", "Charlie"]
name_lower = map(lambda name: name.lower(), names)
print("Names in lowercase:", list(name_lower))