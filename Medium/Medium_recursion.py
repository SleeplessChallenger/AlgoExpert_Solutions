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

# 3 Phone Number Mnemonics
hashtable = {'1': ['1'], '2': ['a','b','c'], '3': ['d','e','f'],
			 '4': ['g','h','i'], '5': ['j','k','l'],
			 '6': ['m','n','o'], '7': ['p','q','r','s'],
			 '8': ['t','u','v'], '9': ['w','x','y','z'], '0': ['0']}

def phoneNumberMnemonics(phone):
	idx = 0
	curr =['0'] * len(phone)
	arr = []
	helper(idx, curr, arr, phone)
	return arr

def helper(idx, curr, arr, phone):
	if idx == len(phone):
		temp = ''.join(curr)
		arr.append(temp)
	else:
		digit = phone[idx]
		letters = hashtable[digit]
		for x in letters:
			curr[idx] = x
			helper(idx+1, curr, arr, phone)
