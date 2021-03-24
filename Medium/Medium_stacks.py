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

 
