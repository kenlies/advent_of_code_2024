
def solve(part):
	stones = []
	blinks = 25
	with open("input.txt", "r") as file:
		for line in file:
			line = line.strip() # remove new line
			stones = line.split(" ")

	for i in range(blinks):
		newStones = []
		for j in range(len(stones)):
			# rules 
			if stones[j] == '0':
				newStones.append('1')
			elif len(stones[j]) % 2 == 0:
				firstpart, secondpart = stones[j][:len(stones[j])//2], stones[j][len(stones[j])//2:]
				newStones.append(str(int(firstpart)))
				newStones.append(str(int(secondpart)))
			else:
				newStones.append(str(int(stones[j]) * 2024))
		stones = newStones
	
	print(len(stones))

if __name__ == "__main__":
	solve(1)