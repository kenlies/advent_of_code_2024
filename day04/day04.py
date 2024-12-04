import re

straight = "XMAS"
backwards = "SAMX"

def secondDiagonalOrder(arr, n, m):
	ans = [[] for i in range(n + m - 1)]

	for i in range(m):
		for j in range(n):
			ans[i + j].append(arr[j][m - i - 1])
	return ans

def firstDiagonalOrder(arr, n, m): 
	ans = [[] for i in range(n + m - 1)] 
	
	for i in range(m): 
		for j in range(n): 
			ans[i + j].append(arr[j][i]) 
	return ans

def createNewList(lst):
	newlist = []
	for line in lst:
		s = ""
		for char in line:
			s += char
		newlist.append(s)
	return newlist

def findMatches(lst):
	total = 0
	for line in lst:
		x = re.findall(straight, line)
		y = re.findall(backwards, line)
		total += len(y) + len(x)
	return total

def solve(part):
	f = open("input.txt", "r")
	total = 0
	lst = []

	# read the file into a list
	for line in f:
		lst.append(line)
	f.close()

	col_size = len(lst)
	row_size = len(lst[0]) - 1 # remove newline

	# find all horizontals
	total += findMatches(lst)

	# find all verticals
	convert = list(map(list, zip(*lst))) # make lists of colums
	newlist = createNewList(convert)
	total += findMatches(newlist)

	# find all first diagonals
	newlist = createNewList(firstDiagonalOrder(lst, col_size, row_size))
	total += findMatches(newlist)

	# find all second diagonals
	newlist = createNewList(secondDiagonalOrder(lst, col_size, row_size))	
	total += findMatches(newlist)

	print(total)


if __name__ == "__main__":
	solve(1)