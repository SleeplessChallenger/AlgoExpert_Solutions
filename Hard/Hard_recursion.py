# 1 Lowest Common Manager
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

class Help:
	def __init__(self, manager, num):
		self.manager = manager
		self.num = num


def getLowestCommonManager(topManager, reportOne, reportTwo):
	return helper(topManager, reportOne, reportTwo).manager

def helper(top, nodeOne, nodeTwo):
	idx = 0
	for branch in top.directReports:
		result = helper(branch, nodeOne, nodeTwo)
		if result.manager:
			return result
		if result.num > 0:
			idx += result.num

	if top == nodeOne or top == nodeTwo:
		idx += 1
	boss = top if idx == 2 else None

	return Help(boss, idx)

# 2 Interweaving Strings
# T: O(2^(n + m)) S: O(n + m)
def interweavingStrings(one, two, three):
	if len(one) + len(two) != len(three):
		return False
	
	return helper(0, 0, 0, one, two, three)

def helper(i, j, k, one, two, three):
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		if helper(i + 1, j, k + 1, one, two, three):
		# `if` for the case when response is False
		# hence we switch to the next `if`
			return True
	if j < len(two) and two[j] == three[k]:
		return helper(i, j + 1, k + 1, one, two, three)
		# here `if` is useless as we simply sift down
		# to False if a) conditions above aren't met
		# b) we came back from all recursive calls
	return False

# T: O(nm) S: O(nm)
def interweavingStrings(one, two, three):
	if len(one) + len(two) != len(three):
		return False
	
	memo = [[None for x in range(len(two) + 1)]
		   	for y in range(len(one) + 1)]
	# `+1` is because there can be cases
	# when one of the indicies > len() of str
	return helper(0, 0, 0, one, two, three, memo)

def helper(i, j, k, one, two, three, memo):
	if memo[i][j] is not None:
		return memo[i][j]
	
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		memo[i][j] = helper(i + 1, j, k + 1, one, two, three, memo)
		if memo[i][j]:
		# `if` for the case when response is False
		# hence we switch to the next `if`
			return True
	if j < len(two) and two[j] == three[k]:
		memo[i][j] = helper(i, j + 1, k + 1, one, two, three, memo)
		return memo[i][j]
		# here `if` is useless as we simply sift down
		# to False if a) conditions above aren't met
		# b) we came back from all recursive calls
	memo[i][j] = False
	return False
