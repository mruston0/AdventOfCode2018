import io
import itertools

def part_one():
    file = open('inputs\\day_1_part_1.txt', 'r')
    total = 0
    for line in file:
        total = total + int(line)
    print(f'Part 1 Total {total}')

def part_two():
    file = open('inputs\\day_1_part_1.txt', 'r')
    observed_frequencies = {0}
    total = 0
    for line in itertools.cycle(file):
        total = total + int(str.strip(line))
        if total in observed_frequencies:
            print(f"Frequency {total} has been seen twice.")
            break
        #print(f'Line {str.strip(line)}. Observed: {total}')
        observed_frequencies.add(total)

part_two()
    

    

