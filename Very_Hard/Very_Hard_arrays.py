# 1 Apartment Hunting
# T: O(b^2*r) S: O(b)
def apartmentHunting(blocks, reqs):
	maxDist = [float('-inf') for _ in blocks]
	for block in range(len(blocks)):
		for i in range(len(reqs)):
			smallest = float('inf')
			for j in range(len(blocks)):
				if blocks[j][reqs[i]]:
					smallest = min(smallest, abs(block - j))
			# below is max() because we'll go through it
			# while all reqs are not visited. And according
			# to the task we need to pick the biggest number
			# throughout all reqs for each block
			maxDist[block] = max(maxDist[block], smallest)
	
	return results(maxDist)

def results(arr):
	output = float('inf')
	# choose min and return
	# that idx
	for idx in range(len(arr)):
		output = min(output, arr[idx])
	return arr.index(output)

# def results(arr):
# 	output = float('inf')
# 	i = 0
# 	for idx in range(len(arr)):
# 		value = arr[idx]
# 		if value < output:
# 			i = idx
# 			output = value
# 	return i

# T: O(b * r) S: O(br)
def apartmentHunting(blocks, reqs):
	# 1. precompute values for every requirement
	#    in separate array for every requirement
	# 2. find closest index to every requirement
    minDist = list(map(lambda req: getMinDist(blocks, req), reqs))
	# 3. Take each row from created arrays (requirements)
	#    and find max(). Because we need the farthest
	#    from all the facilities that are closest
	maxDist = getMax(minDist, blocks)
	return getResult(maxDist)
	
def getMinDist(blocks, req):
	minDistances = [0 for _ in blocks]
	closest = float('inf')
	for i in range(len(blocks)):
		if blocks[i][req]:
			closest = i
		minDistances[i] = getDifference(i, closest)
		# Ex: if True and closest = 3 then i = 3
		# hence difference = 0. Else closest will
		# keep last index where req was True

	# to find actual min values we need to iterate
	# in reverse order
	#    [gym, gym, store, school, gym]
	# -> [0, 0, 1, 2, 0]
	# <- [0, 0, 1, 1, 0]
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closest = i
		minDistances[i] = min(minDistances[i],
							  getDifference(i, closest))
	
	return minDistances

def getMax(dist, blocks):
	maxDist = [0 for _ in blocks]
	for i in range(len(blocks)):
		minDist = list(map(lambda d: d[i], dist))
		maxDist[i] = max(minDist)
	# [i] [i]
	# [0, 0, 1, 1, 2]
	# [0, 1, 3, 4, 0]
	# [1, 2, 0, 1, 3]
	# We'll go through columns in reqs
	# and take max from it
	return maxDist

def getResult(arr):
	output = float('inf')
	for i in arr:
		output = min(output, i)
	return arr.index(output)

def getDifference(i, j):
	return abs(i - j)
