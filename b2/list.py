from collections import Counter

# Input
grades = [85, 85, 78, 10, 10]

# Tinh trung binh 
tb = sum(grades) / len(grades)
print("The average grade is:", tb)

# Tinh trung vi
print("Before grades:", grades)
grades.sort()
print("After grades:", grades)

l = len(grades)
print("Length of grades:", l)

mid = l // 2
print("middle:", mid)

if l % 2 == 0:
    median = (grades[mid - 1] + grades[mid]) / 2
else:
    median = grades[mid]

print("The median grade is:", median)

# Tinh yeu vi
counter = Counter(grades)
print("counter:", counter)

max_freq = max(counter.values())
print("Maximum frequency:", max_freq)

yv = []
for element, frequency in counter.items():
    if frequency == max_freq:
        yv.append(element)

print("yeu vi:", yv)