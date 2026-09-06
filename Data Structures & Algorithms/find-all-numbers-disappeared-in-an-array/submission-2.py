class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num_map = [i for i in range(len(nums)+1)]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            if num_map[i] not in nums:
                res.append(num_map[i])
        return res
