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

# 2 Longest Balanced Substring
# T: O(n^3) S: O(n)
def longestBalancedSubstring(string):
    maxS = 0
	for i in range(len(string)):
		for j in range(i + 1, len(string), 2):
			# 2 as balanced can't be an odd number
			if helper(i, j, string):
				curr = len(string[i:j + 1])
				maxS = max(curr, maxS)
	
	return maxS

def helper(i, j, string):
	stack = []
	open = '('
	close = ')'
	
	for x in string[i:j + 1]:
		if x in open:
			stack.append(x)
		else:
			if len(stack) == 0:
				return False
			else:
				stack.pop()
	
	return len(stack) == 0

# T: O(n) S: O(n)
# when close bracket is met, we .pop() from stack 
# at first as we presume it's open bracket. But after it,
# if len(stack) == 0, it does mean we cannot calc. length
# as length requires some idx to be in the stack (bacause
# AFTER that idx our length starts).
# Why put -1? After -1, i.e. from 0, our substring starts
# and our bigger number is closing bracket.
# (()) ) - x ( : Right after x our new substring starts
def longestBalancedSubstring(string):
    stack = [-1]
	open = '('
	close = ')'
	maxS = 0
	
	for t in range(len(string)):
		bracket = string[t]
		if bracket in open:
			stack.append(t)
		else:
			if emptyStack(stack):
				# calc. length
				stack.pop()
				maxS = max(maxS, t - stack[-1])
			else:
				stack.pop()
				stack.append(t)
	
	return maxS

def emptyStack(stack):
	return len(stack) - 1 != 0

# T: O(n) S: O(1)
# we need to put checks after counter increase
# as in such case: '()' after ')' will be visited
# we can't multiply because we'll leave the loop
def longestBalancedSubstring(string):
    op_count = 0
	cl_count = 0
	op = '('
	cl = ')'
	maxS = 0
	
	for i in string:	
		if i in op:
			op_count += 1
		elif i in cl:
			cl_count += 1
		
		if op_count == cl_count:
			maxS = max(maxS, op_count * 2)
			# not op_count * cl_count as
			# they may be 1 and 1
		elif cl_count > op_count:
			cl_count, op_count = 0, 0
			
	op_count = 0
	cl_count = 0
	
	for i in reversed(range(len(string))):			
		br = string[i]

		if br in op:
			op_count += 1
		elif br in cl:
			cl_count +=1
		
		if op_count == cl_count:
			maxS = max(maxS, op_count * 2)
		elif op_count > cl_count:
			op_count, cl_count = 0, 0
	
	return maxS
