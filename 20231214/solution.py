import sys


def reverse_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def score_me(grid):
    weight = len(grid)
    sum = 0
    for row in grid:
        zeroes = "".join(row).count("O")
        sum += zeroes * weight
        weight -= 1
    return sum

def part1(grid):
    rg = reverse_grid(grid)
    new_rg = []    
    for row in rg:
        row = "".join(row)
        new_row = ""
        ix = 0
        for clearing in row.split("#"):
            new_row = new_row + "#" if ix > 0 else new_row
            new_row += "".join(sorted(clearing, reverse=True))
            ix += 1
        new_rg.append(list(new_row))

    roll_down_grid = reverse_grid(new_rg)
    return score_me(roll_down_grid)
    

if __name__ == "__main__":
    with open(sys.argv[1]) as f:  # python solution.py test1.txt
        data = f.read()
    grid = [list(line) for line in data.splitlines()]

    print('part1 answer', part1(grid))
