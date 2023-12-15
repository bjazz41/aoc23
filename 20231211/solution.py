import sys
from typing import List, Tuple

Point = Tuple[int,int]
Grid = List[List[str]]

def find_empty_rows(grid: Grid, rows=True) -> List:
    empty_ids = []
    working_grid = grid if rows else transpose_grid(grid)
    for i in range(len(working_grid)):
        if all(element == working_grid[i][0] for element in working_grid[i]):
            empty_ids.append(i)
    return empty_ids

def append_empty_rows(grid: Grid, rows=True) -> Grid:
    new_grid = []
    working_grid = grid if rows else transpose_grid(grid)
    for row in working_grid:
        # print(row)
        new_grid.append(row)
        if all(element == row[0] for element in row):
            new_grid.append(row)
    return new_grid if rows else transpose_grid(new_grid)

def append_empties(grid: Grid) -> Grid:
    gr_rows = append_empty_rows(grid)
    # print(gr_rows)
    gr_cols = append_empty_rows(gr_rows, rows=False)
    # print('ran append_empties: orig rows, cols:', len(grid), len(grid[0]), 'new grid: rows, cols', len(gr_cols), len(gr_cols[0]))
    return gr_cols

def transpose_grid(grid: Grid) -> Grid:
    # print('calling transpose_grid on', grid)
    new_grid = []
    cols = len(grid[0])
    for i in range(cols):
        new_row = []
        for row in grid:
            new_row.append(row[i])
            # print('appending', row[i])
        new_grid.append(new_row)
    return new_grid

def find_galaxies(grid: Grid) -> List[Point]:
    galaxies = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            val = grid[i][j]
            if val=='#':
                galaxies.append((i, j))
    return galaxies

def get_dist(pt_a, pt_b):
    return abs(pt_a[0]-pt_b[0]) + abs(pt_a[1]-pt_b[1])

def get_distances(gals, p2=False, boundaries=None):
    size = len(gals)
    dist = []
    for i in range(size):
        for j in range(i+1, size):
            key = f"{gals[i]}, {gals[j]}"
            if p2:
                dist.append({key: get_d2(gals[i], gals[j], boundaries)})
            else: #p1
                dist.append({key: get_dist(gals[i], gals[j])})
    return dist

def get_d2(pt1, pt2, boundaries, multiplier=1000000):
    lat1, lat2 = min(pt1[0], pt2[0]), max(pt1[0], pt2[0])
    lon1, lon2 = min(pt1[1], pt2[1]), max(pt1[1], pt2[1])
    def get_dist_dir(p1, p2, multiplier, boundaries_dir):
        rows_between = list(range(p1, p2+1))
        cnt_boundaries = len(list(set(rows_between) & set(boundaries_dir)))
        # print('rows_between', p1, p2, rows_between, boundaries_dir, cnt_boundaries)
        return abs(p1-p2) + (multiplier-1)*cnt_boundaries
    dist_lat = get_dist_dir(lat1, lat2, multiplier, boundaries[0])
    dist_lon = get_dist_dir(lon1, lon2, multiplier, boundaries[1])
    return dist_lat+dist_lon

def part1(grid):
    grid_clean = append_empties(grid_raw)
    galaxies = find_galaxies(grid_clean)
    distances = get_distances(galaxies)
    # print(galaxies)
    # print(distances)
    sum_dist = sum([sum(list(sub.values())) for sub in distances])
    print(f"The sum of the shortest path between all {len(distances)} pairs of galaxies is {sum_dist}")

def part2(grid):
    empty_rows = find_empty_rows(grid)
    empty_cols = find_empty_rows(grid, False)
    # print(empty_rows, empty_cols)
    my_galaxies = find_galaxies(grid)
    # print(my_galaxies)
    # dist = get_d2((0,3), (1,7), [empty_rows, empty_cols])
    distances = get_distances(my_galaxies, p2=True, boundaries=[empty_rows, empty_cols])
    sum_dist = sum([sum(list(sub.values())) for sub in distances])
    print(f"The sum of the shortest path between all {len(distances)} pairs of galaxies is {sum_dist}")

if __name__ == '__main__':
    with open(sys.argv[1]) as f: # python solution.py test.txt
        data = f.read()
    # print(data)
    # map input to grid
    grid_raw = [list(line) for line in data.splitlines()]
    part1(grid_raw)
    part2(grid_raw)

    # print('grid_clean:', grid_clean)

    """
    For part2, need to re-do this so we calc the galaxy points using the original grid
    Then keep a tally of the rows, cols which are all empty
    When calculating the distance between each galaxy, note how many horizontal and vertical steps are required, and the boundaries that would need to be crossed,
    appending the 1mm for each empty row/col depending
    """