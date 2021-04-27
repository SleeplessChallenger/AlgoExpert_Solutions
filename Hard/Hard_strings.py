# 1 Longest Substring Without Duplication
def longestSubstringWithoutDuplication(string):
	ht = {}
	longest = [0, 1]
	start = 0

	for idx in range(len(string)):
		letter = string[idx]

		if letter in ht:
			start = max(start, ht[letter] + 1)
			# max() from 'start' which will
			# depict idx that we've started
			# current substring from and
			# letter's idx that is already in ht + 1
		if longest[1] - longest[0] < idx - start + 1:
			longest = [start, idx + 1]
		ht[letter] = idx

	return string[longest[0]:longest[1]]

# 2 Underscorify Substring
def underscorifySubstring(string, substring):
    collapsed = collapse(getLocations(string, substring)) 
	return underScorify(collapsed, string)

def getLocations(string, substring):
	start = 0
	locations = []
	while start < len(string):
		idx = string.find(substring, start)
		if idx != -1:
			locations.append([idx, idx + len(substring)])
			start = idx + 1
		else:
			break
	return locations

def collapse(locations):
	if not len(locations):
		return locations
	result = []
	current = locations[0]
	result.append(current)
	
	for next_arr in locations:
		if next_arr[0] <= current[1]:
			current[1] = max(next_arr[1], current[1])
		else:
			result.append(next_arr)
			current = next_arr

	return result

def underScorify(array, string):
	locIdx = 0
	strIdx = 0
	result = []
	idx = 0
	Check = False
	
	while strIdx < len(string) and locIdx < len(array):
		if strIdx == array[locIdx][idx]:
			result.append('_')
			Check = not Check
			if not Check:
				locIdx += 1
			idx = 0 if idx == 1 else 1
		result.append(string[strIdx])
		strIdx += 1
	
	if locIdx < len(array):
		result.append('_')
	elif strIdx < len(string):
		result.append(string[strIdx:])
	return ''.join(result)

# 3 Pattern Matcher
# mine
def patternMatcher(pattern, string):
	if len(pattern) > len(string):
		return []
	new_pattern = checkPattern(pattern)
	ht, firstY = getPosition(new_pattern)
	wasSwap = new_pattern[0] != pattern[0]

	if 'y' in ht and ht['y'] > 0:
		for xIdx in range(1, len(string)):
			lenY = (len(string) - xIdx * ht['x'])/ht['y']
			if lenY <= 0 or lenY % 1 != 0:
				continue
			lenY = int(lenY)
			yIdx = firstY * xIdx
			xString = string[:xIdx]
			yString = string[yIdx:yIdx + lenY]
			temp = map(lambda token: xString if token == 'x'
											 else yString,
											 new_pattern)
			if string == ''.join(temp):
				return [xString, yString] if not wasSwap\
										  else [yString, xString]
	else:
		lenX = len(string)/ht['x']
		if lenX % 1 == 0:
			lenX = int(lenX)
			xString = string[:lenX]
			temp = map(lambda token: xString, new_pattern)
			if string == ''.join(temp):
				return [xString, ''] if not wasSwap\
									 else ['', xString]
	return []

def checkPattern(pattern):
	if pattern[0] == 'x':
		return list(pattern)
	new_pattern = []
	for x in pattern:
		if x == 'x':
			new_pattern.append('y')
		elif x == 'y':
			new_pattern.append('x')
	return new_pattern

def getPosition(pattern):
	ht = {}
	for x in pattern:
		if x not in ht:
			ht[x] = 0
		ht[x] += 1
	pos = pattern.index('y') if 'y' in pattern\
							 else -1
	return ht, pos

# not mine
def patternMatcher(pattern, string):
	if len(pattern) > len(string):
		return []
	new_pattern = checkPattern(pattern)
	ht = {'x': 0, 'y': 0}
	firstY = getPosition(new_pattern, ht)
	wasSwap = new_pattern[0] != pattern[0]

	if ht['y'] > 0:
		for xIdx in range(1, len(string)):
			lenY = (len(string) - xIdx * ht['x'])/ht['y']
			if lenY <= 0 or lenY % 1 != 0:
				continue
			lenY = int(lenY)
			yIdx = firstY * xIdx
			xString = string[:xIdx]
			yString = string[yIdx:yIdx + lenY]
			temp = map(lambda token: yString if token == 'y'
											 else xString,
											 new_pattern)
			if string == ''.join(temp):
				return [xString, yString] if not wasSwap\
										  else [yString, xString]
	else:
		lenX = len(string)/ht['x']
		if lenX % 1 == 0:
			lenX = int(lenX)
			xString = string[:lenX]
			temp = map(lambda token: xString, new_pattern)
			if string == ''.join(temp):
				return [xString, ''] if not wasSwap\
									 else ['', xString]
	return []

def checkPattern(pattern):
	pattern = list(pattern)
	if pattern[0] == 'x':
		return pattern
	return list(map(lambda token: 'x' if token == 'y'
									  else 'y', pattern))

def getPosition(pattern, ht):
	pos = None
	for idx in range(len(pattern)):
		ht[pattern[idx]] += 1
		if pattern[idx] == 'y' and not pos:
			pos = idx
	return pos

# 1 check whether pattern[0] is x or y
#	if x: return elif y: change y for x and vice versa
# 2 count the number of x and y (ht); get position
#   of first y in the pattern
# 3 if y > 0: (len(string) - len(x) * num of x)/ num of y
#   check if resulted number positive and not a decimal
#
#	yIdx = firstYPos (in pattern) * len of x
#	yIdx = 2 * 1 = 2
# 4 x = string[0:len(x)]
#	y = string[yIdx:len of Y]
# 5 replace in pattern if with new X and the same with y
# 	and check if it == string
#   BUT: if you've changed y for x in pattern: swap here
