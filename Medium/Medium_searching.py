# 1 Search in Sorted Matrix
# mine
def searchInSortedMatrix(matrix, target):
	i = 0
	while i < len(matrix):
		temp = helper(matrix[i], target)
		if temp != -1:
			return [i, temp]
		i += 1
	return [-1, -1]

def helper(arr, target):
	for x in range(len(arr)):
		if arr[x] == target:
			return x
	return -1

# not mine
def searchInSortedMatrix(matrix, target):
	row = 0
	col = len(matrix[0]) - 1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
		else:
			return [row, col]
	return [-1, -1]
