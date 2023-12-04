# read input.txt
# export AOC_SESSION=....
# aocd > input.txt
import re

file = open('input.txt', 'r')
lines = file.readlines()
line_answer = []
line_input = []

string_digit_mappings = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

strings_or_nums = ['1', 'one', '2', 'two', '3', 'three', '4', 'four', '5', 'five', '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine']
mappings = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9']

def convert_string_digits(line):
    new_line = line
    for k, v in string_digit_mappings.items():
        new_line = new_line.replace(k, v)
    return new_line

def find_first_match(s, _s_):
    pattern = "|".join(map(re.escape, _s_)) # combine all substrings into one pattern
    match = re.search(pattern, s) # find all matches
    return match.group() if match else None # return the (first or) last match

def find_last_match(s, _s_):
    last_index = -1
    last_substring = None
    for substring in _s_:
        index = s.rfind(substring)
        if index > last_index:
            last_index = index
            last_substring = substring
    return last_substring

def get_only_digits(line):
    return list(filter(lambda i: i.isdigit(), line))

def __process_line(line):
    converted = convert_string_digits(line)
    digits_only = get_only_digits(converted)

def process_line(line):
    first_num = mappings[strings_or_nums.index(find_first_match(line, strings_or_nums))]
    last_num = mappings[strings_or_nums.index(find_last_match(line, strings_or_nums))]
    return first_num + last_num

for line in lines:
    la = int(process_line(line))
    line_answer.append(la)
    line_input.append((line, la))

# DEBUG
# print(line_input)
# print(line_answer)
print("The answer is: ", sum(line_answer))

# Test case  (58)
print("Test result: ", process_line('five2jzsconeightm'), "should be 58")