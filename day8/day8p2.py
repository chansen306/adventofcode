import sys

totalAccum = 0

for line in sys.stdin:
	for x in line:
		if x == '\\':
			totalAccum += 1
		if x == '"':
			totalAccum += 1	
			
	totalAccum += 2

print(totalAccum)