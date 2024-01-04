import sys
sys.setrecursionlimit(1000000)

MOVEMENTS = [(0,1), (0,-1), (1,0), (-1,0)]
DIRS = ['E', 'W', 'S', 'N']
PATHS = {
    '.': {'E': ['E'], 'W': ['W'], 'S': ['S'], 'N': ['N']},
    '-': {'E': ['E'], 'W': ['W'], 'S': ['E', 'W'], 'N': ['E', 'W']},
    '|': {'E': ['N', 'S'], 'W': ['N', 'S'], 'S': ['S'], 'N': ['N']},
    '/': {'E': ['N'], 'W': ['S'], 'S': ['W'], 'N': ['E']},
    '\\': {'E': ['S'], 'W': ['N'], 'S': ['E'], 'N': ['W']},
}

def follow_path(start, grid):
    charged = set()
    def charge(x, y, dir):
        # print('charging', x, y, dir)
        if (x, y, dir) in charged:
            return
        charged.add((x, y, dir))
        point = grid[x][y]
        # print('produces', PATHS[point][dir])
        for next_dir in PATHS[point][dir]:
            next_move = MOVEMENTS[DIRS.index(next_dir)]
            nx = x + next_move[0]
            ny = y + next_move[1]
            if nx in range(len(grid)) and ny in range(len(grid[0])):
                charge(nx, ny, next_dir)
    charge(start[0], start[1], start[2])
    return len(set([(x, y) for x, y, dir in charged]))


def get_edges(rows, cols):
    entry_points = set()
    # left and right edges
    for row in range(rows):
        entry_points.add((row,0,'E'))
        entry_points.add((row,cols-1,'W'))
    # top and bottom edges
    for col in range(cols):
        entry_points.add((0,col,'S'))
        entry_points.add((rows-1,col,'N'))
    return entry_points


def part2(grid):
    entry_points = get_edges(rows=len(grid), cols=len(grid[0]))
    charge_scores = {}
    for entry_point in entry_points:
        charge_scores[entry_point]=follow_path(entry_point, grid)
    # print(charge_scores)
    max_val = (max([val for val in charge_scores.values()]))
    return max_val, charge_scores


if __name__ == "__main__":
    with open(sys.argv[1]) as f:  # python solution.py test1.txt
        data = f.read()
    grid = [list(line) for line in data.splitlines()]

    start = (0, 0, 'E')
    part1 = follow_path(start, grid)

    part2 = part2(grid)

    print('part1 answer', part1)
    print('part2 answer', part2[0])