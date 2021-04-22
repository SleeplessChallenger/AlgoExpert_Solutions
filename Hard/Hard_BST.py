# 1 Same BSTs
def sameBsts(arrayOne, arrayTwo):
	if len(arrayOne) != len(arrayTwo):
		return False
	
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False

	sm1, sm2, big1, big2 = getValue(arrayOne, arrayTwo)
	
	return sameBsts(sm1, sm2) and sameBsts(big1, big2)

def getValue(arr1, arr2):
	smaller1 = []
	smaller2 = []
	bigger1 = []
	bigger2 = []
	
	for value in range(1, len(arr1)):
		if arr1[value] >= arr1[0]:
			bigger1.append(arr1[value])
		elif arr1[value] < arr1[0]:
			smaller1.append(arr1[value])
	
	for value in range(1, len(arr2)):
		if arr2[value] >= arr2[0]:
			bigger2.append(arr2[value])
		elif arr2[value] < arr2[0]:
			smaller2.append(arr2[value])
	
	return smaller1, smaller2, bigger1, bigger2
