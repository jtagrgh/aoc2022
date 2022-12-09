class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

l = 1000

grid = [[0 for _ in range(l)] for _ in range(l)]
lines = []

with open("in.txt", "r") as f:
	for line in f:
		lines.append(line.replace("\n", "").split())

k = [point(l//2,l//2) for _ in range(10)]

for cmd in lines:
	for _ in range(int(cmd[1])):
		if cmd[0] == 'U':
			k[0].y -= 1
		elif cmd[0] == 'D':
			k[0].y += 1
		elif cmd[0] == 'L':
			k[0].x -= 1
		elif cmd[0] == 'R':
			k[0].x += 1

		for n in range(1, len(k)):
			touching = False
			px = k[n-1].x
			py = k[n-1].y
			surrounding = [
				[i,j] \
				for i in range(px - 1, px + 2) \
				for j in range(py - 1, py + 2)
			]
			if [k[n].x, k[n].y] in surrounding: 
				touching = True;
			if not touching:
				x_dif = px - k[n].x
				y_dif = py - k[n].y

				if x_dif != 0: x_dif /= abs(x_dif)
				if y_dif != 0: y_dif /= abs(y_dif)

				k[n].x += int(x_dif)
				k[n].y += int(y_dif)

			if n == len(k) - 1:
				grid[k[n].y][k[n].x] += 1

sum = 0

for i in range(l):
	for j in range(l):
		if grid[i][j] >= 1: 
			sum += 1

print(sum)












