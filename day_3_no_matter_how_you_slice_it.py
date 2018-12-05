import numpy
import re

words = open('inputs\\day_3.txt', 'r')
lines = words.read().splitlines()       # Prevents trailing newline characters

def parse_line(line: str):
    parts = re.split(' |,|:|x', line) 
    x = parts[2]
    y = parts[3]
    size_x = parts[5]
    size_y = parts[6]
    
    val = {}
    val['id'] = parts[0]
    val["x"] = int(x)
    val["y"] = int(y)
    val["size_x"] = int(size_x)
    val["size_y"] = int(size_y)
    return val
    
master_array = numpy.zeros((1000, 1000))        # Initialize an 1000x1000 array with 0's
parsed_data = []
for line in lines:
    d = parse_line(line)
    parsed_data.append(d)
    for i in range(d['size_x']):                     # Set this new array's values
        for j in range(d['size_y']):
            master_array[ d['x'] + i, d['y'] + j ] += 1

# Part 1: Count all of the squares of the array with a value > 1
squares = 0
for x in master_array:
    for y in x:
        if y > 1:
            squares += 1
print(f"Total overlapping squares {squares}")
    
# Part 2: Identify one claim that does not overlap a single square inch of fabric
for data in parsed_data:
    x = data['x']
    y = data['y']
    size_x = data['size_x']
    size_y = data['size_y']

    count = 0
    for i in range(size_x):
        for j in range(size_y):
            if master_array[x + i, y + j] == 1:
                count += 1

    if count == size_x * size_y:
        print(f"Orphaned claim is {data}")
            
            