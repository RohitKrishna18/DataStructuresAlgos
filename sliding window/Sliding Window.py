# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:37:40 2024

@author: rohit
"""

class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        start = 0
        if len(prices)<2:
            return 0
        end = 1
        while((end < len(prices))):
            profit = prices[end] - prices[start]
            if profit < 0:
                start = end
            else:
                max_profit = max(max_profit, profit)
            end += 1
        return max_profit


class Solution2(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_so_far = prices[0]
        for price in prices[1:]:
            min_so_far = min(min_so_far, price)
            profit = price - min_so_far
            max_profit = max(profit, max_profit)
        return max_profit
    
    
prices = [7, 1 ,2, 6, 5]
sol1 = Solution1()
print(sol1.maxProfit(prices))
sol2 = Solution2()
print(sol2.maxProfit(prices))
