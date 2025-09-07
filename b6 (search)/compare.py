def linear_search(arr, x):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == x:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == x:
            return mid, comparisons
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


# ---- Chương trình chính ----
# arr = list(map(int, input("Nhập danh sách số nguyên (cách nhau bằng dấu cách): ").split()))
# x = int(input("Nhập số cần tìm: "))
arr = [10, 23, 45, 70, 11, 15]
x = 70

# Linear Search
pos_linear, comp_linear = linear_search(arr, x)
print(f"\nLinear Search: vị trí = {pos_linear}, số lần so sánh = {comp_linear}")

# Đảm bảo mảng sắp xếp trước khi Binary Search
arr_sorted = sorted(arr)
pos_binary, comp_binary = binary_search(arr_sorted, x)
print(f"Binary Search (trên mảng đã sắp xếp): vị trí = {pos_binary}, số lần so sánh = {comp_binary}")
