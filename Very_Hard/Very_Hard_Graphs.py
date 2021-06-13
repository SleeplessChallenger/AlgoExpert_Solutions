# 1 Rectangle Mania

# T: O(n^2) S: O(n^2)
# square in Space is worst case
# when all coords are on X or Y
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def rectangleMania(coords):
	coordsTable = getCoords(coords)
	return getRectangelCount(coordsTable, coords)
	
def getCoords(coords):
	ht = {}
	for c1 in coords:
		direction = {UP: [], RIGHT: [],
					 LEFT: [], DOWN: []}
		for c2 in coords:
			anotherDir = getDirection(c1, c2)
			if anotherDir in direction:
				direction[anotherDir].append(c2)
		strCoord = getStr(c1)
		ht[strCoord] = direction
		
	return ht
					
def getDirection(c1, c2):
	x1, y1 = c1
	x2, y2 = c2
	if x1 == x2:
		if y1 > y2:
			return DOWN
		elif y1 < y2:
			return UP
	elif y1 == y2:
		if x1 > x2:
			return LEFT
		elif x1 < x2:
			return RIGHT
	return ""

def getRectangelCount(ht, coords):
	count = 0
	for c in coords:
		count += clockwiseCount(c, ht, UP, c)
	return count

def clockwiseCount(coord, ht, direction, origin):
	strVersion = getStr(coord)
	if direction == LEFT:
		res = origin in ht[strVersion][LEFT]
		return 1 if res else 0
	else:
		count = 0
		nextDir = nextDirection(direction)
		for c in ht[strVersion][direction]:
			count += clockwiseCount(c, ht, nextDir,origin)
		return count
		
def nextDirection(direc):
	if direc == UP:
		return RIGHT
	if direc == RIGHT:
		return DOWN
	if direc == DOWN:
		return LEFT
	return ""

def getStr(coord):
	x, y = coord
	return str(x) + ':' + str(y)

UP = 'up'
DOWN = 'down'
RIGHT = 'right'

# T: O(n^2) S: O(n)
def rectangleMania(coords):
	coordsTable = getCoords(coords)
	return getRectangelCount(coordsTable, coords)

def getCoords(coords):
	ht = {}
	for c in coords:
		coordStr = getStr(c)
		ht[coordStr] = True
	return ht

def getRectangelCount(ht, coords):
	count = 0
	for x1, y1 in coords:
		for x2, y2 in coords:
			if not upperRight([x1,y1], [x2,y2]):
				continue
			# find corresponding `top left` and
			# `bottom right`
			uppLeft = getStr([x1, y2])
			downRight = getStr([x2, y1])
			if uppLeft in ht and downRight in ht:
				count += 1
	return count

def upperRight(c1, c2):
	x1, y1 = c1
	x2, y2 = c2
	return x1 < x2 and y2 > y1

def getStr(coord):
	x, y = coord
	return str(x) + ':' + str(y)	
