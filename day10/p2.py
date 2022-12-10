def next_line():
	with open("in.txt", "r") as f:
		for line in f:
			cmd = line.split()
			if cmd[0] == "addx":
				yield ["noop"]
			yield cmd;

cycle = 1
s_pos = 1
screen = []

for line in next_line():
	if (cycle-1) % 40 in range(s_pos - 1, s_pos + 2):
		screen.append('#')
	else:
		screen.append('.')

	cycle += 1
	if line[0] == "addx":
		s_pos += int(line[1])	


for i, c in enumerate(screen, start=1):
	print(c, end="")
	if i % 40 == 0:
		print()

