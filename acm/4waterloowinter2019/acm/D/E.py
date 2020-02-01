import sys

def checkone(r1, r2, r3):
	if r2[1] != 'o':
		return "unknown"
	return 1

def checktwo(r1, r2, r3):
	if (r1[0] == 'o' and r3[2] == 'o') or (r1[2] == 'o' and r3[0] == 'o'):
		return 2
	return 'unknown'

def checkthree(r1, r2, r3):
	if (r1[0] == 'o' and r3[2] == 'o' and r2[1] == 'o') or \
	   (r1[2] == 'o' and r3[0] == 'o'and r2[1] == 'o'):
		return 3
	return 'unknown'

def checkfour(r1, r2, r3):
	if r1[0] == 'o' and r1[2] == 'o' and r3[0] == 'o' and r3[2] == 'o':
		return 4
	return 'unknown'

def checkfive(r1, r2, r3):
	if r1[0] == 'o' and r1[2] == 'o' and \
	r3[0] == 'o' and r3[2] == 'o' and r2[1] == 'o':
		return 5
	return 'unknown'

def checksix(r1, r2, r3):
	if r1[0] == 'o' and r1[1] == 'o' and r1[2] == 'o'\
		and r3[0] == 'o' and r3[1] == 'o' and r3[2] == 'o':
		return 6
	elif r1[0] == 'o' and r2[0] == 'o' and r3[0] == 'o'\
		and r1[2] == 'o' and r2[2] == 'o' and r3[2] == 'o':
		return 6
	return "unknown"

def checkdie(dents, r1, r2, r3):
	valid = "unknown"
	if dents == 1:
		valid = checkone(r1, r2, r3)
	elif dents == 2:
		valid = checktwo(r1, r2, r3)
	elif dents == 3:
		valid = checkthree(r1, r2, r3)
	elif dents == 4:
		valid = checkfour(r1, r2, r3)
	elif dents == 5:
		valid = checkfive(r1, r2, r3)
	elif dents == 6:
		valid = checksix(r1, r2, r3)
	print(valid)

n = 3

r1 = sys.stdin.readline()[:-1]
r2 = sys.stdin.readline()[:-1]
r3 = sys.stdin.readline()[:-1]

dents = 0
for v in r1:
	if v == 'o':
		dents += 1
for v in r2:
	if v == 'o':
		dents += 1
for v in r3:
	if v == 'o':
		dents += 1

if dents < 0 or dents > 6:
	print("unknown")
else:
	checkdie(dents, r1, r2, r3)
