# 1 Topological Sort
# mine (1st way of solving)
def topologicalSort(jobs, deps):
    graph = getGraph(jobs, deps)
	return orderedGraph(graph)

def getGraph(jobs, deps):
	graph = GraphClass(jobs)
	for prereq, job in deps:
		graph.addPrereq(prereq, job)
	return graph

def orderedGraph(graph):
	result = []
	for vertex in graph.vertices:
		isCycle = dfs(vertex, result)
		if isCycle:
			return []
	return result

def dfs(vertex, result):
	if vertex.visited:
		return False
	if vertex.visiting:
		return True
	vertex.visiting = True
	for node in vertex.prereqs:
		isCycle = dfs(node, result)
		if isCycle:
			return []
	
	result.append(vertex.job)
	vertex.visitng = False
	vertex.visited = True
	return False
	
	
class GraphClass:
	def __init__(self, jobs):
		self.vertices = []
		self.graph = {}
		for job in jobs:
			self.insert(job)
	
	def insert(self, job):
		self.graph[job] = JobClass(job)
		self.vertices.append(self.graph[job])
	
	def getNode(self, node):
		return self.graph[node]
	
	def addPrereq(self, prereq, job):
		jobNode = self.getNode(job)
		prereqNode = self.getNode(prereq)
		jobNode.prereqs.append(prereqNode)

		
class JobClass:
	def __init__(self, job):
		self.job = job
		self.prereqs = []
		self.visited = False
		self.visiting = False

# not mine (1st way of solving)
def topologicalSort(jobs, deps):
	job_graph = createJobGraph(jobs, deps)
	return getOrderedJobs(job_graph)


def createJobGraph(jobs, deps):
	graph = JobGraph(jobs)
	# obj = {y: x.job for y, x in graph.graph.items()}
	# print(obj)
	for prereq, job in deps:
		# add edges
		graph.addPrereq(job, prereq)
	return graph

def getOrderedJobs(graph):
	result = []
	vertices = graph.vertices
	while len(vertices) != 0:
		vertex = vertices.pop()
		print(vertex.job, vertex.prereqs)
		isCycle = dfs(vertex, result)
		if isCycle:
			return []
	return result

def dfs(vertex, result):
	if vertex.visited:
		return False
	if vertex.visiting:
		return True
	vertex.visiting = True
	for prereq in vertex.prereqs:
		isCycle = dfs(prereq, result)
		if isCycle:
			return True
	vertex.visited = True
	# below row isn't necessary as
	# if we've marked .visited
	# then we won't go further
	# in the beginning of dfs()
	vertex.visiting = False
	result.append(vertex.job)
	return False


class JobGraph:
	def __init__(self, jobs):
		self.vertices = []
		self.graph = {}
		for x in jobs:
			self.insert(x)
	
	def insert(self, job):
		self.graph[job] = JobNode(job)
		self.vertices.append(self.graph[job])
		
	def addPrereq(self, job, prereq):
		jobNode = self.getNode(job)
		prereqNode = self.getNode(prereq)
		jobNode.prereqs.append(prereqNode)
	
	def getNode(self, job):
		# if job not in self.graph:
			# self.insert(job)
		return self.graph[job]
		
	
class JobNode:
	def __init__(self, job):
		self.job = job
		self.prereqs = []
		self.visited = False
		self.visiting = False

# 2nd way of solving
def topologicalSort(jobs, deps):
	job_graph = createJobGraph(jobs, deps)
	return getOrderedJobs(job_graph)

def createJobGraph(jobs, deps):
	graph = JobGraph(jobs)
	for job, dep in deps:
		# add edges
		graph.addDep(job, dep)
	return graph

def getOrderedJobs(graph):
	result = []
	verticesNoPre = list(filter(lambda vertex:
								vertex.numOfPrereqs == 0,
								graph.vertices))
	while len(verticesNoPre) != 0:
		vertex = verticesNoPre.pop()
		result.append(vertex.job)
		removeDeps(vertex, verticesNoPre)
	verticesPresent = any(vert.numOfPrereqs for vert in graph.vertices)
	return [] if verticesPresent else result

def removeDeps(vertex, verticesNoPre):
	while len(vertex.deps) != 0:
		depend = vertex.deps.pop()
		depend.numOfPrereqs -= 1
		if depend.numOfPrereqs == 0:
			verticesNoPre.append(depend)


class JobGraph:
	def __init__(self, jobs):
		self.vertices = []
		self.graph = {}
		for x in jobs:
			self.insert(x)
	
	def insert(self, job):
		self.graph[job] = JobNode(job)
		self.vertices.append(self.graph[job])
	
	def addDep(self, job, dep):
		jobNode = self.getNode(job)
		depNode = self.getNode(dep)
		jobNode.deps.append(depNode)
		depNode.numOfPrereqs += 1
	
	def getNode(self, job):
		# if job not in self.graph:
			# self.insert(job)
		return self.graph[job]
	

class JobNode:
	def __init__(self, job):
		self.job = job
		self.deps = []
		self.numOfPrereqs = 0


# approaches to tackle the problem
# a) DFS solution
# 1. jobs are vertices and deps are edges
# 2. take random job and look at it's prerequisites
# 3. apply DFS to go through all the prereqs
# 4. when vertex has no prereqs -> add to final array
# 5. come back to previous vertices and explore them
# 6. also keep track of visited vertices so as not to 
#    double count them
# 7. keep track of cycles => vertices that are currently
#    in process of being visited. Hence if find some vertex
#    that is currently in process => Cycle and invalid graph


# b) keep track of nodes that have no prerequisites
# 1. keep track of how many prereqs every vertex has
# 2. traverse only vertices that have no prereqs: noPre = []
# 3. .pop() from noPre, add to final array
# 4. remove all the dependencies of that vertex
# 5. update prereqs of that former dependencies
# 6. come back to noPre and check for vertcies there:
#    if they're some then repeat the process.
# 7. after some moment there'll be another vertex with
#    no prereqs -> add it to noPre
#    and repeat the process above.
# 8. finally last vertex will have no prereqs, add it to
#    noPre and from there to final array
# * if there is Cycle: noPre is blank, but there are still
#   vertices to explore => Cycle and invalid graph
