import copy

currRegionArea = 0
currRegionPerimiter = 0

def findPerimiter(input, i, j):
	global currRegionPerimiter
	copyInput = copy.deepcopy(input)
	rows = len(input)
	columns = len(input[0])

	for k in range(rows):
		for l in range(columns):
			if input[k][l] == ".":
				input[k][l] = ","  # mark this spot as checked
				if k - 1 < 0 or copyInput[k - 1][l] != ".":
					currRegionPerimiter += 1
				# check right
				if l + 1 >= columns or copyInput[k][l + 1] != ".":
					currRegionPerimiter += 1
				# check down
				if k + 1 >= rows or copyInput[k + 1][l] != ".":
					currRegionPerimiter += 1
				# check right
				if l - 1 < 0 or copyInput[k][l - 1] != ".":
					currRegionPerimiter += 1
	

def dfs(input, i, j, oldChar, newChar):
	global currRegionArea
	global currRegionPerimiter

	if input[i][j] != oldChar:
		return

	input[i][j] = newChar
	currRegionArea += 1

	rows = len(input)
	columns = len(input[0])

	# check up
	if i - 1 >= 0:
		dfs(input, i - 1, j, oldChar, newChar)
	# check right
	if j + 1 < columns:
		dfs(input, i, j + 1, oldChar, newChar)
	# check down
	if i + 1 < rows:
		dfs(input, i + 1, j, oldChar, newChar)
	# check left
	if j - 1 >= 0:
		dfs(input, i, j - 1, oldChar, newChar)


def floodFill(input, i, j, newChar):
	oldChar = input[i][j]
	if oldChar == newChar:
		return
	dfs(input, i, j, oldChar, newChar)


def solve(part):
	global currRegionArea
	global currRegionPerimiter
	total = 0
	input = []

	with open("input.txt", "r") as file:
		for line in file:
			line = line.strip()
			row = []
			for char in line:
				row.append(char)
			input.append(row)

	rows = len(input)
	columns = len(input[0])

	for i in range(rows):
		for j in range(columns):
			if input[i][j] != ",":
				floodFill(input, i, j, ".")
				findPerimiter(input, i, j)
				total += currRegionArea * currRegionPerimiter
				currRegionArea = 0
				currRegionPerimiter = 0

	print(total)


if __name__ == "__main__":
	solve(1)