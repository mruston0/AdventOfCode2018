import numpy
import math

words = open('inputs/day_6.txt', 'r')
lines = words.read().splitlines()       # Prevents trailing newline characters
input = []
for l in lines:
    parsed = l.strip().split(',')
    input.append((int(parsed[0]), int(parsed[1])))

# test input
#input = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]

# Used for displaying test input
owners_to_alpha = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f"
    }

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_owner(x, y, data):
    # owner is the coordinate that has the closest manhattan distance to the given (x, y) coordinate.
    min_distance = 99999
    owner = None
    for index, coordinate in enumerate(data):
        distance = manhattan_distance(coordinate[0], coordinate[1], x, y)
        if distance < min_distance:
            min_distance = distance
            owner = index
        elif distance == min_distance:
            owner = '.'     # return a period if this coordinate has > 1 possible owner.
        if distance == 0:
            owner = index
    return owner

def print_map(input, size_x, size_y):
    print("")
    for y in range(size_y):
        print('')
        for x in range(size_x):
            print(owner_map[x][y], end='')
    print('')
    

plane_size_x = sorted(input, key=lambda x: x[0])[-1][0] + 1
plane_size_y = sorted(input, key=lambda x: x[1])[-1][1] + 1

owner_map = []

for x in range(plane_size_x):
    owner_map.append([])
    for y in range(plane_size_y):
        owner_map[x].append([])
        owner_index = calculate_owner(x, y, input)
        if owner_index != None:
            owner_map[x][y] = owner_index

print_map(owner_map, plane_size_x, plane_size_y)

# Remove coordinates whose ownership could be infinite.
for x in range(plane_size_x):
    for y in range(plane_size_y):
        if x == 0 or x == plane_size_x -1 or y == 0 or y == plane_size_y -1:
            if owner_map[x][y] != ".":
                input[int(owner_map[x][y])] = None

print("Remaining coordinates...")
print(input)

sizes = {}
# Get the size
for x in range(plane_size_x):
    for y in range(plane_size_y):
        owner = owner_map[x][y]
        if owner != None:
            if str(owner) not in sizes:
                sizes[str(owner)] = 0
            sizes[str(owner)] += 1
print(sizes)

max_size = 0
for index, val in enumerate(input):
    if val != None:
        print(f"Size for {val} is {sizes[str(index)]}")
        if sizes[str(index)] > max_size:
            max_size = sizes[str(index)]
print(f"Part One: {max_size} is max size")
    

