class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

l = 500
grid = [[0 for _ in range(l)] for _ in range(l)]
k = [point(0,0) for _ in range(10)]

def get_line():
	with open("in.txt", "r") as f:
		for line in f:
			yield line.replace("\n", "").split()

for cmd in get_line():
	for _ in range(int(cmd[1])):
		if cmd[0] == 'U':
			k[0].y -= 1
		elif cmd[0] == 'D':
			k[0].y += 1
		elif cmd[0] == 'L':
			k[0].x -= 1
		elif cmd[0] == 'R':
			k[0].x += 1

		for i, t in enumerate(k[1:], start=1):
			px = k[i-1].x
			py = k[i-1].y
			surrounding = (
				(x,y) \
				for x in range(px - 1, px + 2) \
				for y in range(py - 1, py + 2)
			)
			if not (t.x, t.y) in surrounding:
				x_dif = px - t.x
				y_dif = py - t.y

				if x_dif != 0: x_dif /= abs(x_dif)
				if y_dif != 0: y_dif /= abs(y_dif)

				k[i].x += int(x_dif)
				k[i].y += int(y_dif)

			if i == len(k) - 1:
				grid[t.y][t.x] += 1

sum = 0

for i in range(l):
	for j in range(l):
		if grid[i][j] >= 1: 
			sum += 1

print(sum)












