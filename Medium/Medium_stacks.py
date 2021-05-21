# 1 Balanced Brackets
def balancedBrackets(string):
	open_ = '[{('
	close_ = ')}]'
	match = {'}': '{', ']': '[', ')': '('}
	stack = []
	for x in string:
		if x in open_:
			stack.append(x)
		elif x in close_:
			if len(stack) == 0:
				return False
			elif match[x] == stack[-1]:
				# if matched open bracket == -1 
				# => our close one matches the last in stack
				stack.pop()
			else:
				return False
	return len(stack) == 0

# 2 Sunset views
# a
def sunsetViews(b, d):
	result = []
	srt = 0 if d == 'WEST' else len(b) - 1
	step = 1 if d == 'WEST' else -1
	idx = srt
	max_ = 0
	while idx >= 0 and idx < len(b):
		curr = b[idx]
		if curr > max_:
			result.append(idx)
		max_ = max(max_, idx)
		idx += step
	if d == 'EAST':
		return result[::-1]
	return result

# b 
def sunsetViews(b, d):
	result = []
	srt = 0 if d == 'EAST' else len(b) - 1
	step = 1 if d == 'EAST' else -1
	idx = srt
	while idx >= 0 and idx < len(b):
		curr = b[idx]
		while len(result) > 0 and b[result[-1]] <= curr:
			result.pop()
		result.append(idx)
		idx += step
	if d == 'EAST':
		return result[::-1]
	return result

# 3 Min Max Stack Construction
# mine
class MinMaxStack:
	def __init__(self):
		self.stack = []
		# due to O(1) S & T constraint
		# we'll keep Min/Max values
		self.MinMaxStack = []

	def peek(self):
		return self.stack[-1]

	def pop(self):
		self.MinMaxStack.pop()
		return self.stack.pop()

	def push(self, number):
		self.stack.append(number)
		if len(self.MinMaxStack) == 0:
			self.MinMaxStack.append({'min': number, 'max': number})
		else:
			min = self.MinMaxStack[-1]['min'] if\
				  self.MinMaxStack[-1]['min'] < number else number
			max = self.MinMaxStack[-1]['max'] if\
				  self.MinMaxStack[-1]['max'] > number else number
			self.MinMaxStack.append({'min': min, 'max': max})

	def getMin(self):
		return self.MinMaxStack[-1]['min']

	def getMax(self):
		return self.MinMaxStack[-1]['max']

# another way to make push()
	
	def push(self, number):
		newMinMax = {'min': number, 'max': number}
		if len(self.MinMaxStack):
			lastMinMax = self.MinMaxStack[-1]
			lastMinMax['min'] = min(lastMinMax['min'], number)
			lastMinMax['max'] = max(lastMinMax['max'], number)
		self.MinMaxStack.append(lastMinMax)
		self.stack.append(number)

# 4 Sort Stack
def sortStack(stack):
	if len(stack) == 0:
		return stack

	temp = stack.pop()

	sortStack(stack)
	helper(stack, temp)

	return stack

def helper(stack, value):
	if len(stack) == 0 or stack[-1] <= value:
		stack.append(value)
		return

	temp = stack.pop()
	helper(stack, value)

	stack.append(temp)

# 5 Next Greater Element
# mine
def nextGreaterElement(arr):
    new = [-1 for _ in range(len(arr))]

	idx = 0
	while idx != len(arr):
		curr = arr[idx]
		for i in range(idx + 1, len(arr) + idx):
			i = i % len(arr)
			if arr[i] > curr:
				new[idx] = arr[i]
				break
		idx += 1
	
	return new

# not mine `a`
def nextGreaterElement(arr):
	# in this solution we
	# add indicies on the
	# top of the stack
    res = [-1 for _ in range(len(arr))]
	stack = []
	
	for idx in range(2 * len(res)):
		idx = idx % len(res)
		
		while len(stack) != 0 and arr[stack[-1]] < arr[idx]:
			node = stack.pop()
			res[node] = arr[idx]
			
		stack.append(idx)
		
	return res

# not mine `b`
def nextGreaterElement(arr):
	# in this solution we
	# add values on the
	# top of the stack
	new = [-1 for _ in range(len(arr))]
	stack = []
	
	for i in range(2 * len(arr) - 1, -1, -1):
		i = i % len(new)
		
		while len(stack) != 0:
			if stack[-1] > arr[i]:
				new[i] = stack[-1]
				break
			else:
				stack.pop()
		stack.append(arr[i])

	return new
