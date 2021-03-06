# 1 Minimum waiting time
#mine
def minimumWaitingTime(queries):
	count = 0
	queries.sort()
	add = 0
	for x in range(1, len(queries)):
		count += queries[x - 1] + add
		add += queries[x - 1]
	return count
# a
def minimumWaitingTime(queries):
	queries.sort()
	temp = 0
	for x, y in enumerate(queries):
		temp += y * len(queries[x + 1:])
	return temp

# b
def minimumWaitingTime(queries):
	queries.sort()
	temp = 0
	for x in range(len(queries)):
		temp += queries[x] * len(queries[x + 1:])
	return temp

# 2 Class photos
#mine a
def classPhotos(reds, blues):
	reds.sort()
	blues.sort()
	colour = 'red' if reds[0] > blues[0] else 'blue'
	
	for x in range(len(reds)):
		if colour == 'red' and reds[x] <= blues[x]:
			return False
		elif colour == 'blue' and reds[x] >= blues[x]:
			return False
	return True
# mine b
def classPhotos(reds, blues):
	reds.sort(reverse=True)
	blues.sort(reverse=True)
	if reds[0] > blues[0]:
		for x in range(len(reds)):
			if reds[x] > blues[x]:
				continue
			return False
	elif reds[0] < blues[0]:
		for y in range(len(blues)):
			if reds[y] < blues[y]:
				continue
			return False
	else:
		return False
	return True

# not mine
def classPhotos(reds, blues):
	reds.sort(reverse=True)
	blues.sort(reverse=True)
	losing = 'RED' if reds[0] < blues[0] else 'BLUE'
	for x in range(len(reds)):
		if losing == 'RED':
			if reds[x] >= blues[x]:
				return False
		elif losing == 'BLUE':
			if reds[x] <= blues[x]:
				return False
	return True

# 3 Tandem bicycle
# mine
def tandemBicycle(red, blue, fastest):
	total = 0

	if fastest:
		red.sort()
		blue.sort(reverse=True)
	else:
		red.sort()
		blue.sort()

	for idx in range(len(red)):
		total += max(red[idx], blue[idx])

	return total

# not mine
def tandemBicycle(red, blue, fastest):
	red.sort()
	blue.sort()
	if fastest is not True:
		helper(red)

	total = 0
	for idx in range(len(blue)):
		total += max(red[idx], blue[len(blue) - idx - 1])
	return total

def helper(arr):
	i = 0
	j = len(arr) - 1
	while i < j:
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1
