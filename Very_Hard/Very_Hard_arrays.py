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

# 2 Calendar Matching
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	newCalen1 = updateCalender(calendar1, dailyBounds1)
	newCalen2 = updateCalender(calendar2, dailyBounds2)
	mergedCalen = mergeCalendars(newCalen1, newCalen2)
	flattened_calen = flatten(mergedCalen)
	return getResult(flattened_calen, meetingDuration)
	
def mergeCalendars(arr1, arr2):
	i, j = 0, 0
	result = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i][0] > arr2[j][0]:
			result.append(arr2[j])
			j += 1
		else:
			result.append(arr1[i])
			i += 1
			
	while i < len(arr1):
		result.append(arr1[i])
		i += 1
		
	while j < len(arr2):
		result.append(arr2[j])
		j += 1
	
	return result

def flatten(arr):
	# find values that overlap
	# 1
	if len(arr) < 2:
		return arr

	output = []
	current = arr[0]
	output.append(current)
	for next_arr in arr:
		if next_arr[0] <= current[1]:
			current[1] = max(current[1], next_arr[1])
		else:
			current = next_arr
			output.append(current)
			
	
	return output
	# 2
	# result = [arr[0][:]]
	# for i in range(1, len(arr)):
	# 	curr = arr[i]
	# 	# !!!below use `-1` and not `i - 1`
	# 	# as we need from `result` and not from
	# 	# array
	# 	prev = result[-1]
	# 	# if previous meeting ends
	# 	# after current starts
	# 	if curr[0] <= prev[1]:
	# 		newMeet = [prev[0], max(curr[1], prev[1])]
	# 		result[-1] = newMeet
	# 	else:
	# 		result.append(curr[:])
	# return result

def getResult(arr, t):
	res = []
	for i in range(1, len(arr)):
		prevEnd = arr[i - 1][1]
		currStart = arr[i][0]
		duration = currStart - prevEnd
		if duration >= t:
			res.append([prevEnd, currStart])
	
	return list(map(lambda x: [minTotime(x[0]), minTotime(x[1])], res))
	
def updateCalender(arr, bound):
	newArr = arr[:]
	newArr.insert(0, ['0:00', bound[0]])
	newArr.append([bound[1], '23:59'])
	return list(map(lambda x: [timeTomin(x[0]), timeTomin(x[1])], newArr))

def timeTomin(t):
	h, m = list(map(int, t.split(':')))
	# a, b = map(int, t.split(':'))
	return h * 60 + m

def minTotime(var):
	h = var // 60
	m = var % 60
	hStr = str(h)
	mStr = '0' + str(m) if m < 10 else str(m)
	return hStr + ':' + mStr
