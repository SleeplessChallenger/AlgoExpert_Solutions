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

# 3 Detect Arbitrage

# Explanation

# currency = vertice
# rate = edge

# use Bellman-Ford algorithm
# to detect negative weight cycles
# (and it can handle negative weight edges).
# Initially: if we start from 1.0 USD and
# if we come back to USD with greater number
# -> What we need! (actually, what we try to
# find if edges multiply by 1)

# negative weight cycle = positive mult. cycle (descr. above)

# 1. modify graph so that every edge
# is a `-log(edge)`
# log(a * b) > log(1) => log(a * b) > 0
# But we need negative weight cycle, not `> 0`
# Hence we mult. eveything by `-1`:
# - ( log(a) + log(b) ) < 0
# Note: to use B-F alg. we need to have all nodes
# connected, thus if we add new node, it must be
# connected to all existing nodes
# 2. Traverse the graph `realixing` (looking at) every edge
#  to find the shortest path. Amount of nodes to relax is `n - 1`.
# After we've relaxed all nodes (n - 1) times, we need to repeat
# the process one more time, and if some distance becomes
# shorter => "neagtive weight cycle is found"
# 3. Start from CAD, relax all other nodes.
#		  CAD  USD  GBP
#  start: [0,  inf, inf] -> [0, -2, inf] -> [0, -2, -6]
#   Then switch to USD and do the same.

#  start: [0, -2, -6] -> !!!from USD to CAD we take -2 and
#	add 1 (imagine we have USD -> CAD == 1) [-1, -2, -6]
#	-> take -2 and add 4 (USD -> GBP == 4), but it's not
# smaller than -6, skip it [-1, -2, -6]

#  	And last is GBP -> same process.
# start: [-1, -2, -6] -> (GBP -> CAD == 3) -6 + 3 = -3, 
# it's smaller than -1, hence update [-3, -2, -6] ->
# (GBP -> USD == 3) -6 + 3 = -3, hence update [-3, -3, -6]

# first value is current node from which we `act`
# and second value is edge. Result is compared to curr.
# result TO THE VERTIX. Ex: first val: USD: -2, second val:
# USD -> CAD: 1. Result: -2 + 1 = -1 compared to [CAD: 0]

# 4. All the time throughout 3rd point we have the same
# data structure which we modify to find the shortest path.

# 5. do the process again one more time.
#			   CAD USD GBP
# CAD vertex: [-3, -3, -6] -> CAD - USD: -3 - 2 = -5 [-3, -5, -6]
#							  CAD - GBP: -3 - 6 = -9 [-3, -5, -9]
# USD vertex: [-3, -5, -9] -> USD - CAD: -5 + 1 = -4 [-4, -5, -9]
#							  USD - GBP: -5 + 4 not > than -9
# GBP vertex: [-4, -5, -9] -> GBP - CAD: -9 + 3 = -6 [-6, -5, -9]
#							  GBP - USD: -9 + 3 = -6 [-6, -6, -9]
# 6. If there is `negative weight cycle`, every iteration
#	will bring more and more negative values

# with 2D array
import math

def detectArbitrage(exchangeRates):
    graph = createGraph(exchangeRates)
	return findNegCycle(graph, 0)

def findNegCycle(graph, start):
	# or we can:
	# 1. remove -1
	# 2. return True in the end
	# instead of additional func()
	distances = [float('inf') for _ in range(len(graph))]
	# instead of float we can place `0`
	distances[start] = 0
	
	n = len(graph) - 1
	# as we need to make `n - 1` calls
	for _ in range(n):
		if not relaxEdges(graph, distances):
		# if some updates are done to
		# distances -> True else False
			return False

	return relaxEdges(graph, distances)
	# relax once more time. If found smaller
	# -> True. Else False

def relaxEdges(graph, dist):
	smallerDone = False
	
	for idx in range(len(graph)):
		edges = graph[idx]
		for idx2 in range(len(edges)):
			edge = edges[idx2]
			newDist = dist[idx] + edge
			# `dist[idx]` means take
			# one vertex per outer loop
			# and add others. Then change
			# vertex.
			# I.e. take one from which we go,
			# add others to which we go.
			if newDist < dist[idx2]:
				# compare "TO which we go"
				dist[idx2] = newDist
				smallerDone = True
	
	return smallerDone
	
def createGraph(rates):
	graph = []
	
	for i in range(len(rates)):
		graph.append([])
		for j in range(len(rates[i])):
			rate = rates[i][j]
			graph[i].append(-math.log10(rate))

	return graph

# with hashtable
import math

def detectArbitrage(exchangeRates):
    graph = createGraph(exchangeRates)
	return findNegCycle(graph, 0)

def findNegCycle(graph, start):
	distances = [float('inf') for _ in graph.keys()]
	distances[start] = 0
	
	n = len(graph.keys() ) - 1
	# as we need to make `n - 1` calls
	for _ in range(n):
		if not relaxEdges(graph, distances):
		# if some updates are done to
		# distances -> True else False
			return False
	
	return relaxEdges(graph, distances)
	# relax once more time. If found smaller
	# -> True. Else False

def relaxEdges(graph, dist):
	smallerDone = False
	edges = graph.keys()
	for idx in edges:
		values = graph[idx]
		for idx2 in range(len(values)):
			val = values[idx2]
			newDist = dist[idx] + val
			if newDist < dist[idx2]:
				dist[idx2] = newDist
				smallerDone = True
	
	return smallerDone
	
def createGraph(rates):
	graph = {}
	
	for i in range(len(rates)):
		for j in range(len(rates[i])):
			rate = rates[i][j]
			if i not in graph:
				graph[i] = []
			graph[i].append(-math.log10(rate))

	return graph

# 4 Two-Edge-Connected Graph

# Explanation

# Graph: unweighted and undirected. No parallel edges
# edges = [[1, 2, 5], [0, 2], [0, 1, 3],
#		   [2, 4, 5], [3, 5], [0, 3, 4]]

# vertices = 6; {0: [1, 2, 5], 1: [0, 2], 2: [0, 1, 3],
# 			     3: [2, 4, 5], 4: [3, 5], 5: [0, 3, 4]}

# two-edge: every vertex has reverse connection from 
# each of the outbound verticies. + it does mean if
# you remove one edge, then graph doesn't become
# disconnected, i.e. you can still visit ALL
# the vertices from either of the vertex (
# no so-called `Bridge`)

# edge: tree & back. Tree - edge that connects new
# vertices in dfs. Back - edge that comes from already
# visited node to node that has been visited before it (ancestor).
# => check that every tree edge has back edge by looking
# at tree edge DESCENDANTS which must connect to node FROM WHICH
# tree edge came from. Ex: 0 -> 1. 1 is Tree edge, hence either
# of the descendants of 1 should connect to 0. Because if we
# remove conn. from 0 to 1 we still will be able to reach 1
# from 0 by: 1) going through descendants of 1, landing at 0
# 2) then reaching through other nodes at 1

# Steps:
#	
# 1. don't consider node you come from
# 2. have 2 nums: order visited and arrival time
# 3. when at edge check for other visited nodes and
# if node is such -> check for it's order visited
# (not arrival time) and if it's `< curr. edge arrival time`
# -> replace curr. edge arrival time. It does mean we can access
# from curr. node ANCESTOR with smaller arrival time
# 4. after we've visited all nodes, we'll go back in 
# recursive call stack and update all previous arrival times
# if they're bigger than the one coming from recursive call.
# In result, if return value from dfs() of start node
# == arrival time of start node => no bridge.
# If min. arrival time of accessible ancestor isn't
# smaller than curr. edge => bridge. `return -1`

# Overall there're 2 steps:
# 1. graph is connected
# 2. no bridge

def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
		return True
	
	# arrival time of all vertices
	arrivalTimes = [-1 for _ in range(len(edges))]
	
	# _, _, currVertex, currArrivalTime, parent
	if checkAllArrivalTimes(arrivalTimes, edges, 0, 1, -1) == -1:
		return False
	
	return checkArrival(arrivalTimes)

def checkArrival(times):
	for t in times:
		if t == -1:
			return False
	
	return True

def checkAllArrivalTimes(times, edges, currVertex, currTime, parent):
	# currTime of the first node can be 0.
	# It is at what pos. we visited this node
	minTime = currTime
	times[currVertex] = currTime
	
	for edge in edges[currVertex]:
		if times[edge] == -1:
			# this OUTBOUND vertex hasn't
			# already been visited
			minTime = min(minTime, checkAllArrivalTimes(
				times, edges, edge, currTime + 1, currVertex))
		elif edge != parent:
			# vertex has already been visited
			# AND it's not the one we came from.
			# Remember: we disregard parent node
			# and look at other edges (don't
			# consider tree edge)
			minTime = min(minTime, times[edge])
	
	# 1. we're not on the start node
	# 2. if minArrivalTime is still the same
	# as it was in the beginning =>
	# we have found a bridge
	if parent != -1 and currTime == minTime:
		return -1
	
	return minTime
