def getMapper():
	fin = open('input.in', 'r')
	fmap = open('mappings.in', 'r')

	lines = int(fin.readline())
	fmap.readline();

	mapper = {}

	# I know some
	mapper['q'] = 'z'
	mapper['z'] = 'q'

	for i in range(lines):
		tos = list(fin.readline())
		froms = list(fmap.readline())

		for j in range(len(froms)):
			mapper[froms[j]] = tos[j]

	return mapper

fin = open('A-small-attempt3.in', 'r')
fout = open ('output.txt', 'w')

mapper = getMapper()

print(mapper)

lines = int(fin.readline())

for i in range(lines):
	chars = list(fin.readline())
	line = 'Case #' + str(i + 1) + ': '
	
	for j in range(len(chars)):
		if chars[j] in mapper:
			line += mapper[chars[j]]
		else:
			print(chars[j])
	
	fout.write(line)
