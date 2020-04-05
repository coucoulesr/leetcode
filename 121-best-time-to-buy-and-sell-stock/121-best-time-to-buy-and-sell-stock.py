"""
Leetcode Problem 121: Best Time to Buy and Sell Stock
Author: Richard Coucoules
"""  

class Solution:
    def maxProfit(self, prices):
        if not len(prices):
            return 0
        max_profit = 0
        min_price_so_far = prices[0]
        for i in range(1, len(prices)):
            min_price_so_far = min(min_price_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - min_price_so_far)
        return max_profit

def main():
    sol = Solution()
    prices_1 = [7,1,5,3,6,4]
    prices_2 = [7,6,4,3,1]
    print(sol.maxProfit(prices_1))
    print(sol.maxProfit(prices_2))

if __name__ == "__main__":
    main()
