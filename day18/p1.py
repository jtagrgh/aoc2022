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
    side_count = 6
    for neighbour in neighbours(cube):
        if neighbour in cubes_set:
            cubes_set[neighbour] -= 1
            side_count-=1

    cubes_set[cube] = side_count

print(sum(cubes_set.values()))
