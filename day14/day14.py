
def solve(part):
	quadrants = [0, 0, 0, 0]
	seconds = 100
	robots = []
	dimX = 101
	dimY = 103

	with open("input.txt", "r") as file:
		for line in file:
			line = line.strip()
			vals = []
			splitted = line.split("=")
			vals.append(int(splitted[1].split(" ")[0].split(",")[0]))
			vals.append(int(splitted[1].split(" ")[0].split(",")[1]))
			vals.append(int(splitted[2].split(",")[0]))
			vals.append(int(splitted[2].split(",")[1]))
			robots.append(vals)

	for robot in robots:
		posX = robot[0]
		posY = robot[1]
		for s in range(seconds):
			posX += robot[2]
			posY += robot[3]
			if posX >= dimX:
				posX = abs(posX - dimX)
			if posX < 0:
				posX = dimX + posX
			if posY >= dimY:
				posY = abs(posY - dimY)
			if posY < 0:
				posY = dimY + posY

		if posX < dimX // 2:
			if posY < dimY // 2:
				quadrants[0] += 1
			elif posY > dimY // 2:
				quadrants[2] += 1
		elif posX > dimX // 2:
			if posY < dimY // 2:
				quadrants[1] += 1
			elif posY > dimY // 2:
				quadrants[3] += 1

	print("ans: ", quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


if __name__ == "__main__":
	solve(1)
