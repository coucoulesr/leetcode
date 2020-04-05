"""
Leetcode Problem 122: Best Time to Buy and Sell Stock II
Author: Richard Coucoules
"""  

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit = bought_at = 0
        own_stock = False
        for i in range(len(prices)):
            if i == len(prices) - 1:
                if own_stock:
                    profit += prices[i] - bought_at
                break
            if not own_stock and prices[i + 1] > prices[i]:
                own_stock = True
                bought_at = prices[i]
            if own_stock and prices[i] > bought_at:
                if prices[i + 1] > prices[i]:
                    continue
                own_stock = False
                profit += prices[i] - bought_at
        return profit

def main():
    sol = Solution()
    prices_1 = [7,1,5,3,6,4]
    prices_2 = [1,2,3,4,5]
    prices_3 = [7,6,4,3,1]
    print(sol.maxProfit(prices_1))
    print(sol.maxProfit(prices_2))
    print(sol.maxProfit(prices_3))

if __name__ == "__main__":
    main()