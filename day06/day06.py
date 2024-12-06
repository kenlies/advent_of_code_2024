
def movePlayer(curr_pos, curr_dir, lst, rows, columns):
	if curr_dir[0]:
		if curr_pos[1] - 1 >= 0 and lst[curr_pos[1] - 1][curr_pos[0]] == "#":
			curr_dir = [False, True, False, False]
		else:
			curr_pos[1] -= 1 # move up
	elif curr_dir[1]:
		if curr_pos[0] + 1 < columns and lst[curr_pos[1]][curr_pos[0] + 1] == "#":
			curr_dir = [False, False, True, False]
		else:
			curr_pos[0] += 1 # move right
	elif curr_dir[2]:
		if curr_pos[1] + 1 < rows and lst[curr_pos[1] + 1][curr_pos[0]] == "#":
			curr_dir = [False, False, False, True]
		else:
			curr_pos[1] += 1 # move down
	elif curr_dir[3]:
		if curr_pos[0] - 1 >= 0 and lst[curr_pos[1]][curr_pos[0] - 1] == "#":
			curr_dir = [True, False, False, False]
		else:
			curr_pos[0] -= 1 # move left
	return curr_pos, curr_dir


def weAreInsideMapNextMove(curr_pos, rows, columns):
	if (curr_pos[1] + 1 > columns) or (curr_pos[1] - 1 < 0):
		return False
	if (curr_pos[0] + 1 > rows) or (curr_pos[0] - 1 < 0):
		return False
	return True


def solve(part):
	f = open("test.txt", "r")
	total = 0
	lst = []
	curr_pos = []
	#			up,  right,  down,  left
	curr_dir = [True, False, False, False]

	# read the file into a list of lists of characters
	for line in f:
		l = []
		for char in line:
			if char != "\n":
				l.append(char)
		lst.append(l)
	f.close()

	rows = len(lst)
	columns = len(lst[0])

	# get the starting position
	for index, row in enumerate(lst):
		if "^" in row:
			curr_pos.append(row.index("^"))
			curr_pos.append(index)
	
	# check path
	while weAreInsideMapNextMove(curr_pos, rows, columns):
		if lst[curr_pos[1]][curr_pos[0]] != "X":
			lst[curr_pos[1]][curr_pos[0]] = "X"
			total += 1
		curr_pos, curr_dir = movePlayer(curr_pos, curr_dir, lst, rows, columns)

	print(total)


if __name__ == "__main__":
	solve(1)
