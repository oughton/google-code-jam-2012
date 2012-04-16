def allSameDigits(n):
	digits = str(n)
	marker = digits[0]

	for digit in digits:
		if digit != marker:
			return False
	return True

def runTest(testNo, a, b):
	count = 0
	seen = {}

	for n in range(a, b):
		digits = str(n)

		if allSameDigits(n):
			continue

		for end in range(len(digits)):
			testDigits = digits[end + 1:] + digits[:end + 1]

			# check if its already been used
			if testDigits in seen:
				continue

			if int(testDigits) >= a and int(testDigits) <= b:
				print(testDigits)
				count += 1

			seen[digits] = True

	print('\nresult:' +  str(count))

fin = open('C-large-practice.in', 'r')
fout = open('output.txt', 'w')

tests = int(fin.readline())

for test in range(tests):
	parts = fin.readline().split(' ')

	runTest(test + 1, int(parts[0]), int(parts[1]))

