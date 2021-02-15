# 1 Nth fibonacci
# a
def fib(n):
	if n <= 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

# b
def fib(n, memo={1:0, 2:1}):
	if n in memo:
		return memo[n]
	memo[n] = fib(n-1, memo) + fib(n-2, memo)
	return memo[n]

# c 
def fib(n):
	temp = [0,1]
	i = 3
	while i <= n:
		sum_ = temp[0] + temp[1]
		temp[0] = temp[1]
		temp[1] = sum_
		i += 1
	return temp[1] if n > 1 else temp[0]

# 2 Product sum
def productSum(arr, mult=1):
	temp = 0
	for x in arr:
		if type(x) == list:
			temp += productSum(x, mult+1)
		else:
			temp += x
	return temp * mult
