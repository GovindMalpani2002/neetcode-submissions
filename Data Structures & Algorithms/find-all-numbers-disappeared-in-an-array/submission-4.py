class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mark = [False]*(len(nums)+1)
        res = []
        for num in nums:
            mark[num] = True
        for i in range(1,len(nums)+1):
            if mark[i] == False:
                res.append(i)
        return res
