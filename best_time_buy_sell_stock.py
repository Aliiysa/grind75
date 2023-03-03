def maxProfit(prices):
    maxProf = 0

    low, high = 0, 1

    while high < len(prices):
        if prices[low] < prices[high]:
            profit = prices[high] - prices[low]
            maxProf = max(profit, maxProf)


        else: 
            low = high
        high += 1

    return maxProf

print(maxProfit([7, 1, 5, 3, 6, 4]))
