import copy
total = 0

def solveByBackTrack(map, y, x, prev, part):
	global total

	if map[y][x] == prev + 1:
		if map[y][x] == 9:
			total += 1
			if part == 1:
				map[y][x] = 99
		# explore below
		if y < len(map) - 1:
			solveByBackTrack(map, y + 1, x, prev + 1, part)
		if y > 0:
			solveByBackTrack(map, y - 1, x, prev + 1, part)
		if x < len(map[y]) - 1:
			solveByBackTrack(map, y, x + 1, prev + 1, part)
		if x > 0:
			solveByBackTrack(map, y, x - 1, prev + 1, part)
		

def solve(part):
	map = []
	global total
	total = 0
	with open("input.txt", "r") as file:
		for line in file:
			l = []
			for char in line:
				if char == ".":
					l.append(99)
				elif char != "\n":
					l.append(int(char))
			map.append(l)
	
	rows = len(map)
	columns = len(map[0])

	for y in range(rows):
		for x in range(columns):
			if map[y][x] == 0:
				newMap = copy.deepcopy(map)
				solveByBackTrack(newMap, y, x, -1, part)
		
	print(total)

if __name__ == "__main__":
	solve(1)
	solve(2)
