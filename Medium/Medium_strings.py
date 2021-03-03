# 1 Longest palindromic substring
def longestPalindromicSubstring(string):
	longest = [0, 1]
	for x in range(1, len(string)):
		odd = func(string, x-1, x+1)
		even = func(string, x-1, x)
		long = max(odd, even, key=lambda x: x[1]-x[0])
		longest = max(long, longest, key=lambda x: x[1]-x[0])
	return string[longest[0]:longest[1]]

def func(string, i, j):
	while i >= 0 and j < len(string):
		if string[i] != string[j]:
			break
		i -= 1
		j += 1
	return [i+1, j]
# i is one index away from what we need
# 4,7; 3,8; 2,9 -> break

# 2 Group anagrams
def groupAnagrams(words):
	result = {}
	for x in words:
		key = ''.join(sorted(x))
		if key not in result:
			result[key] = []
		result[key].append(x)
	return list(result.values())

# 3 Valid IP Addresses
def validIPAddress(string):
	result = []
	for x in range(1, len(string)):
		temp = ['', '', '', '']
		temp[0] = string[:x]
		if not func(temp[0]):
			continue
		for y in range(x+1, x + min(len(string) - x, 4)):
			temp[1] = string[x:y]
			if not func(temp[1]):
				continue
			for z in range(y+1, y + min(len(string) - y, 4)):
				temp[2] = string[y:z]
				temp[3] = string[z:]
				if func(temp[2]) and func(temp[3]):
					result.append('.'.join(temp))
	return result

def func(arr):
	int_arr = int(arr)
	if int_arr > 255:
		return False
	return len(str(int_arr)) == len(arr)
