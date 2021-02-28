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
 