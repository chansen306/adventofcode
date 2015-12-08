import sys

accum = 0

for line in sys.stdin:
	line = line.rstrip('\n')
	evaluatedLine = eval(line)
	accum += len(line) - len(evaluatedLine)
	print( str(len(line) - 1) + ":" + str(len(evaluatedLine)) )

print(accum)