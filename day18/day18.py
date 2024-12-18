from collections import deque


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


def solve(part):

	steps = 0
	mem_space = []
	visited = []
	source = Point(0, 0)
	dest = Point(70, 70)

	# create mem space and visited list
	for x in range(70 + 1):
		mem_line = []
		vis_line = []
		for y in range(70 + 1):
			mem_line.append(".")
			vis_line.append(False)
		mem_space.append(mem_line)
		visited.append(vis_line)

	# fill the mem space with fallen bytes
	with open("input.txt", "r") as file:
		for i, line in enumerate(file):
			line = line.strip()
			if i == 1024 and part == 1:
				steps = BFS(mem_space, visited, source, dest)
				print(steps)
				break;
			elif part == 2:
				s = line.split(",")
				mem_space[int(s[1])][int(s[0])] = "#"
				steps = BFS(mem_space, visited, source, dest)
				if steps == None:
					print(line)
					break;
				for i in range(len(visited)):
					for j in range(len(visited[0])):
						visited[i][j] = False
			if part == 1:
				s = line.split(",")
				mem_space[int(s[1])][int(s[0])] = "#"

if __name__ == "__main__":
	solve(1)
	solve(2)
