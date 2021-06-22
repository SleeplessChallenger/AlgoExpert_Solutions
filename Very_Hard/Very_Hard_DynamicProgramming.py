# 1 Max Profit With K Transactions

# first
# Time: O(n*k) Space: O(n*k)
def maxProfitWithKTransactions(prices, k):
	if len(prices) == 0:
		return 0
    profits = [[0 for _ in prices] for _ in range(k + 1)]
	
	for transaction in range(1, k + 1):
		maxFigure = float('-inf')
		for price in range(1, len(prices)):
			# to bypass n^2 time we keep only
			# biggest amount of previous price
			# when going through one 'transaction level'
			maxFigure = max(maxFigure, - prices[price - 1]
							+ profits[transaction - 1][price - 1])

			profits[transaction][price] = max(
				profits[transaction][price - 1],
				prices[price] + maxFigure)
	
	return profits[-1][-1]

# second
# Time: O(n*k) Space: O(n)
def maxProfitWithKTransactions(prices, k):
    if len(prices) == 0:
		return 0
	even = [0 for _ in prices]
	odd = [0 for _ in prices]
	
	for tr in range(1, k + 1):
		maxPr = float('-inf')
		if tr % 2 == 0:
			curr = even
			prev = odd
		else:
			curr = odd
			prev = even
		for p in range(1, len(prices)):
			maxPr = max(maxPr, - prices[p - 1] + prev[p - 1])
			curr[p] = max(curr[p - 1], prices[p] + maxPr)
	
	return even[-1] if k % 2 == 0 else odd[-1]
