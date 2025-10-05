# Khởi tạo (khai báo) {} or dict()
my_dict = {}
my_dict = dict()

# Thêm phần tử vào dictionary
my_dict["name"] = "dat" # 0(1)
print("After add:", my_dict)

# Cập nhật phần tử trong dictionary
my_dict["name"] = "dat-123" 
print("After update:", my_dict)

# Truy xuất (truy cập)
print("Access name:", my_dict["name"]) # 0(1)

# Xóa phần tử trong dictionary
del my_dict["name"]
print("After delete:", my_dict)