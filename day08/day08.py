import copy

def solve(part):
	input = []

	total = 0
	with open("input.txt", "r") as file:
		for line in file:
			line = line.replace("\n", "")
			row = []
			for char in line:
				row.append(char)
			input.append(row)

	rows = len(input)
	columns = len(input[0])
	s = copy.deepcopy(input)

	for i in range(rows):
		for j in range(columns):
			if input[i][j] != "." and input[i][j] != "#":
				for k in range(rows):
					for l in range(columns):
						if input[i][j] == input[k][l] and i != k and j != l:
							if k > i:
								newk = i - (k - i)
							else:
								newk = i + (i - k)
							if l > j:
								newl = j - (l - j)
							else:
								newl = j + (j - l)
							if newk >= 0 and newk < rows and newl >= 0 and newl < columns and s[newk][newl] != "#":
								s[newk][newl] = "#"
								total += 1
	
	for line in s:
		print(line)
							
	print(total)

if __name__ == "__main__":
	solve(1)