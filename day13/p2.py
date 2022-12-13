from itertools import zip_longest
from functools import cmp_to_key

lines = []

with open("in.txt", "r") as f:
	for line in f:
		if line != "\n":
			lines.append(eval(line.strip("\n")))

def compare_lists(left, right):
	for l, r in zip_longest(left, right):
		match l, r:
			case int(), int(): 
				if r - l != 0: yield r - l
			case None, _:
				yield 1
			case _, None:
				yield -1
			case list(), list():
				yield from compare_lists(l, r)
			case int(), list():
				yield from compare_lists([l], r)
			case list(), int():
				yield from compare_lists(l, [r])

lines.append([[2]])
lines.append([[6]])

lines.sort(key = cmp_to_key(lambda l, r: next(compare_lists(l,r))), reverse = True)

p1 = lines.index([[2]]) + 1
p2 = lines.index([[6]]) + 1

print(p1 * p2)






