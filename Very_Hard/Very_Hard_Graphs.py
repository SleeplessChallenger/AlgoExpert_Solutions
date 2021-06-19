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

# 2 Airport Connections

# 1. create graph which incorporates all
#    airports and reachable destiantions
# 2. populate `start airport` with airports
#	 that are reachable from it. Also traverse
# 	 through all connections of those airports.
#	 After that, add all unreachable to ht 
#	 and set their `.reachable` to False
# 3. write how many reachable airports we have
#	 for every unreachable airport so as to 
#	 pick the ones with higher scores then
# 4. sort by most amount of unreachable in 
#	 `unreachableAirports` where every node
#	 is class instance with all properties.
#	 Look for `***`
def airportConnections(airports, routes, startingAirport):
    graph = createGraph(airports, routes)
	unreachableAirports = findUnreachableFromStartingAirport(
								startingAirport, graph, airports)
	defineScoreUnreachable(unreachableAirports, graph)
	return getMinRequired(unreachableAirports, graph)

def createGraph(airports, routes):
	graph = {}
	for airport in airports:
		graph[airport] = AirportGraph(airport)
	for a_port, destination in routes:
		graph[a_port].connections.append(destination)
	return graph
	
def findUnreachableFromStartingAirport(start, graph, airports):
	possibleToVisit = {}
	dfsAllFromStartingAirport(possibleToVisit, start, graph)
	unreachable = []
	for airport in airports:
		if airport in possibleToVisit:
			continue
		airNode = graph[airport]
		# receive class `AirportGraph`
		airNode.reachable = False
		# add `node` not simple `airport name`
		# because we need easy access to all
		# properties
		unreachable.append(airNode)
	return unreachable
	
def dfsAllFromStartingAirport(possibleToVisit, airport, graph):
	if airport in possibleToVisit:
		return
	nodes = graph[airport].connections
	possibleToVisit[airport] = True
	for port in nodes:
		dfsAllFromStartingAirport(possibleToVisit, port, graph)

def defineScoreUnreachable(unreachableAirports, graph):
	for node in unreachableAirports:
		airport = node.airport
		unreachable = []
		# pass 0 so as not to double count
		# `starting node`
		dfsUnreachableConnections(0, unreachable, airport, graph, {})
		node.unreachableAirports = unreachable

def dfsUnreachableConnections(i, unreachable, airport, graph, explored):
	# as there can be airport with direction
	# to it from one in unreachable, but not vice versa,
	# and we can reach this airport from `starting`:
	# 'starting' -> this airport <- child <- `airport`
	# * but we cannot go from `starting` to `airport`
	# which makes latter one unreachable
	if graph[airport].reachable:
		return
	if airport in explored:
		return
	explored[airport] = True
	if i != 0:
		unreachable.append(airport)
	connections = graph[airport].connections
	for node in connections:
		dfsUnreachableConnections(i + 1, unreachable, node, graph, explored)

def getMinRequired(unreachableAirports, graph):
	unreachableAirports.sort(key=lambda x: len(x.unreachableAirports),
							 reverse=True)
	count = 0
	for node in unreachableAirports:
		if node.reachable:
			continue
		count += 1
		# ***
		# mark all connections of unreachable
		# airport with highest score. Then we
		# won't iterate over those that can be
		# reached from current airport
		for nextNode in node.unreachableAirports:
			graph[nextNode].reachable = True
	return count
	

class AirportGraph:
	def __init__(self, airport):
		self.airport = airport
		self.connections = []
		self.reachable = True
		self.unreachableAirports = []
