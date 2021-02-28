# 1 Permutations
def getPermutations(arr):
	perms = []
	helper(0, arr, perms)
	return perms

def helper(idx, arr, perms):
	if idx == len(arr) - 1:
		perms.append(arr[:])
	else:
		for x in range(idx, len(arr)):
			swap(x, idx, arr)
			helper(idx + 1, arr, perms)
			swap(x, idx, arr)

def swap(idx1, idx2, arr):
	arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# 2 Powerset
# a
def powerset(arr):
	cont = [[]]
	for x in arr:
		for y in range(len(arr)):
			temp = cont[y]
			cont.append(temp + [x])
	return cont

# b
def powerset(arr, idx=None):
	if idx is None:
		idx = len(arr) - 1
	if idx < 0:
		return [[]]
	ele = arr[idx]
	subs = powerset(arr, idx-1)
	for x in range(len(subs)):
		temp = subs[x]
		subs.append(temp + [ele])
	return subs
