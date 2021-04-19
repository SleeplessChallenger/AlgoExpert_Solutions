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
