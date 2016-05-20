import re

Fname = raw_input("Enter File Name: ")
F = open(Fname)

for line in F:
	numbers = re.findall("[0-9]+", line)

numbers = map(int, numbers)

ints = []

for number in numbers:
	converted = int(number)
	ints.append(converted)

print sum(ints)