# 1 Two number sum
def twoNumberSum(arr, target):
	# here for simplicity use inbuilt sort()
	arr.sort()
	left = 0
	right = len(arr) - 1
	while left < right:
		middle = arr[left] + arr[right]
		if middle == target:
			return [arr[left], arr[right]]
		elif target > middle:
			left += 1
		else:
			right -= 1
	return []

# 2 Valid subsequence
def isValidSubsequence(arr, seq):
    i = 0
	j = 0
	while i < len(arr):
		if arr[i] == seq[j]:
			j += 1
		if j == len(seq):
			return True
		i += 1
	return False

# 3 Non-constructible change
def nonConstructibleChange(coins):
    #for simplicity use inbuilt sort()
	coins.sort()
	temp = 0
	for x in coins:
		if x <= temp + 1:
			temp += x
		elif x > temp + 1:
			break
	return temp + 1

# 4 Tournament winner
# mine
def tournamentWinner(competitions, results):
	hashtable = dict()
	for x in competitions:
		hashtable[x[0]] = 0
	for x in competitions:
		hashtable[x[1]] = 0
	for y in range(len(results)):
		if results[y] == 1:
			hashtable[competitions[y][0]] += 1
		elif results[y] == 0:
			hashtable[competitions[y][1]] += 1
	return max(hashtable, key=hashtable.get)

# not mine
const = 1
def tournamentWinner(competitions, results):
	curr = ''
	hash_ = {curr: 0}
	for x, y in enumerate(competitions):
	# or tweak for range(len(competitions))
		result = results[x]
		home, away = y
		winning = home if result == const else away
		helper(3, winning, hash_)
		if hash_[curr] < hash_[winning]:
			curr = winning
	return curr

		
def helper(score, team, arr):
	if team not in arr:
		arr[team] = 0
	arr[team] += score

# 5 Sorted Squared Array
# mine
def sortedSquaredArray(arr):
	for x in range(len(arr)):
		arr[x] = arr[x] * arr[x]
	arr.sort() # for simplicity
	return arr

# not mine
def sortedSquaredArray(arr):
	new_arr = [x for x in range(len(arr))]
	small = 0
	large = len(arr) - 1

	for x in reversed(range(len(arr))):
		small_val = arr[small]
		large_val = arr[large]

		if abs(small_val) > abs(large_val):
			new_arr[x] = small_val * small_val
			small += 1
		else:
			new_arr[x] = large_val * large_val
			large -= 1

	return new_arr
