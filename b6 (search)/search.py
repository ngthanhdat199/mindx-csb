# Tìm kiếm tuần tự
def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Tìm kiếm nhị phân
def binary_search(arr, num):
    # con trỏ trái
    left = 0 
    # con trỏ phải
    right = len(arr) - 1
    while left <= right:
        # con trỏ giữa
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1
