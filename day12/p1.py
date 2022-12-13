import heapq

g_iter = 1

start = 0
end = 0

lines = []
with open("in.txt", "r") as f:
	for line in f:
		row = [c for c in line.strip("\n")]
		row_tup = [(99,-1)]
		for c in row:
			if c == "S":
				start = g_iter
				c = "z"
			elif c == "E":
				end = g_iter
				c = "z"
			c_ord = ord(c) - ord('a')
			row_tup.append((c_ord, g_iter))
			g_iter += 1
		row_tup.append((99,-1))
		lines.append(row_tup)

zeros = [(99,-1) for _ in lines[0]]
lines.append(zeros)
lines.insert(0, zeros)

# for line in lines:
# 	print(line)

graph = {}

for i, line in enumerate(lines[1:-1], start=1):
	for j, point in enumerate(line[1:-1], start=1):
		graph[point[1]] = set()
		neighbours = [lines[i-1][j], lines[i+1][j], lines[i][j-1], lines[i][j+1]]
		for n in neighbours:
			if point[0] - n[0] >= -1:
				graph[point[1]].add((n[1], n[0] - point[0]))

visited = set()
distances = []
table = {key: 0 if key == start else 9999999 for key in graph.keys()}
heapq.heappush(distances, (0, start))

while(end not in visited):
	curr = heapq.heappop(distances)
	if (curr in visited): continue
	for n in graph[curr[1]]:
		if (curr[0] + 1 < table[n[0]]):
			new_dist = curr[0] + 1
			table[n[0]] = new_dist
			heapq.heappush(distances, (new_dist, n[0]))

	visited.add(curr[1])
 
print("best", table[end])











