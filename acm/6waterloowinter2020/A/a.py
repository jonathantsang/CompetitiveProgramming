import sys

T, M, N = list(map(int, sys.stdin.readline().split()))
# . soil, S sheep, W, wolf
# * soil with carcass
# # for grass

grid = []
wolves = []
sheeps = []

def printGrid():
	for row in grid:
		r = ""
		for c in row:
			r += " " + str(c)
		print(r)

class wolf(object):
	def __init__(self, i, j):
		self.last_eat = 0
		self.i = i
		self.j = j
		self.d = False
	def move(self):
		if self.last_eat >= 10:
			self.dead()
			grid[self.i][self.j].carcass = True
			return
		global N
		grid[self.i][self.j].setWolf(None)
		if self.j+1 == N:
			self.j = 0
		else:
			self.j += 1
		grid[self.i][self.j].setWolf(self)
	def dead(self):
		self.d = True
	def __repr__(self):
		return 'W'
	def __str__(self):
		return 'W'

class sheep(object):
	def __init__(self, i, j):
		self.last_eat = 0
		self.i = i
		self.j = j
		self.d = False
	def move(self):
		if self.last_eat >= 5:
			self.dead()
			grid[self.i][self.j].carcass = True
			return
		global M
		grid[self.i][self.j].setSheep(None)
		if self.i+1 == M:
			self.i = 0
		else:
			self.i += 1
		grid[self.i][self.j].setSheep(self)
	def dead(self):
		self.i = -1
		self.j = -1
		self.d = True
	def __repr__(self):
		return 'S'
	def __str__(self):
		return 'S'

class soil(object):
	def __init__(self):
		self.grass = 0
		self.carcass = False
		self.wolf = None
		self.sheep = None
	def __repr__(self):
		if self.wolf:
			return str(self.wolf)
		elif self.sheep:
			return str(self.sheep)
		elif self.carcass:
			return '*'
		elif self.grass >= 3:
			return '#'
		else:
			return '.'
	def __str__(self):
		if self.wolf:
			return str(self.wolf)
		elif self.sheep:
			return str(self.sheep)
		elif self.carcass:
			return '*'
		elif self.grass >= 3:
			return '#'
		else:
			return '.'
	def setWolf(self, wolf):
		self.wolf = wolf

	def setSheep(self, sheep):
		self.sheep = sheep
		if self.grass >= 3 and not self.carcass:
			self.grass = 0
			if self.sheep != None:
				self.sheep.last_eat = 0

	def updateSoil(self):
		self.grass += 1
		if self.sheep != None:
			if self.sheep.last_eat >= 5:
				self.sheep.dead()
				self.sheep = None
				self.carcass = True
			else:
				self.sheep.last_eat += 1
		if self.wolf != None:
			if self.wolf.last_eat >= 10:
				self.wolf.dead()
				self.wolf = None
				self.carcass = True
			else:
				self.wolf.last_eat += 1

	def checkEat(self):
		if self.wolf != None and self.sheep != None:
			self.carcass = True
			# destroy sheep
			self.sheep.dead()
			self.wolf.last_eat = 0
			self.sheep = None
			return True
		return False

i = 0
for line in sys.stdin:
	grid.append([])
	for j, c in enumerate(line):
		if c == '\n':
			break
		grid[i].append(soil())
		if c == 'W':
			w = wolf(i ,j)
			wolves.append(w)
			grid[i][j].setWolf(w)
		elif c == 'S':
			s = sheep(i, j)
			sheeps.append(s)
			grid[i][j].setSheep(s)
	i += 1

for turn in range(0, T):
	print('before ' + str(turn))
	printGrid()
	for i in range(len(wolves)-1, -1, -1):
		wolf = wolves[i]
		if wolf.d == False:
			wolf.move()
		else:
			wolves.pop(i)
	for i in range(len(sheeps)-1, -1, -1):
		sheep = sheeps[i]
		if sheep.d == False:
			sheep.move()
		else:
			sheeps.pop(i)
	for i in range(0, len(grid)):
		for j in range(0, len(grid[0])):
			grid[i][j].checkEat()
			# Handle grass growing
			grid[i][j].updateSoil()

print("end")
printGrid()
