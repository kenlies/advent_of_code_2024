import itertools

def solve(part):
	test_vals = []
	eq_vals = []
	total = 0

	# read values to lists
	with open('input.txt', 'r') as file:
		for line in file:
			line = line.replace("\n", "")
			s1 = line.split(":")
			test_vals.append(int(s1[0]))
			s2 = s1[1].split(" ")
			s2 = s2[1:] # leave the first one out (it was a blank for some reason)
			for i in range(len(s2)):
				s2[i] = int(s2[i])
			eq_vals.append(s2)
	
	# solve the problem
	operators = ["*", "+"]
	if part == 2:
		operators.append("||")

	for i in range(len(test_vals)):
		for comp in itertools.product(operators, repeat=len(eq_vals[i]) - 1):
			check = eq_vals[i][0]
			for j in range(1, len(eq_vals[i])):
				if comp[j - 1] == "*":
					check *= eq_vals[i][j]
				elif part == 2 and comp[j - 1] == "||":
					check = int(str(check) + str(eq_vals[i][j]))
				else:
					check += eq_vals[i][j]
			if check == test_vals[i]:
				total += test_vals[i]
				break

	print(total)

if __name__ == "__main__":
	solve(1)
	solve(2)
