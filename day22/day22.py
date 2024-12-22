
def solve(part):
	buyers = []
	total = 0

	with open("input.txt", "r") as file:
		for line in file:
			line = line.strip()
			buyers.append(int(line))

	for initSecretNum in buyers:
		for i in range(2000):
			for i in range(3):
				secretNum = initSecretNum
				if i == 0:
					secretNum = secretNum << 6
				elif i == 1:
					secretNum = secretNum >> 5
				elif i == 2:
					secretNum = secretNum << 11
				secretNum = secretNum ^ initSecretNum # mix
				initSecretNum = secretNum % 16777216 # prune
		total += initSecretNum

	print(total)


if __name__ == "__main__":
	solve(1)
