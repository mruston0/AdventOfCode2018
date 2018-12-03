import io
import itertools

words = open('inputs\\day_2.txt', 'r')
lines = words.read().splitlines()       # Prevents trailing newline characters

def part_1():
    a = 0
    b = 0
    for l in lines:
        s = sorted(l)
        print(f"{l} -> {s}")
        has_counted_a = False
        has_counted_b = False
        for k, g in itertools.groupby(s):
            g_list = list(g)
            print(f"Key is {k} and group is {g_list}")
            if len(g_list) == 2 and not has_counted_a:
                a = a + 1
                has_counted_a = True
            if len(g_list) == 3 and not has_counted_b:
                b = b + 1
                has_counted_b = True
    print(f"Checksum is {a} * {b} {a * b}")

def part_2():
    for l in lines:
        for check_string in lines:
            common_letters = []
            uncommon_letters = []
            num_differences = 0
            for index, val in enumerate(l):
                if val != check_string[index]:
                    num_differences += 1
                    uncommon_letters.append(val)
                else:
                    common_letters.append(val)
                if num_differences > 1:
                    break   # Don't need to continue checking this string.
            if num_differences == 1:
                print(f"Matching boxes {l} and {check_string} and common letters are {''.join(common_letters)} uncommon {''.join(uncommon_letters)}")                

    
part_2()



