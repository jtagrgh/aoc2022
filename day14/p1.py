grid = [["." for _ in range(1000)] for _ in range(1000)]
lines = []
lowest_y = 0

with open("in.txt", "r") as f:
	for line in f:
		points = line.split("->")
		points = [point.strip() for point in points]
		for one, two, in zip(points[0:-1], points[1:]):
			x_end = int(one.split(",")[0])
			x_start = int(two.split(",")[0])
			y_start = int(one.split(",")[1])
			y_end = int(two.split(",")[1])
			lowest_y = max(y_end, lowest_y)
			if x_start == x_end:
				for y in range(min(y_start,y_end), max(y_start, y_end) +1):
					grid[x_start][y] = "#"
			elif y_start == y_end:
				for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
					grid[x][y_start] = "#"

placed = 0

def drop_sand():
	sand_pos = [500,0]
	while(1):
		if sand_pos[1] > lowest_y:
			return "filled"
		elif grid[sand_pos[0]][sand_pos[1] + 1] == ".":
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
			return "placed"

ret = drop_sand()
while(ret != "filled"):
	ret = drop_sand()

print(placed)















