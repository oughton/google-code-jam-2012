def getUniquePairsCount(n, a, b, cache):
	pairs = 0
	digits = str(n)

	for end in range(len(digits) - 1):
			testDigits = digits[end + 1:] + digits[:end + 1]

			if int(testDigits) < a or int(testDigits) > b:
				continue

			key1 = digits + ',' + testDigits
			key2 = testDigits + ',' + digits

			if key1 in cache or key2 in cache:
				continue

			if testDigits != digits:
				pairs += 1
				cache[key1] = True

	return pairs

def runTest(testNo, a, b):
	count = 0
	seen = {}

	for n in range(a, b + 1):
		count += getUniquePairsCount(n, a, b, seen)
	
	fout.write('Case #' + str(testNo) + ': ' + str(count) + '\n')

fin = open('C-large-practice.in', 'r')
fout = open('output.txt', 'w')

tests = int(fin.readline())

for test in range(tests):
	parts = fin.readline().split(' ')

	runTest(test + 1, int(parts[0]), int(parts[1]))
