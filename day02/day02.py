import copy

def solve(part):
	f = open("input.txt", "r")
	total = 0
	for reactor in f:
		safe = True
		levels = list(map(int, reactor.split()))
		if levels[0] > levels[1]:
			# negate the list if its decreasing:
			# then we are only workin with increasing lists
			levels = [-x for x in levels]

		for idx in range(len(levels) - 1):
			diff = levels[idx + 1] - levels[idx]
			if not (diff >= 1 and diff <= 3):
				safe = False
				break
		
		if part == 2 and safe is False:
			for index in range(len(levels)):
				safe = True
				levels_copy = copy.deepcopy(levels)
				levels_copy.pop(index)
				if levels_copy[0] > levels_copy[1]:
					levels_copy = [-x for x in levels_copy]
				for idx in range(len(levels_copy) - 1):
					diff = levels_copy[idx + 1] - levels_copy[idx]
					if not (diff >= 1 and diff <= 3):
						safe = False
						break
				if safe == True:
					break
		
		if safe == True:
			total = total + 1

	print(total)
	f.close()

if __name__ == "__main__":
	solve(1)
	solve(2)