# Tìm kiếm tuần tự

def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Tìm kiếm nhị phân
def binary_search(arr, num):
    if len(arr) == 0:
        return -1
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [3, 6, 1, 8, 4, 5, 7, 2]
num = 7

print("Mảng đã sắp xếp:", arr)
