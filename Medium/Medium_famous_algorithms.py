# 1 Kadane's Algorithm
def kadanesAlgorithm(arr):
	temp = arr[0]
	total = arr[0]
	for x in range(1, len(arr)):
		temp = max(temp + arr[x], arr[x])
		total = max(temp, total)
	return total
