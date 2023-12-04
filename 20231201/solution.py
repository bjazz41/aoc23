# read input.txt
file = open('input.txt', 'r')
lines = file.readlines()
line_answer = []

def get_only_digits(line):
    return list(filter(lambda i: i.isdigit(), line))

def process_line(line):
    digits_only = get_only_digits(line)
    return digits_only[0]+digits_only[-1]

for line in lines:
    line_answer.append(int(process_line(line)))

print(sum(line_answer))