import sys, re

numbers = re.compile("[0-9]+")
signals = {}

extraLines = []

for line in sys.stdin:
	extraLines.append(line)

while len(extraLines) > 0:
	line = extraLines.pop(0)
	line = line.rstrip('\n')
	tokens = line.split(' ')
	last = tokens[len(tokens)-1]

	if "AND" in line:
		first = tokens[0]
		second = tokens[2]

		if numbers.search(first) and numbers.search(second):
			signals[last] = int(first) & int(second)
		elif numbers.search(first) and second in signals:
			signals[last] = int(first) & int(signals[second])
		elif first in signals and numbers.search(second):
			signals[last] = int(first) & int(signals[second])
		elif first in signals and second in signals:
			signals[last] = int(signals[first]) & int(signals[second])
		else:
			extraLines.append(line)
		continue
	if "OR" in line:
		first = tokens[0]
		second = tokens[2]

		if numbers.search(first) and numbers.search(second):
			signals[last] = int(first) | int(second)
		elif numbers.search(first) and second in signals:
			signals[last] = int(first) | int(signals[second])
		elif first in signals and numbers.search(second):
			signals[last] = int(first) | int(signals[second])
		elif first in signals and second in signals:
			signals[last] = int(signals[first]) | int(signals[second])
		else:
			extraLines.append(line)
		continue
	if "LSHIFT" in line:
		first = tokens[0]
		second = int(tokens[2])

		if numbers.search(first):
			signals[last] = int(first) << second
		if first in signals:
			signals[last] = int(signals[first]) << second
		else:
			extraLines.append(line)
		continue
	if "RSHIFT" in line:
		first = tokens[0]
		second = int(tokens[2])

		if numbers.search(first):
			signals[last] = int(first) >> second
		if first in signals:
			signals[last] = int(signals[first]) >> second
		else:
			extraLines.append(line)
		continue
	if "NOT" in line:
		first = tokens[1]
		if numbers.search(first):
			signals[last] = ~ int(first)
		elif first in signals:
			signals[last] = ~ int(signals[first])
		else:
			extraLines.append(line)
		continue
		
	first = tokens[0]

	if numbers.search(first):
		signals[last] = int(first)
	elif first in signals:
		signals[last] = signals[first]
	else:
		extraLines.append(line)

print(signals["a"])