from itertools import zip_longest

lines = []

with open("in.txt", "r") as f:
	for line in f:
		if line != "\n":
			lines.append(eval(line.strip("\n")))

def compare_ints(left, right):
	if left < right:
		return "good"
	elif left == right:
		return "ok"
	else:
		return "bad"

def compare_nones(left, right):
		if left == None and right == None:
			return "ok"
		elif left == None:
			return "good"
		elif right == None:
			return "bad"

def compare_lists(left, right):
	for l, r in zip_longest(left, right):
		if isinstance(l, int) and isinstance(r, int):
			yield compare_ints(l, r)
		elif isinstance(l, list) and isinstance(r, list):
			yield from compare_lists(l, r)
		elif isinstance(l, int) and isinstance(r, list):
			yield from compare_lists([l], r)
		elif isinstance(l, list) and isinstance(r, int):
			yield from compare_lists(l, [r])
		else:
			yield compare_nones(l, r)

good_pairs = 0

for i, (left, right) in enumerate(zip(lines[:-1:2], lines[1::2]), start=1):
	for result in compare_lists(left, right):
		if result == "good":
			good_pairs += i
			print(left, right, "in good order")
			break
		elif result == "bad":
			print(left, right, "in bad order")
			break
		else:
			continue

print(good_pairs)










