import sys

NORTH = {"grid": "reverse", "sort": "reverse"}

def tilt_direction(grid, dir):
    rg = reverse_grid(grid) if dir in ['N', 'S'] else grid
    rev_sort = True if dir in ['N', 'W'] else False
    new_rg = []    
    for row in rg:
        row = "".join(row)
        new_row = ""
        ix = 0
        for clearing in row.split("#"):
            new_row = new_row + "#" if ix > 0 else new_row
            new_row += "".join(sorted(clearing, reverse=rev_sort))
            ix += 1
        new_rg.append(list(new_row))
    return reverse_grid(new_rg) if dir in ['N', 'S'] else new_rg


def run_cycle(grid):
    # N-W-S-E
    # Run single cycle
    for dir in ['N', 'W', 'S', 'E']:
        grid = tilt_direction(grid, dir)
    return grid


def reverse_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

def part2(grid, cnt_cycles=1):
    for i in range(cnt_cycles):
        grid = run_cycle(grid)
    return score_me(grid), grid


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

def unpack_grid(grid):
    for row in grid:
        print('.'.join(row))


if __name__ == "__main__":
    with open(sys.argv[1]) as f:  # python solution.py test1.txt
        data = f.read()
    grid = [list(line) for line in data.splitlines()]

    part1_answer = part1(grid)
    print('part1 answer', part1_answer)

    cnt_cycles = int(sys.argv[2])

    part2_answer, part2_grid = part2(grid, cnt_cycles)
    print('part2 answer', part2_answer)
    unpack_grid(part2_grid)
