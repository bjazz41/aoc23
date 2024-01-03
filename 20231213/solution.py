import sys

def is_reflection(previous, next, pattern, is_vertical):
    # print('is_reflection:', previous, next, pattern, is_vertical)
    if is_vertical:
        while previous >= 0 and next < len(pattern[0]):
            for i in range(len(pattern)):
                if pattern[i][previous] != pattern[i][next]:
                    return False
            previous -= 1
            next += 1
        return True
        
    else: #horizontal
        while previous >= 0 and next < len(pattern):
            if pattern[previous] != pattern[next]:
                return False
            previous -= 1
            next += 1
        return True
        
def find_reflection_point(pattern, is_vertical):
    if is_vertical:
        for i in range(1, len(pattern[0])):
            prev_col, next_col = [], []
            for j in range(0, len(pattern)):
                prev_col.append(pattern[j][i-1])
                next_col.append(pattern[j][i])
            if prev_col == next_col:
                if is_reflection(i-1, i, pattern, is_vertical):
                    return i
    else: #horizontal
        for i in range(1, len(pattern)):
            if pattern[i-1] == pattern[i]:
                if is_reflection(i-1, i, pattern, is_vertical):
                    return i


def analyze_pattern(pattern):
    my_pattern = [list(row) for row in pattern.split()]

    vertical_reflection = find_reflection_point(my_pattern, is_vertical=True) #vertical
    if vertical_reflection:
        return vertical_reflection

    horizontal_reflection = find_reflection_point(my_pattern, is_vertical=False) #horizontal
    if horizontal_reflection:
        return horizontal_reflection * 100

    raise Exception("Can't find reflection!")

def summarize_patterns(patterns):
    sum = 0
    for pattern in patterns:
        cols = len(pattern.split()[0])
        rows = len(pattern.split())
        # print(cols, rows)
        sum += analyze_pattern(pattern)
    return sum

if __name__ == '__main__':
    with open(sys.argv[1]) as f: # python solution.py test1.txt
        patterns = f.read().split('\n\n')
    
    part1 = summarize_patterns(patterns) #returns sum
    print('Part1:', part1)


