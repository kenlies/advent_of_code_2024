import re

def solve(part):
	r = open("input.txt", "r")
	pattern = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"
	total = 0

	if part == 1:
		for line in r:
			x = re.findall(pattern, line)
			for mul in x:
				l = list(map(int, re.findall(r'\d+', mul)))
				total = total + l[0] * l[1]

	print(total)
	r.close()

if __name__ == "__main__":
	solve(1)
