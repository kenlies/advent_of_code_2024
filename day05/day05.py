
def solve(part):
	f = open("test.txt", "r")
	rules = []
	updates = []
	wrongs = []
	total = 0
	read_rules = True

	# reading rules and updates to lists
	for line in f:
		if line[0] == '\n':
			read_rules = False
			continue
		if read_rules:
			rules.append(line.replace("\n", "").split("|"))
		else:
			updates.append(line.replace("\n", "").split(","))

	# for each update, loop through the rules and check if the number is correctly placed
	# it is not found, then move to the next rule
	if part == 1:
		for update_set in updates:
			valid = True
			for rule_set in rules:
				if rule_set[0] not in update_set or rule_set[1] not in update_set:
					continue
				left_index = update_set.index(rule_set[0])
				right_index = update_set.index(rule_set[1])
				if left_index > right_index:
					valid = False
			if valid:
				total += int(update_set[(len(update_set)) // 2])

	print(total)
	f.close()

if __name__ == "__main__":
	solve(1)