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

# 4 Reverse words in string
# a
def reverseWordsInString(string):
	temp = []
	idx = 0
	for x in range(len(string)):
		if string[x] == ' ':
		# if we have 2 spaces: the first
		# one will be added by first loop
		# the second one will be added 
		# on the next iteration by the 
		# second loop
			temp.append(string[idx:x])
			idx = x
		# on the next iteratoion 
		# after the space was found
		# we check whether 'string' itself
		# on the (x - 1) has space (and it 
		# does have) => we append our list
		# with the ' '
		# if it doesn't have space => skip
		elif string[idx] == ' ':
			temp.append(' ')
			idx = x

	temp.append(string[idx:])

	i, j = 0, len(temp) - 1
	while i < j:
		temp[i], temp[j] = temp[j], temp[i]
		i += 1
		j -= 1

	return ''.join(temp)

# b
def reverseWordsInString(string):
	arr = [x for x in string]
	swap(arr, 0, len(arr) - 1)

	start = 0
	while start < len(string):
		end = start
		while end < len(string) and arr[end] != ' ':
			end += 1

		swap(arr, start, end - 1)
		# (above) to bypass whitespace
		start = end + 1
		# (above) to bypass whitespace
	return ''.join(arr)

def swap(arr, st, end):
	while st < end:
		arr[st], arr[end] = arr[end], arr[st]
		st += 1
		end -= 1

# 5 Minimum Characters for words
# mine
def minimumCharactersForWords(words):
    ht = {}
	
	for word in words:
		new = {}
		for let in word:
			if let not in new:
				new[let] = 0
			new[let] += 1
		
		for x, y in new.items():
			if x not in ht:
				ht[x] = y
			else:
				ht[x] = max(ht[x], y)
	
	result = []
	
	# below you can opt between 2 ways
	
	# a
	for x in ht:
		while ht[x] != 0:
			result.append(x)
			ht[x] -= 1
	
	# b
	for x in ht:
		freq = ht[x]
		
		for _ in range(freq):
			result.append(x)
	
	return result
