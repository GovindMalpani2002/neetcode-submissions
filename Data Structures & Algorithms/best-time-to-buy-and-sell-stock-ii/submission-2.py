class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, bought):
            if i == len(prices):
                return 0
            if (i,bought) in memo:
                return memo[(i,bought)]
            memo[(i,bought)] = dfs(i+1, bought)
            if bought:
                memo[(i,bought)] = max(memo[(i,bought)], prices[i] + dfs(i +1, False))
            else:
                memo[(i,bought)] = max(memo[(i,bought)], -prices[i] + dfs(i+1,True))
            return memo[(i,bought)]
        return dfs(0,False)


        