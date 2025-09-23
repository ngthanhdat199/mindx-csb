input = ['b', 'r', 'b', 'w', 'w', 'r']

def sort(input):
    output = []
    for x in input:
        if x == 'r':
            output.append('r')
    for x in input:
        if x == 'w':
            output.append('w')
    for x in input:
        if x == 'b':
            output.append('b')
    return output

print(sort(input))