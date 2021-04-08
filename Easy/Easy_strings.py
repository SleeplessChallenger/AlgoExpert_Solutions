# 1 Palindrome check
def isPalindrome(string):
	if len(string) == 1:
		return True
	elif len(string) == 2:
		return string[0] == string[1]
	elif string[0] == string[-1]:
		return isPalindrome(string[1:-1])
	return False

# 2 Caesar cipher encryptor
# a
def caesarCipherEncryptor(string, key):
	key = key % 26
	arr = []
	for x in string:
		word = ord(x) + key
		if word <= 122:
			arr.append(chr(word))
		elif word > 122:
			arr.append(chr(96 + word % 122))
	return ''.join(arr)

# b
def caesarCipherEncryptor(string, key):
	alph = list('abcdefghijklmnopqrstuvwxyz')
	key = key % 26
	arr = []
	for x in string:
		word = alph.index(x) + key
		arr.append(alph[word % 26])
	return ''.join(arr)

# 3 Run-Length encoding
# mine
def runLengthEncoding(string):
	cont = []
	temp = string[0]
	counter = 1
	for x in range(1, len(string)):
		if temp != string[x]:
			cont.append(str(counter))
			cont.append(temp)
			counter = 0
			temp = string[x]
		if counter == 9:
			cont.append(str(counter))
			cont.append(temp)
			counter = 0
		counter += 1
	if counter:
		cont.append(str(counter))
		cont.append(string[-1])
	return ''.join(cont)

# not mine
def runLengthEncoding(string):
	result = []
	counter = 1
	for x in range(1, len(string)):
		curr = string[x]
		prev = string[x - 1]

		if curr != prev or counter == 9:
			result.append(str(counter))
			result.append(prev)
			counter = 0
		counter += 1

	result.append(str(counter))
	result.append(string[len(string) - 1])
	return ''.join(result)

# 4 Generate document
# mine
def generateDocument(characters, document):
	ht = {}

	for x in characters:
		if x in ht:
			ht[x] += 1
		else:
			ht[x] = 1

	for y in document:
		if y not in ht or ht[y] == 0:
			return False
		else:
			ht[y] -= 1
	return True

# not mine
def generateDocument(characters, document):
	for char in document:
		num1 = fucn(char, document)
		num2 = fucn(char, characters)

		if num1 > num2:
			return False
	return True

def fucn(target, st):
	count = 0
	for x in st:
		if x == target:
			count += 1
	return count

# 5 First Non-Repeating Character
# mine
def firstNonRepeatingCharacter(string):
	ht = {}

	for x in string:
		if x not in ht:
			ht[x] = 0
		ht[x] += 1

	for x, y in ht.items():
		if y == 1:
			return string.index(x)

	return -1

# not mine
def firstNonRepeatingCharacter(string):
	ht = {}

	for x in string:
		if x not in ht:
			ht[x] = 0
		ht[x] += 1

	for idx in range(len(string)):
		letter = string[idx]
		if ht[letter] == 1:
			return idx

	return -1
