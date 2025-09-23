def intersection(arr1, arr2):
    result = []
    seen = {}
    for num in arr1:
        seen[num] = 1
    
    for num in arr2:
        if num in seen and seen[num] == 1:
            result.append(num)
    
    return result

arr1 = [1, 2, 2, 1, 9291, 10, 30091]
arr2 = [1, 3, 6, 8, 10, 30091]
print(intersection(arr1, arr2))
# em gửi nha thầy, máy em hết pin