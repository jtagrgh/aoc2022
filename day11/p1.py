from functools import partial

class monkey:
	inspects = 0
	def __init__(self, items=[], op=lambda x:1, test=lambda x:True, t_i=0, f_i=0):
		self.items = items
		self.op = op
		self.test = test
		self.t_i = t_i
		self.f_i = f_i

def next_line():
	with open("in.txt", "r") as f:
		for line in f:
			yield line.split()

monkeys = []
monkeys.append(monkey())
i = 0

for line in next_line():
	if len(line) == 0:
		monkeys.append(monkey())
		i += 1
	elif line[0] == "Starting":
		monkeys[i].items = [int(i.strip(',')) for i in line[2:]]
	elif line[0] == "Operation:":
		if line[-1] == "old":
			if line[-2] == '+':
				monkeys[i].op = lambda x: x + x
			elif line[-2] == '*':
				monkeys[i].op = lambda x: x * x
		else:
			mod = int(line[-1])
			if line[-2] == '+':
				monkeys[i].op = partial(lambda mod, x: x + mod, mod)
			elif line[-2] == '*':
				monkeys[i].op = partial(lambda mod, x: x * mod, mod)
	elif line[0] == "Test:":
		div = int(line[-1])
		monkeys[i].test = partial(lambda div, x: True if x % div == 0 else False, div) 
	elif line[1] == "true:":
		monkeys[i].t_i = int(line[-1])
	elif line[1] == "false:":
		monkeys[i].f_i = int((line[-1]))

for i in range(20):
	for m in monkeys:
		while(1):
			try:
				item = m.items.pop()
				m.inspects += 1
				worry = m.op(item) // 3
				if (m.test(worry)):
					monkeys[m.t_i].items.append(worry)
				else:
					monkeys[m.f_i].items.append(worry)
			except IndexError:
				break		

all_inspects = [m.inspects for m in monkeys]
all_inspects.sort(reverse=True)
print(all_inspects[0] * all_inspects[1])




