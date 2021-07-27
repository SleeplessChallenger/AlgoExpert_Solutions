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

# 3 Waterfall Streams
# 3 - 1
# T: O(w^2 * h) S: O(1)
# without separate variables,
# just using `+=`
def waterfallStreams(arr, source):
    arr[0][source] = -1
	
	for i in range(1, len(arr)):
		# we cannot use `source`
		# as water will be splitted
		# hence we iterate over `prev row`
		for j in range(len(arr[i - 1])):
			# if above row doesn't
			# have water -> skip.
			# `>= 0` is essential as
			# `- 1` will be changed
			if arr[i - 1][j] >= 0:
				continue
			# if curr row & curr col != block
			elif arr[i][j] != 1:
				arr[i][j] += arr[i - 1][j]
				continue
			
			# elif it's a block
			elif arr[i][j] == 1:
				left = j - 1
				while left >= 0:
# 1. # # # _ _
# 2. _ _ _ _ #
# 3. _ _ _ # _
# if we're at 3rd row (block)
# and at 2nd row water will be
# splitted then right direction
# is a wall. Same check with left
					if arr[i - 1][left] == 1:
						break
					if arr[i][left] != 1:
						arr[i][left] += arr[i - 1][j] * 0.5
						break
					left -= 1
						
				right = j + 1
				while right < len(arr[i - 1]):
					if arr[i - 1][right] == 1:
						break
					if arr[i][right] != 1:
						arr[i][right] += arr[i - 1][j] * 0.5
						break
					right += 1

	result = list(map(lambda x: x * -100, arr[-1]))
	return result

# 3 - 2
# with separate `water` variable
def waterfallStreams(arr, source):
    arr[0][source] = -1
	
	for i in range(1, len(arr)):
		# we cannot use `source`
		# as water will be splitted
		# hence we iterate over `prev row`
		for j in range(len(arr[i - 1])):
			# if above row doesn't
			# have water -> skip.
			# `>= 0` is essential as
			# `- 1` will be changed
			if arr[i - 1][j] >= 0:
				continue
			# if curr row & curr col != block
			elif arr[i][j] != 1:
				arr[i][j] += arr[i - 1][j]
				continue
			
			# elif it's a block	
			water = arr[i - 1][j] / 2

			left = j 
			while left - 1 >= 0:
				left -= 1
				if arr[i - 1][left] == 1:
					break
				if arr[i][left] != 1:
					arr[i][left] += water
					break

			right = j
			while right + 1 < len(arr[i - 1]):
				right += 1
				if arr[i - 1][right] == 1:
					break
				if arr[i][right] != 1:
					arr[i - 1][right] += water
					break

	result = list(map(lambda x: x * -100, arr[-1]))
	return result

# 4 Minimun Area Rectangle
# T: O(n^2) S: O(n)
def minimumAreaRectangle(points):
    visited = {}
	minDiff = float('inf')
	plot = createPlot(points)
	plotKeys = sorted(plot.keys())
	# use separate variable
	# as `sorted()` will remove `values()`
	for x in plotKeys:
		values = plot[x]
		values.sort()
		# `values` is subarray =>
		# time compl. isn't n^2*logn, but n*logn
		for val in range(len(values)):
			# iterate till current
			for prevVal in range(0, val):
				# create all possible pairs
				# and store them in `visited`
				curr = values[val]
				prev = values[prevVal]
				yKey = f"{prev}:{curr}"
					
				if yKey in visited:
					# if we have such y-values
					# that means we can form
					# a rectangle with
					# similar/another x
					# `- visited[yKey]` is our prev
					# x which is to the left of current
					temp = (curr - prev) * (x - visited[yKey])
					minDiff = min(minDiff, temp)
				# update key with y-values
				# with the most recent x
				# as we need min() so there is
				# no need to keep furtherest
				visited[yKey] = x
	
	return minDiff if minDiff != float('inf') else 0
	
def createPlot(plots):
	ht = {}
	for value in plots:
		x, y  = value
		if x not in ht:
			ht[x] = []
		ht[x].append(y)

	return ht

# T: O(n^2) S: O(n)
def minimumAreaRectangle(points):
    allPoints = createSet(points)
	minVal = float('inf')
	
	for point in range(len(points)):
		curr = points[point]
		for prevPoint in range(0, point):
			prev = points[prevPoint]
			if curr[0] != prev[0] and curr[1] != prev[1]:
				# as we need different x & y values
				# in two points (but similar x and y is OK)
				oppositeOne = f"{curr[0]}:{prev[1]}"
				oppositeTwo = f"{prev[0]}:{curr[1]}"
	
				if oppositeOne in allPoints and oppositeTwo in allPoints:
					temp = abs(curr[0] - prev[0]) * abs(curr[1] - prev[1])
					minVal = min(temp, minVal)
				
	return minVal if minVal != float('inf') else 0
	
def createSet(points):
	res = set()
	for point in points:
		# we cannot store list()
		# as `in`check will give
		# False, hence we create
		# string key
		x, y = point
		key = f"{x}:{y}"
		res.add(key)

	return res

# 5 Line Through Points
# `points` has 1. no dupl 2. len() >= 1
# points = [[x, y], [x, y] ...]
# slope = (y2 - y1) / (x2 - x1)
# Steps:
# 	1. traverse with double loop
# 	2. create ht to put all the possible lines
# 		and their number
# 		- key will be "a/b" reduced & str
# 	3. after every iteration of lower loop
# 		we take biggest number and keep `maxNum`
# 	4. after we start new outer loop -> new ht

def lineThroughPoints(points):
	return createPoints(points)

def createPoints(points):
	maxLines = 1
	# as at least one point present
	
	for i in range(len(points)):
		ht = {}
		coord_one = points[i]
		for j in range(i + 1, len(points)):
			coord_two = points[j]
			rise, run = addPoints(coord_one, coord_two)
			# slope = rise/run
			slopeKey = stringify(rise, run)
			
			if slopeKey not in ht:
				ht[slopeKey] = 1
				
			ht[slopeKey] += 1

		currMax = max(ht.values(), default=0)
		# `default` as if we have no values -> error
		maxLines = max(maxLines, currMax)
	
	return maxLines

def addPoints(coord_one, coord_two):
	x1, y1 = coord_one
	x2, y2 = coord_two
	
	slope = [1, 0]
	# if vertical line -> no slope
	
	if x2 != x1:
		yNew = y2 - y1
		xNew = x2 - x1
		gcd = makeGCD(abs(yNew), abs(xNew))
		# abs() because `makeGCD` doesn't work with negative
		xNew = xNew // gcd
		yNew = yNew // gcd
		
		if xNew < 0:
		# 1. xNew < 0 & yNew < 0 => positive
			# our changes will make num positive
		# 2. xNew < 0 & yNew > 0 => negative
			# we'll convert xNew to pos, but instead
			# yNew will hold neg value
		# 3. xNew > 0 & yNew > 0 => positive
		# 4. xNew > 0 & yNew < 0 => negative
			# yNew will already have neg in numerator
			xNew *= -1
			yNew *= -1
		
		slope = [yNew, xNew]
		
	return slope
			
def stringify(key1, key2):
	return f"{key1}:{key2}"
	
def makeGCD(a, b):
	while True:
		if a == 0:
			return b
		if b == 0:
			return a
		
		a, b = b, a % b
