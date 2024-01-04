import sys

def run_hash(term):
    val=0
    for char in term:
        val += ord(char)
        val = val * 17
        val = val % 256
    print(term, '=', val)
    return val  


if __name__ == "__main__":
    with open(sys.argv[1]) as f:  # python solution.py test1.txt
        data = f.read()
        sum = 0
        for term in data.split(','):
            sum += run_hash(term)

    print('part1 answer', sum)

