def write():
    with open("grades.txt", "w") as file:
        file.write("Alice 95\n")
        file.write("Bob 92\n")
        file.write("Charlie 78\n")
        file.write("Diana 90\n")

def read():
    with open("grades.txt", "r") as file:
        for line in file:
            print(line.strip())

read()