import sys


def interpret_line(line):
    # print('line', line, 'has', [len(springs) for springs in line.split('.') if len(springs)>0])
    return [len(springs) for springs in line.split('.') if len(springs)>0] 

def unknown_chars(line):
    idx, unk_chars = 0, []
    while(idx!=-1):
        idx = line.find('?', idx)
        if idx!=-1: 
            unk_chars.append(idx)
            idx+=1
    return unk_chars

def map_char(c):
    return '.' if c=='0' else '#'

def get_all_binary_nums(num):
    bins = []
    for i in range(2**num):
        # print(i, bin(i))
        bstr = str(bin(i))[2:]
        bstr_pad = bstr.zfill(num)
        bins.append([map_char(char) for char in bstr_pad])
    return bins

def replace_char(ix, char, s):
    sl = list(s)
    sl[ix] = char
    return ''.join(sl)

def find_arrangements(springs, groups):
    # brute force
    # 1- how many ?
    unk = unknown_chars(springs)
    # print(springs, 'has', len(unk), 'unknown chars')
    
    # 2- convert to binary
    bins = get_all_binary_nums(len(unk))

    # 3 - find all lines that match groups
    possibilities = []
    for b in bins:
        one_possibility = springs
        for i, c in enumerate(unk):
            # print(i,c)
            one_possibility=replace_char(c, b[i], one_possibility)
            # print(one_possibility)
            # print(c, i)
        # print(one_possibility)
        op_works = interpret_line(one_possibility)
        if (op_works==groups):
            possibilities.append(one_possibility)

    return possibilities


if __name__ == '__main__':
    with open(sys.argv[1]) as f: # python solution.py test.txt
        lines = f.readlines()

    arrangements = []
    cnt_arr = 0
    for line in lines:
        springs, groups = line.strip().split(' ')
        groups = [int(group) for group in groups.split(',')]
        arrangements = find_arrangements(springs, groups)
        print('springs', springs, 'with groups', groups, 'has', len(arrangements), 'possibilities.  They are', arrangements)
        cnt_arr += len(arrangements)

        # x = interpret_line('#.#.###')
        # y = unknown_chars('???#.#?##.?')
        # print(x, y)
        # print(bin(2), bin(4), bin(16), bin(32), bin(64), bin(65), bin(127), bin(128))
        
    print('There are a total of', cnt_arr, 'arrangements.')