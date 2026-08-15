class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i, brought):
            if i == len(prices):
                return 0
            res = dfs(i+1, bought)
            if bought:
                res = max(res, prices[i] + dfs(i +1, False))
            else:
                res = max(res, -prices[i] + dfs(i+1,True))
            return res
        return dfs(0,False)


        