grid = [["." for _ in range(1000)] for _ in range(1000)]
lines = []
lowest_y = 0

with open("in.txt", "r") as f:
	for line in f:
		points = line.split("->")
		points = [point.strip() for point in points]
		for one, two, in zip(points[0:-1], points[1:]):
			x1 = int(one.split(",")[0])
			x2 = int(two.split(",")[0])
			y1 = int(two.split(",")[1])
			y2 = int(one.split(",")[1])
			lowest_y = max(y1, lowest_y)
			if x1 == x2:
				for y in range(min(y1, y2), max(y1, y2) +1):
					grid[x2][y] = "#"
			elif y1 == y2:
				for x in range(min(x1, x2), max(x1, x2) + 1):
					grid[x][y2] = "#"

for i in range(1000):
	grid[i][lowest_y + 2] = "#"

placed = 0

def drop_sand():
	sand_pos = [500,0]
	while(1):
		if grid[sand_pos[0]][sand_pos[1] + 1] == ".":
			sand_pos[1] += 1
		elif grid[sand_pos[0] - 1][sand_pos[1] + 1] == ".":
			sand_pos[0] -= 1
			sand_pos[1] += 1
		elif grid[sand_pos[0] + 1][sand_pos[1] + 1] == ".":
			sand_pos[0] += 1
			sand_pos[1] += 1
		else:
			global placed
			placed += 1
			grid[sand_pos[0]][sand_pos[1]] = "O"
			if sand_pos == [500, 0]:
				return "filled"
			return "placed"

ret = drop_sand()
while(ret != "filled"):
	ret = drop_sand()

print(placed)
