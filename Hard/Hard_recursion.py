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
