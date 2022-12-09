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

h = point(l//2,l//2)
l = point(l//2,l//2)

for cmd in lines:
	for _ in range(int(cmd[1])):
		if cmd[0] == 'U':
			h.y -= 1
		elif cmd[0] == 'D':
			h.y += 1
		elif cmd[0] == 'L':
			h.x -= 1
		elif cmd[0] == 'R':
			h.x += 1

		touching = False
		surrounding = [[i,j] for i in range(h.x - 1, h.x + 2) for j in range(h.y - 1, h.y + 2)]
		if [t.x, t.y] in surrounding: 
			touching = True;
		if not touching:
			x_dif = h.x - t.x
			y_dif = h.y - t.y

			if x_dif != 0: x_dif /= abs(x_dif)
			if y_dif != 0: y_dif /= abs(y_dif)

			t.x += int(x_dif)
			t.y += int(y_dif)

		grid[t.y][t.x] += 1

sum = 0

for i in range(l):
	for j in range(l):
		if grid[i][j] >= 1: 
			sum += 1

# for x in grid:
# 	print(x)

print(sum)












