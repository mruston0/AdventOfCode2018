import numpy
import math

words = open('inputs\\day_6.txt', 'r')
lines = words.read().splitlines()       # Prevents trailing newline characters
input = []
for l in lines:
    parsed = l.strip().split(',')
    input.append((int(parsed[0]), int(parsed[1])))

# test input
input = [(1, 2), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_owner(x, y, data):
    min_distance = 99999
    owner = None
    for index, coordinate in enumerate(data):
        distance = manhattan_distance(coordinate[0], coordinate[1], x, y)
        print(f"Distance between {x}, {y} and {coordinate[0]},{coordinate[1]} is {distance}")
        if distance < min_distance:
            min_distance = distance
            owner = index
        elif distance == min_distance:
            owner = '.'     # dot means conflict.min_distance
        if distance == 0:
            owner = "*"
    print(f"Position {x},{y} is owned by {owner}")
    return owner
    

#plane_size_x = sorted(input, key=lambda x: x[0])[-1][0]
#plane_size_y = sorted(input, key=lambda x: x[1])[-1][1]

plane_size_x = 10
plane_size_y = 10

owner_map = []

for x in range(plane_size_x):
    owner_map.append([])
    for y in range(plane_size_y):
        owner_map[x].append([])
        owner_index = calculate_owner(x, y, input)
        if owner_index != None:
            owner_map[x][y] = owner_index

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in owner_map]))

# ## We need to remove owners who are infinite, so go around the outside edge of hte plane
# for x in range(plane_size_x):
#     for y in range(plane_size_y):
#         if x == 0 or x == plane_size_x -1 or y == 0 or y == plane_size_y -1:
#             if owner_map[x, y] != None:
#                 input[int(owner_map[x, y])] = None
# print("Remaining...")
# print(input)

# sizes = {}
# # Get the size
# for x in range(plane_size_x):
#     for y in range(plane_size_y):
#         owner = owner_map[x,y]
#         if owner != None:
#             if str(owner) not in sizes:
#                 sizes[str(owner)] = 0
#             sizes[str(owner)] += 1
# print(sizes)
        
    

