class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i == len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                # option 1: buy the stock
                buy = dfs(i + 1, False) - prices[i]
                # option 2: skip
                skip = dfs(i + 1, True)

                dp[(i, buying)] = max(buy, skip)
            else:
                #option 1: sell
                sell = dfs(i + 1, True) + prices[i]
                #option 2: hold
                hold = dfs(i + 1, False)

                dp[(i, buying)] = max(sell, hold)

            return dp[(i, buying )]
        
        return dfs(0, True)
            