import sys
from typing import List, Tuple

"""
1- declare constants for directions, denoting each as a tuple (row, column) incremental from current point
2- locate start coord
3- from start, try each direction to see if next tile is playable (not ., not a tile type that wouldn't match up with the direction)
4- do until you reach start - the resulting length divided by 2 is the max distance from S
"""

NORTH = (-1,0)
EAST = (0,1)
SOUTH = (1,0)
WEST = (0,-1)

def reversedir(dir: Tuple[int,int]):
    return (dir[0]*-1,dir[1]*-1)

Point = Tuple[int,int]
Grid = List[List[str]]

def padd(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])

def gget(g: Grid, p: Point) -> str:
    x,y = p[0], p[1]
    if (y < 0) or (y >= len(g[0])) or (x < 0) or (x >= len(g)):
        return '.'
    return g[x][y]

def connections(tile: str) -> Tuple[Tuple[int,int]]:
    if tile == '-':
        return (EAST,WEST)
    if tile == '|':
        return (NORTH,SOUTH)
    if tile == 'F':
        return (EAST,SOUTH)
    if tile == 'L':
        return (NORTH,EAST)
    if tile == 'J':
        return (NORTH,WEST)
    if tile == '7':
        return (SOUTH,WEST)
    print("unhandled tile encountered: ", tile)
    assert False # This means we did something wrong

def solve(start: Point, grid: Grid):
    visited = [start]
    nextDirs = set([NORTH,SOUTH,EAST,WEST])
    while True:
        print('while true here are nextDirs', nextDirs)
        for d in nextDirs:
            print('current d', d)
            n = padd(visited[-1], d)
            # see if it's a valid tile we can travel to
            tile = gget(grid,n)
            if tile == '.':
                continue
            if tile == 'S':
                return visited
            if reversedir(d) in connections(tile):
                print('reversedir(d)', reversedir(d), 'connections(tile)', connections(tile), 'tile', tile)
                # yes, we can travel here
                nextDirs = set(connections(tile))
                nextDirs.remove(reversedir(d))
                visited.append(n)
                print('nextdir now set to the remaining nextDir for this tile)', nextDirs)
                break

def part1(start: Point, grid: Grid):
    """ Find max distance from start
        Travel from start until return, take this length and divide by 2
    """
    path = solve(start, grid)
    print(f"Part 1: {len(path)/2}")
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f: # python solution.py test1.txt
        data = f.read()
    print(data)
    # map input to grid
    grid = [list(line) for line in data.splitlines()]
    start = None
    for (y,row) in enumerate(grid):
        if 'S' in row:
            start = (y, row.index('S'))
            print(start)
            break
    part1(start, grid) if start is not None else print('No start tile found!')


