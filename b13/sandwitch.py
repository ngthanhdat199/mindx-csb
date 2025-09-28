from collections import deque

# students: [1,1,1,0,0,1]
# sandwiches: [1,0,0,0,1,1]
# output: 3
def count_hungry_students(students, sandwiches):
    count0 = 0
    count1 = 0
    for student in students:
        if student == 0:
            count0 += 1
        else:
            count1 += 1
    
    print(count0, count1)

    for sandwich in sandwiches: 
        if sandwich == 0:
            if count0 > 0:
                count0 -= 1
            else:
                return count1
        else:
            if count1 > 0:
                count1 -= 1
            else:
                return count0
            
    return 0

if __name__ == "__main__":
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    print(count_hungry_students(students, sandwiches))