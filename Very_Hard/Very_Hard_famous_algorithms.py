# 1 Knuth-Morris-Pratt Algorithm
def knuthMorrisPrattAlgorithm(string, substring):
	pattern = buildPattern(string, substring)
	return findResult(string, substring, pattern)

def buildPattern(string, substring):
	i = 1
	j = 0
	arr = [-1 for _ in range(len(substring))]
	
	while i < len(substring):
		if substring[i] == substring[j]:
			arr[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = arr[j - 1] + 1
			# if there is pattern -> take it & + 1
			# elif no: -1 + 1
		else:
			i += 1
	return arr

def findResult(string, sub, pat):
	i = 0
	j = 0
	
	while i + len(sub) - j <= len(string):	
		# if j == len(sub):
			# return True
		if string[i] == sub[j]:
			if j == len(sub) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pat[j - 1] + 1
		else:
			i += 1
	return False
