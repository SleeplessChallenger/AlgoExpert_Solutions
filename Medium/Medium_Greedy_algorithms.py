# 1 Task assignment
def taskAssignment(k, tasks):
	sorte = sorted(tasks)
	cont = []
	hashtable = helper(tasks)

	for x in range(k):

		task1 = sorte[x] # take from beginning time duration
		idxs1 = hashtable[task1] # receive list of indicies of particular key
		idx1 = idxs1.pop()

		idx_large = (len(tasks) - 1) - x # take index of largest from the end on every loop
		task2 = sorte[idx_large]
		idxs2 = hashtable[task2]
		idx2 = idxs2.pop()

		cont.append([idx1, idx2])

	return cont

def helper(arr):
	hashtable = {}
	for x, y in enumerate(arr):
		if y not in hashtable:
			hashtable[y] = [x]
		else:
			hashtable[y] += [x]
	return hashtable

# 2 Valid Starting City
# T: O(n^2) S: O(1)
def validStartingCity(distances, fuel, mpg):
	num_cities = len(distances)

	for x in range(num_cities):
		miles = 0

		for y in range(x, x + num_cities):
			if miles < 0:
				break # == continue

			y = y % num_cities
			# if we have y > len(distances) - 1
			# then we need to return to '0' idx
			fuelCurr = fuel[y]
			distToNext = distances[y]
			miles += fuelCurr * mpg - distToNext

		if miles >= 0:
			return x
	return -1

# T: O(n) S: O(1)
def validStartingCity(distances, fuel, mpg):
	num_cities = len(distances)
	miles = 0

	milesAtFirst = 0
	idx = 0

	for x in range(1, num_cities):

		fuelPrev = fuel[x - 1]
		distPrev = distances[x - 1]
		miles += mpg * fuelPrev - distPrev

		if miles < milesAtFirst:
			milesAtFirst = miles
			idx = x

	return x
