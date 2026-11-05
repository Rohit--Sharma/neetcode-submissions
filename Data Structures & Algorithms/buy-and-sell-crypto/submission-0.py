class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        curr_min = prices[0]
        max_profit = 0

        while i < len(prices):
            if prices[i] > curr_min:
                profit = prices[i] - curr_min
                max_profit = max(max_profit, profit)
            else:
                curr_min = prices[i]

            i += 1

        return max_profit