
# rule
# check if there is an empty space towards the move direction before a wall,
# if there is an empty spot just next to us, just move there, if there is a box,
# we go to the boxoes position and move the box to the empty spot

def checkAvailableSpot(warehouse, posY, posX, direction):
	if direction == "^":
		for y in range(posY, 0, -1):
			if warehouse[y][posX] == "#":
				return False
			elif warehouse[y][posX] == ".":
				warehouse[posY][posX] = "."
				warehouse[y][posX] = "O"
				return True
	elif direction == ">":
		for x in range(posX, len(warehouse[0])):
			if warehouse[posY][x] == "#":
				return False
			elif warehouse[posY][x] == ".":
				warehouse[posY][posX] = "."
				warehouse[posY][x] = "O"
				return True
	elif direction == "v":
		for y in range(posY, len(warehouse)):
			if warehouse[y][posX] == "#":
				return False
			elif warehouse[y][posX] == ".":
				warehouse[posY][posX] = "."
				warehouse[y][posX] = "O"
				return True
	elif direction == "<":
		for x in range(posX, 0, -1):
			if warehouse[posY][x] == "#":
				return False
			elif warehouse[posY][x] == ".":
				warehouse[posY][posX] = "."
				warehouse[posY][x] = "O"
				return True


def solve(part):
	total = 0
	warehouse = []
	moves = []
	posX = 0
	posY = 0
	with open("input.txt", "r") as file:
		readMap = True
		for line in file:
			if line[0] == "\n":
				readMap = False
				continue
			line = line.strip()
			row = []
			for char in line:
				if not readMap:
					moves.append(char)
					continue
				row.append(char)
			if readMap:
				warehouse.append(row)

	# find robot
	for y in range(len(warehouse)):
		for x in range(len(warehouse[0])):
			if warehouse[y][x] == "@":
				warehouse[y][x] = "."
				posY = y
				posX = x
				break
		if posX != 0:
			break

	# simulate
	for move in moves:
		if move == "^":
			if warehouse[posY - 1][posX] == ".":
				posY = posY - 1
			elif warehouse[posY - 1][posX] == "#":
				pass
			else:
				if checkAvailableSpot(warehouse, posY - 1, posX, "^"):
					posY = posY - 1
		elif move == ">":
			if warehouse[posY][posX + 1] == ".":
				posX = posX + 1
			elif warehouse[posY][posX + 1] == "#":
				pass
			else:
				if checkAvailableSpot(warehouse, posY, posX + 1, ">"):
					posX = posX + 1
		elif move == "v":
			if warehouse[posY + 1][posX] == ".":
				posY = posY + 1
			elif warehouse[posY + 1][posX] == "#":
				pass
			else:
				if checkAvailableSpot(warehouse, posY + 1, posX, "v"):
					posY = posY + 1
		elif move == "<":
			if warehouse[posY][posX - 1] == ".":
				posX = posX - 1
			elif warehouse[posY][posX - 1] == "#":
				pass
			else:
				if checkAvailableSpot(warehouse, posY, posX - 1, "<"):
					posX = posX - 1

	# sum up the gordinates
	for y in range(len(warehouse)):
		for x in range(len(warehouse[0])):
			if warehouse[y][x] == "O":
				total += 100 * y + x
	
	print(total)


if __name__ == "__main__":
	solve(1)
