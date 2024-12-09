
def solve(part):
	unformatted = []
	total = 0
	with open("input.txt", "r") as file:
		content = file.readlines()[0]
	curr_id = 0

	for i in range(len(content)):
		if content[i] == "\n":
			break
		if i % 2 == 0:
			for x in range(int(content[i])):
				unformatted.append(curr_id)
			curr_id += 1
		else:
			for x in range(int(content[i])):
				unformatted.append(".")

	for i in range(len(unformatted)):
		if unformatted[i] == ".":
			done = False
			for j in range(len(unformatted) - 1, -1, -1):
				if j <= i:
					done = True
					break
				if unformatted[j] != ".":
					unformatted[i] = unformatted[j]
					unformatted[j] = "."
					break
			if done:
				break

	for i in range(len(unformatted)):
		if unformatted[i] == ".":
			break
		total += i * unformatted[i]

	print(total)

if __name__ == "__main__":
	solve(1)
