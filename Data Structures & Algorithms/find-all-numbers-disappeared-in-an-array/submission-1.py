class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num_map = [0]*(len(nums)+1)
        for num in nums:
            num_map[num] = num
        for i in range(1,len(nums)+1):
            if num_map[i] ==0:
                res.append(i)
        return res
