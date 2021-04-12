# 1 Subarray sort
def subarraySort(arr):
	left = float('inf')
	right = float('-inf')

	for idx in range(len(arr)):
		if helper(idx, arr[idx], arr):
			left = min(left, arr[idx])
			right = max(right, arr[idx])

	if left == float('inf'):
		return [-1, -1]

	idxLeft = 0
	while arr[idxLeft] <= left:
		idxLeft += 1

	idxRight = len(arr) - 1
	while arr[idxRight] >= right:
		idxRight -= 1

	return [idxLeft, idxRight]

def helper(idx, figure, arr):
	if idx == 0:
		return arr[idx + 1] < figure
	elif idx == len(arr) - 1:
		return arr[idx - 1] > figure
	return arr[idx - 1] > figure or arr[idx + 1] < figure
