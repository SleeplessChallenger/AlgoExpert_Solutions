# 1 Shorten Path
# 1
def shortenPath(path):
    stack = []
	result = path.split('/')
	
	#for symb in result:
		#if symb == '' or symb == '.':
			#result.remove(symb)
	# another way
	result = filter(helper, path.split('/'))
		 
	slashBegin = path[0] == '/'
	if slashBegin:
		stack.append('')
		# 'join' in the end will see some
		# element in the stack 
	for value in result:
		if value == '..':
			if len(stack) == 0 or stack[-1] == '..':
				stack.append(value)
			elif stack[-1] != '':
				stack.pop()
			elif stack[-1] == '':
				continue
		else:
# if we have root (aka /) and then .. =>
# do nothing (no if statement for this case and just next iteration)
# so as not to pop that root directory
# but if it's not '' (== root directory) => remove: elif stack[-1] != '':

# if we have ../../foo => relative path
# so we mustn't remove '..': if len(stack) == 0
			stack.append(value)

	if len(stack) == 1 and stack[0] == '':
		return '/'
	return '/'.join(stack)

def helper(value):
	return len(value) > 0 and value != '.'

# 2
def shortenPath(path):
    stack = []
	result = path.split('/')
	new = []

	for symb in result:
		if len(symb) > 0 and symb != '.':
			new.append(symb) 

	slashBegin = path[0] == '/'
	if slashBegin:
		stack.append('')
	
	for value in new:
		if value == '..':
			if len(stack) == 0 or stack[-1] == '..':
				stack.append(value)
			elif stack[-1] != '':
				stack.pop()
			elif stack[-1] == '':
				continue
		else:
			stack.append(value)

	if len(stack) == 1 and stack[0] == '':
		return '/'
	return '/'.join(stack)
