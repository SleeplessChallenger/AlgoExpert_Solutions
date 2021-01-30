#1)Two number sum

#1
def twoSum(arr, targetSum):
	i = 0
	j = 1
	while i < len(arr):
		while j < len(arr):
			if arr[j] + arr[i] == targetSum:
				return [arr[j],arr[i]]
			j += 1
		i += 1
		j = i + 1
	return []

#2
def QuickSort(arr):
	less = []
	equal = []
	more = []
	if len(arr) > 1:
		for x in arr:
			pillar = arr[0]
			if x > pillar:
				more.append(x)
			elif x < pillar:
				less.append(x)
			else: #pillar == x
				equal.append(x)
		return QuickSort(less) + equal + QuickSort(more)
	else:
		return arr


def twoSumQuick(arr, targetSum):
	result = QuickSort(arr)
	left = 0
	right = len(result) - 1
	while left < right:
		total = arr[left] + arr[right]
		if  total == targetSum:
			return [arr[left], arr[right]]
		elif total < targetSum:
			left += 1
		else:
			right -= 1
	return -1
print(twoSumQuick([3,5,-4,8,11,-1,1,6],10))


#2)Validate subsequence

def validSubs(arr, seq):
	i = 0
	j = 0
	while i < len(arr):
		if arr[i] == seq[j]:
			j += 1
		if len(seq) == j:
			return True
		i += 1
	return False
print(validSubs([5,1,22,25,6,8,10],[1,6,-1,10]))

#3) Find closest value in BST

class BST:

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

def findClosestBST(tree, target):
	closest = float('inf')
	root = tree
	while root:
		if abs(target - root.value) < abs(target - closest):
			closest = root.value
		if target > root.value:
			root = root.right
		elif target < root.value:
			root = root.left
		else:
			break
	return closest

#4) Branch sums
def branchSums(root):
	result = []
	temp = 0
	def traverse(root, temp):
		newTemp = temp + root.value
		if root.left:
			traverse(root.left, newTemp)
		if root.right:
			traverse(root.right, newTemp)
		if root.left is None and root.right is None:
			result.append(newTemp)
	traverse(root, temp)
	return result

#same but with minor tweak
def branchSums2(root):
	result = []
	def traverse(root, temp = 0):
		newTemp = temp + root.value
		if root.left:
			traverse(root.left, newTemp)
		if root.right:
			traverse(root.right, newTemp)
		if root.left is None and root.right is None:
			result.append(newTemp)
	traverse(root, temp = 0)
	return result

#5) Node depths

#1
def depthsRecur(root, depth = 0):
	if root is None:
		return 0
	return depth + depthsRecur(root.left, depth + 1) + depthsRecur(root.right, depth + 1)

#2
def depthsIter(root):
	result = 0
	stack = [{'node':root, 'depth':0}]
	while len(stack) > 0:
		info = stack.pop()
		node, fig = info['node'], info['depth']
		if node is None:
			continue
		result += fig
		stack.append({'node':node.left, 'depth':fig + 1})
		stack.append({'node':node.right, 'depth': fig + 1})
	return result


#6) Nth Fibonacci

#1
def fibOrd(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibOrd(n - 1) + fibOrd(n - 2)

#2
def fibMemo(n, memo = {1:0, 2:1}):
	if n in memo:
		return memo[n]
	memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
	return memo[n]

#3
def fibBest(n):
	i = 3
	repos = [0,1]
	while i <= n:
		temp = repos[0] + repos[1]
		repos[0] = repos[1]
		repos[1] = temp
		i += 1
	return repos[1] if n > 1 else repos[0]


#7) dfs
def dfs(self, arr):
	arr.append(self.name)
	for x in self.children:
		x.dfs(arr)
	return arr

#8) Product sum
def productSum(arr,mult = 1):
	total = 0
	for x in arr:
		if type(x) == list:
			total += productSum(x, mult + 1)
		else:
			total += 1
	return total * mult


#9) Binary Search
def binarySearch(arr, target):
	left = 0
	right = len(arr) - 1
	middle = (left + right) // 2
	while left <= right and arr[middle] != target:
		if arr[middle] > target:
			right = middle - 1
		elif arr[middle] < target:
			left = middle + 1
		middle = (left + right) // 2
	if arr[middle] == target:
		return middle
	return -1



#10) Three largest numbers

#1
def threeLargest(arr):
	first = 0
	second = 0
	third = 0
	for x in arr:
		if x >= first:
			first, second, third = x, first, second
		elif x >= second:
			second, third = x, second
		elif x > third:
			third = x
	return [third, second, first]

#2
def threeAnother(arr):
	result = [None, None, None]
	for x in arr:
		helper(x, result)
	return result

def helper(x, result):
	if result[2] is None or x > result[2]:
		put(2, x, result)
	elif result[1] is None or x > result[1]:
		put(1, x, result)
	elif result[0] is None or x > result[0]:
		put(0, x, result)

def put(idx, x, result):
	for y in range(idx + 1):
		if y == idx:
			result[y] = x
		else:
			result[y] = result[y + 1]

#11) Bubble sort
def bubbleSort(arr):
	i = len(arr) - 1
	j = 0
	while i > 0:
		noSwaps = True
		while j < i:
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				noSwaps = False
			else:
				j += 1
		if noSwaps:
			return arr
		i -= 1
		j = 0
	return arr

#12) Selection Sort

def selectSort(arr):
	i = 0
	j = i + 1
	while i < len(arr):
		min_ = i
		while j < len(arr):
			if arr[min_] > arr[j]:
				min_ = j
				j += 1
			else:
				j += 1
		if min_ != i:
			arr[min_], arr[i] = arr[i], arr[min_]
		i += 1
		j = i + 1
	return arr

#13) Insertion sort

def insertSort(arr):
	i = 1
	j = i -1
	while i < len(arr):
		min_ = arr[i]
		while j >= 0 and min_ < arr[j]:
			arr[j + 1], arr[j] = arr[j], arr[j + 1]
			j -= 1
		arr[j + 1] = min_
		i += 1
		j = i - 1
	return arr


#14) Palindrome check

#1
def isPalindrome(string):
	if len(string) == 1:
		return True
	if len(string) == 2:
		return string[0] == string[1]
	if string[0] == string[-1]:
		return string[1:-1]
	return False

#2
def alsoPalindrome(string):
	if len(string) == 0 or len(string) == 1:
		return True
	if string[0] == string[-1]:
		return string[1:-1]
	return False


#15) Caesar cipher encryptor

#1
def encrypt(string):
	result = []
	key = key % 26
	for x in string:
		var = ord(x) + key
		if var <= 122:
			result.append(chr(var))
		else:
			result.append(chr(96 + var % 122))
	return ''.join(result)

#2
def encryptCustom(string):
	alph = ['type alphabet here']
	result = []
	key = key % 26
	for x in string:
		result.append(helper(key, x, alph))
	return result

def helper(alph, x, key):
	letter = alph.index(x) + key
	return alph[letter % 26]


#16) Run Length encoding

def isLength(string):
	result = []
	count = 1
	for x in range(1,len(string)):
		prev = string[x - 1]
		curr = string[x]
		if count == 9 or prev != curr:
			result.append(str(count))
			result.append(prev)
			count = 0
		count += 1
	result.append(str(count))
	result.append(string[-1])
	return ''.join(result)





























\



#Nth fibonacci
def fib_naive(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib_naive(n-1) + fib_naive(n-2)

#Actually the one above is pretty bad as Time complexity 2^n.

#DFS graph
#mine was when in the __init__ is dict(), Clement one is when in the __init__ list()

def dfs_list(self,array):
	array.append(self.name)
	for x in self.children:
		x.dfs_list(array)
	return array

#mine
def dfs_dict(self,vertex):
	explored = {}
	result = []
	def traverse(vertex):
		if vertex:
			explored[vertex] = True
			result.append(vertex)
			for x in self.adjacencyList[vertex]:
				if x not in explored:
					traverse(x)
		return
	traverse(vertex)
	return result




#Find three largest numbers 
def find(arr):
	first = float('-inf')
	second = float('-inf')
	third = float('-inf')
	for x in arr:
		if x >= first:
			first, second, third = x, first, second
		elif x >= second:
			second, third = x, second
		elif x > third:
			third = x
	return [third, second, first]

#Clement's solution
def main_func(arr):
	result = [None, None, None]
	for x in arr:
		helper1(result, x)
	return result

def helper1(result, x):
	if result[2] is None or x > result[2]:
		helper2(result, x, 2)
	elif result[1] is None or x > result[1]:
		helper2(result, x ,1)
	elif result[0] is None or x > result[0]:
		helper2(result, x, 0)

def helper2(result, x, idx):
	for y in range(idx + 1):
		if y == idx:
			result[y] = x
		else:
			result[y] = result[y + 1]


#Node depths

#recur
def sum_depth(root, depth = 0):
	if root is None:
		return 0
	return sum_depth(root, depth + 1) + sum_depth(root, depth + 1)


#iter
def sum_Iter(root):
	result = 0
	stack = [{'node':root, 'depth':0}]
	while len(stack) > 0:
		bucket = stack.pop()
		node, depth = bucket['node'], bucket['depth']
		if node is None:
			continue
		result += depth
		stack.append({'node':node.left, 'depth':depth + 1})
		stack.append({'node':node.right, 'depth':depth + 1})
	return result


#Product sum
def isSum(arr, mult = 1):
	result = 0
	for x in arr:
		if type(x) == list:
			result += isSum(x, mult + 1)
		else:
			result += x
	return result * mult
					




























