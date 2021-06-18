# 1 Smallest Substring Containing
def smallestSubstringContaining(bigString, smallString):
    smallHashTable = {}
	createHashTable(smallString, smallHashTable)
	bounds = traverseString(smallHashTable, bigString)
	return getStringFromBounds(bounds, bigString)
	
def traverseString(smallHashTable, string):
	bigHashTable = {}
	markedLetters = 0
	# bounds below are for better Time Compex.
	StartEndIdx = [0, float('inf')]
	uniqueTokens = len(smallHashTable.keys())
	# (above) or just `len(smallString)`
	rightIdx = 0
	leftIdx = 0
	while rightIdx < len(string):
		token = string[rightIdx]
		if token not in smallHashTable:
			rightIdx += 1
			continue
		
		if token not in bigHashTable:
			bigHashTable[token] = 0
		bigHashTable[token] += 1
		
		# we can reach here if token is
		# in smallHashTable, no need to
		# check whether key is present
		# + if we have same character
		# which exceeds number in smallHashTable,
		# this check will handle this case as we've
		# pointed that only if `==`
		if smallHashTable[token] == bigHashTable[token]:
			markedLetters += 1
		# if we've counted all required amount
		# of letters, we can proceed.
		# `while` below will continue till
		# either tokens as required and found
		# by us are equal or left border smaller/equal
		# to right border
		while uniqueTokens == markedLetters and leftIdx <= rightIdx:
			# keep snapshot of best array till we
			# alter the number in bigHashTable
			StartEndIdx = getRanges(leftIdx, rightIdx,
								    StartEndIdx[0], StartEndIdx[1])
			leftToken = string[leftIdx]
			# reasons for below check:
			# a) leftIdx starts at 0, hence we may
			# have unrelated character
			# b) we'll move leftIdx to rightIdx and as
			# we did above with righIdx, we may encounter
			# unrelated characters
			if leftToken not in smallHashTable:
				leftIdx += 1
				continue
			# if number of tokens equal in both ht,
			# then we need to decrease overall
			# counted letters as it's obvious that
			# we'll get insufficient number of them
			# due to the action after this `if`
			if smallHashTable[leftToken] == bigHashTable[leftToken]:
				markedLetters -= 1
			bigHashTable[leftToken] -= 1
			leftIdx += 1
		rightIdx += 1
			
	return StartEndIdx
	
def getStringFromBounds(ranges, string):
	if ranges[1] == float('inf'):
		return ""
	return string[ranges[0]:ranges[1] + 1]

def createHashTable(string, ht):
	for token in string:
		if token not in ht:
			ht[token] = 0
		ht[token] += 1

def getRanges(idx1, idx2, idx3, idx4):
	return [idx1, idx2] if (idx2 - idx1) < (idx4 - idx3) else [idx3, idx4]
