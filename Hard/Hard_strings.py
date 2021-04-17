# 1 Longest Substring Without Duplication
def longestSubstringWithoutDuplication(string):
	ht = {}
	longest = [0, 1]
	start = 0

	for idx in range(len(string)):
		letter = string[idx]

		if letter in ht:
			start = max(start, ht[letter] + 1)
			# max() from 'start' which will
			# depict idx that we've started
			# current substring from and
			# letter's idx that is already in ht + 1
		if longest[1] - longest[0] < idx - start + 1:
			longest = [start, idx + 1]
		ht[letter] = idx

	return string[longest[0]:longest[1]]
