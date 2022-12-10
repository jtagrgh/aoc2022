def next_line():
	with open("in.txt", "r") as f:
		for line in f:
			cmd = line.split()
			if cmd[0] == "addx":
				yield ["noop"]
			yield cmd;

cycle = 1
total = 1
strength = 0

for line in next_line():
	cycle += 1
	if line[0] == "addx":
		total += int(line[1])

	if cycle in (20, 60, 100, 140, 180, 220):
		strength += cycle * total

print(strength)