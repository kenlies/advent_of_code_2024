def solve(part):
	f = open("input.txt", "r")
	first_values = []
	second_values = []
	total = 0

	for x in f:
		x = x.split()
		first_values.append(int(x[0]))
		second_values.append(int(x[1]))

	first_values.sort()
	second_values.sort()
	
	if part == 1:
		for index, value in enumerate(first_values):
			total = total + abs(first_values[index] - second_values[index])
	else:
		for value in first_values:
			total = total + value * second_values.count(value)

	print(total)
	f.close()


if __name__ == "__main__":
	solve(1)
	solve(2)