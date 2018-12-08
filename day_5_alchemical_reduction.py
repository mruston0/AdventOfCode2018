words = open('inputs/day_5.txt', 'r')
input = words.read()

import string

def reduce_chemical(line: str) -> str:
    oldline = None
    while True:
        oldline = line
        for i in range(26):
            line = remove_unit(i, line)
        if oldline == line:
            break
    return line

def remove_unit(char_index, input):
    input = input.replace(string.ascii_lowercase[char_index] + string.ascii_uppercase[char_index], "")
    input = input.replace(string.ascii_uppercase[char_index] + string.ascii_lowercase[char_index], "")
    return input

# Test solution with the example case
result = reduce_chemical("dabAcCaCBAcCcaDA")
assert result == "dabCBAcaDA", "Test case fails."

result = reduce_chemical(input)
print(f"Length of resulting chemical is {len(result)}")

# We can use the input from Part 1 in Part 2.
input_round_two = result
shortest_length = len(input_round_two)
for i in range(26):
    initial_reduce = input_round_two.replace(string.ascii_lowercase[i], "").replace(string.ascii_uppercase[i], "")
    result = reduce_chemical(initial_reduce)
    if len(result) < shortest_length:
        shortest_length = len(result)
print(f"The shortest string we can produce is {shortest_length}")
