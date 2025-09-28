def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

if __name__ == "__main__":
    # print("Please input len of numbers:")
    n = int(input())
    # print("Please input numbers:")
    numbers = list(map(int, input().split()))
    sorted_numbers = selection_sort(numbers)
    print(' '.join(map(str, sorted_numbers)))

