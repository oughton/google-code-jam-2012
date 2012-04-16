MINSCORE = 0
MAXSCORE = 10

def canBeSurprising(totalScore):
	# edge cases
	if totalScore == MAXSCORE * 3 - 1 or totalScore == MAXSCORE * 3 or totalScore == MINSCORE or totalScore == MINSCORE + 1: 
		return False
	return True

def isGoodPick(totalScore, minResult):
	r = totalScore % 3
	n = totalScore / 3

	if not canBeSurprising(totalScore):
		return False

	if r == 0:
		if n >= minResult: return False
		return n + 1 >= minResult
	if r == 1:
		return False
	if r == 2:
		if n + 1 >= minResult: return False
		return n + 2 >= minResult

def getMaxNotSurprisingScore(totalScore):
	r = totalScore % 3
	n = totalScore / 3

	if r == 0: return n
	if r == 1: return n + 1
	if r == 2: return n + 1

def runTest(testNo, dancers, surprising, minResult, totalScores):
	maxDancers = 0
	surpisingLeft = surprising

	for i in range(len(totalScores)):
		totalScore = int(totalScores[i])

		maxScore = getMaxNotSurprisingScore(totalScore)

		if maxScore < minResult:
			if isGoodPick(totalScore, minResult) and surpisingLeft > 0:
				maxDancers += 1
				surpisingLeft -= 1
		else:
			maxDancers += 1

	fout.write('Case #' + str(testNo) + ': ' + str(maxDancers) + '\n')


fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')

tests = int(fin.readline())

for test in range(tests):
	parts = fin.readline().split(' ')

	runTest(test + 1, int(parts.pop(0)), int(parts.pop(0)), int(parts.pop(0)), parts)

