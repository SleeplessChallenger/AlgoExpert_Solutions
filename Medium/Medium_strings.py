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