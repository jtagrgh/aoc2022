from collections import deque


def cubes():
    with open('in.txt', 'r') as f:
        for line in f:
            yield eval(line.strip())

def neighbours(cube):
    cx = cube[0]
    cy = cube[1]
    cz = cube[2]
    neighbours = []
    for x in range(cx-1,cx+2,2):
        neighbours.append((x,cy,cz))
    for y in range(cy-1,cy+2,2):
        neighbours.append((cx,y,cz))
    for z in range(cz-1,cz+2,2):
        neighbours.append((cx,cy,z))
    return neighbours

cubes_set = {}

for cube in cubes():
    cubes_set[cube] = 6
    for neighbour in neighbours(cube):
        if neighbour in cubes_set:
            cubes_set[neighbour] -= 1
            cubes_set[cube]-=1

max_pocket = 1100
pockets = []
visited_starts = set()

for cube in cubes_set:
    for start in neighbours(cube):
        if start in cubes_set or start in visited_starts:
            continue

        visited_starts.add(start)

        visited = set()
        pocket = []
        search = deque()
        search.append(start)
        pocket_len = 0

        while search and pocket_len < max_pocket:
            next = search.pop()
            pocket.append(next)
            pocket_len+=1
            visited.add(next)
            for n in neighbours(next):
                if n not in cubes_set and n not in visited:
                    visited.add(n)
                    search.append(n)
        
        if pocket_len < max_pocket:
            for point in pocket:
                visited_starts.add(point)
            pockets.extend(pocket)


for pocket in pockets:
    for neighbour in neighbours(pocket):
        if neighbour in cubes_set:
            cubes_set[neighbour] -= 1

print(sum(cubes_set.values()))
