def max_profit(prices):
	l,r = 0,1
	maxProfit = 0
	while r < len(prices):
		if prices[l] < prices[r]:
			profit = prices[r]-prices[l]
			maxProfit = max(maxProfit, profit)
		else:
			l = r
		r += 1
	return maxProfit

if __name__ == "__main__":
	prices = [7,1,3,1,12,1,16,1,14]
	print(max_profit(prices))
