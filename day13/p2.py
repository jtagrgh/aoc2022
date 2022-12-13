from itertools import zip_longest
from functools import cmp_to_key

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

def compare(left, right):
	for result in compare_lists(left, right):
		if result == "good":
			return 1
		elif result == "bad":
			return -1
		elif result == "ok":
			continue
	return 0

lines.append([[2]])
lines.append([[6]])

lines.sort(key = cmp_to_key(compare), reverse = True)

p1 = lines.index([[2]]) + 1
p2 = lines.index([[6]]) + 1

print(p1 * p2)






