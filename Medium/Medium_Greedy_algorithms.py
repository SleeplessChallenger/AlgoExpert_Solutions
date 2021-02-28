# 1 Task assignment
def taskAssignment(k, tasks):
	sorte = sorted(tasks)
	cont = []
	hashtable = helper(tasks)

	for x in range(k):

		task1 = sorte[x] # take from beginning time duration
		idxs1 = hashtable[task1] # receive list of indicies of particular key
		idx1 = idxs1.pop()

		idx_large = (len(tasks) - 1) - x # take index of largest from the end on every loop
		task2 = sorte[idx_large]
		idxs2 = hashtable[task2]
		idx2 = idxs2.pop()

		cont.append([idx1, idx2])

	return cont

def helper(arr):
	hashtable = {}
	for x, y in enumerate(arr):
		if y not in hashtable:
			hashtable[y] = [x]
		else:
			hashtable[y] += [x]
	return hashtable