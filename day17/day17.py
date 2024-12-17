

def findComboOperand(operand, regA, regB, regC):
	if operand >= 0 and operand <= 3:
		return operand
	elif operand == 4:
		return regA
	elif operand == 5:
		return regB
	elif operand == 6:
		return regC


def solve(part):
	regA = 0
	regB = 0
	regC = 0
	program = []
	out = ""

	with open("input.txt", "r") as file:
		for i, line in enumerate(file):
			if i == 0:
				regA = int(line.split(" ")[2])
			elif i == 1:
				regB = int(line.split(" ")[2])
			elif i == 2:
				regC = int(line.split(" ")[2])
			elif i == 4:
				p = line.split(" ")[1]
				for i in p:
					if i != "," and i != "\n":
						program.append(int(i))

	i = 0
	while i + 1 < len(program):
		opcode = program[i]
		operand = program[i + 1]
		
		if opcode == 0: # adv
			regA = regA // 2 ** findComboOperand(operand, regA, regB, regC)
		elif opcode == 1: # bxl
			regB = regB ^ operand
		elif opcode == 2: # bst
			val = findComboOperand(operand, regA, regB, regC) % 8
			regB = val
		elif opcode == 3: # jnz
			if regA == 0:
				pass
			else:
				i = operand
				continue
		elif opcode == 4: # bxc
			regB = regB ^ regC
		elif opcode == 5: # out
			out += str(findComboOperand(operand, regA, regB, regC) % 8) + ","
		elif opcode == 6: # bdv
			regB = regA // 2 ** findComboOperand(operand, regA, regB, regC)
		elif opcode == 7: # cdv
			regC = regA // 2 ** findComboOperand(operand, regA, regB, regC)

		i += 2

	print(out[:-1])


if __name__ == "__main__":
	solve(1)
