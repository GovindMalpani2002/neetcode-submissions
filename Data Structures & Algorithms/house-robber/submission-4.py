class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = nums[0], max(rob1, nums[1])
        for i in range(1,len(nums)):
            temp = rob2
            rob2 = max(rob1, rob1 + nums[i])
            rob1 = rob2
        return rob2
        


