from collections import deque
import copy

class Point:
	def __init__(self,x: int, y: int):
		self.x = x
		self.y = y


class queueNode:
	def __init__(self,pt: Point, dist: int):
		self.pt = pt
		self.dist = dist


def isValid(row: int, col: int, rowSize, colSize):
    return (row >= 0) and (row < rowSize) and (col >= 0) and (col < colSize)


def BFS(input, visited, src: Point, dest: Point):
	rowNum = [-1, 0, 0, 1]
	colNum = [0, -1, 1, 0]
	rowSize = len(input)
	columnSize = len(input[0])
	visited[src.x][src.y] = True # set the starting cell as visited

	q = deque() # create a queue for BFS

	s = queueNode(src, 0) # create the first node, distance is 0 drom starting cell (we are in it)

	q.append(s) # enqueue the source cell

	while q: # do the BFS starting from source cell
		curr = q.popleft() # dequeue the front cell
		pt = curr.pt
		if pt.x == dest.x and pt.y == dest.y:
			return curr.dist
		for i in range(4):
			row = pt.x + rowNum[i]
			col = pt.y + colNum[i]

			if isValid(row, col, rowSize, columnSize) and input[row][col] != "#" and visited[row][col] == False:
				visited[row][col] = True
				Adjcell = queueNode(Point(row, col), curr.dist+1)
				q.append(Adjcell)


def resetVisited(visited):
	for i in range(len(visited)):
		for j in range(len(visited[0])):
			if visited[i][j] == True:
				visited[i][j] = False


def validForCheat(race_map, i, j):
	if race_map[i][j] == "#" and i - 1 >= 0 and j - 1 >= 0 and \
		i + 1 < len(race_map) and j + 1 < len(race_map[0]):
		l = 0
		for x in range(4):
			if race_map[i + 1][j] == ".":
				l += 1
			if race_map[i - 1][j] == ".":
				l += 1
			if race_map[i][j + 1] == ".":
				l += 1
			if race_map[i][j - 1] == ".":
				l += 1
		if l >= 2:
			return True
	return False


def makeCheat(race_map, i, j):
	new_race_map = copy.deepcopy(race_map)
	new_race_map[i][j] = "."
	return new_race_map


def solve(part):

	total = 0
	base_picoseconds = 0
	race_map = []
	visited = []

	# read map
	with open("input.txt", "r") as file:
		for i, line in enumerate(file):
			line = line.strip()
			row = []
			for j in line:
				row.append(j)
			race_map.append(row)

	# get start and end and create visited
	for i in range(len(race_map)):
		vis_row = []
		for j in range(len(race_map[0])):
			vis_row.append(False)
			if race_map[i][j] == "S":
				source = Point(i, j)
			elif race_map[i][j] == "E":
				dest = Point(i, j)
		visited.append(vis_row)

	base_picoseconds = BFS(race_map, visited, source, dest)
	resetVisited(visited)

	for i in range(len(race_map)):
		for j in range(len(race_map[0])):
			if validForCheat(race_map, i, j):
				if base_picoseconds - BFS(makeCheat(race_map, i, j), visited, source, dest) >= 100:
					total += 1
				resetVisited(visited)

	print(total)


if __name__ == "__main__":
	solve(1)
