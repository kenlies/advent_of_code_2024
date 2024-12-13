import re

def solve(part):
	total = 0
	buttonA = []
	buttonB = []
	price = []
	ruleIndex = 0

	with open("input.txt", "r") as file:
		for line in file:
			if line[0] == "\n":
				buttonA = []
				buttonB = []
				price = []
				ruleIndex = 0
				continue
			numbers = re.findall('\\d+', line)
			for i in range(len(numbers)):
				numbers[i] = int(numbers[i])
			if ruleIndex == 0:
				buttonA = numbers
			elif ruleIndex == 1:
				buttonB = numbers
			else:
				price = numbers
			ruleIndex += 1

			if ruleIndex == 3:
				totalTokensUsed = 0
				totalBigPresses = 0
				totalSmlPresses = 0
				possible = True
				if buttonA[0] > buttonB[0]:
					bigger = buttonA
					smaller = buttonB
					BigTokInc = 3
					SmlTokInc = 1
				else:
					bigger = buttonB
					smaller = buttonA
					BigTokInc = 1
					SmlTokInc = 3
				counter = [0, 0]
				while price[0] > counter[0] or price[1] > counter[1]:
					counter[0] += bigger[0]
					counter[1] += bigger[1]
					totalTokensUsed += BigTokInc
					totalBigPresses += 1
				while price[0] != counter[0] or price[1] != counter[1] or totalBigPresses > 100:
					counter[0] -= bigger[0]
					counter[1] -= bigger[1]
					totalTokensUsed -= BigTokInc
					totalBigPresses -= 1
					while price[0] > counter[0] or price[1] > counter[1]:
						counter[0] += smaller[0]
						counter[1] += smaller[1]
						totalTokensUsed += SmlTokInc
						totalSmlPresses += 1
						if totalSmlPresses > 100:
							possible = False
							break
					if not possible:
						break
				if possible:
					total += totalTokensUsed
		print(total)


if __name__ == "__main__":
	solve(1)