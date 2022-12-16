from intervaltree import IntervalTree

class sensor:
    pos = ()
    r = 0
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r
    def __eq__(self, another):
        return hasattr(another, 'pos') and self.pos == another.pos
    def __hash__(self):
        return hash(self.pos)
    def __repr__(self):
        return str(self.pos)

sensors = {}

def get_hamilton_distance(p1, p2):
    distance = abs(p1[0] - p2[0])
    distance += abs(p1[1] - p2[1])
    return distance

with open("in.txt", "r") as f:
    for line in f:
        line = line.split()
        line = [l for l in line if any(key in l for key in "xy")]
        line = [int(l.split("=")[1].replace(',', '').replace(':', '')) for l in line]
        sensor_pos = (line[0], line[1])
        beacon_pos = (line[2], line[3])
        new_sensor = sensor(sensor_pos, get_hamilton_distance(sensor_pos, beacon_pos))
        sensors[new_sensor] = [beacon_pos]
        for key in sensors.keys():
            if key == new_sensor:
                continue
            if get_hamilton_distance(key.pos, new_sensor.pos) <= key.r:
                sensors[key].append(new_sensor.pos)

total = 0
Y = 2000000
subtracted_neighbours = set()

y2m = IntervalTree()
for key, value in sensors.items():
    if not get_hamilton_distance(key.pos, (key.pos[0], Y)) <= key.r:
        continue

    for neighbour in value:
        if neighbour[1] == Y and neighbour not in subtracted_neighbours:
            total -= 1
            subtracted_neighbours.add(neighbour)

    y_dif = max(key.pos[1], Y) - min(key.pos[1], Y)
    line_length = abs((key.r * 2 + 1) - y_dif * 2)
    halfs_length = (line_length - 1) // 2
    l = key.pos[0] - halfs_length
    r = key.pos[0] + halfs_length + 1 # Upper bound not included
    y2m.addi(l, r)

y2m.merge_overlaps()
print(y2m)


for interval in y2m:
    total += abs(interval[0] - interval[1])

print(total)














