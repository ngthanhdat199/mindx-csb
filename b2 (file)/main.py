from collections import Counter

grades = [85, 85, 78, 92]

tb = sum(grades) / len(grades)

print(f"The average grade is: {tb:.2f}")

grades.sort()

print("Sorted grades:", grades)

l = len(grades)
mid = l // 2

print("Length of grades:", l)
print("mid:", mid)

if l % 2 == 0:
    median = (grades[mid - 1] + grades[mid]) / 2
else:
    median = grades[mid]

print(f"The median grade is: {median:.2f}")

counter = Counter(grades)
print("Frequency of each grade:", counter)
max_freq = max(counter.values())
print("Maximum frequency:", max_freq)

yv = []
for element, frequency in counter.items():
    if frequency == max_freq:
        yv.append(element)

print("The mode(s) of the grades is/are:", yv)