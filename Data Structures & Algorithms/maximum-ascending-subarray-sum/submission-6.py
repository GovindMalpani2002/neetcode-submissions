class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum, max_sum = nums[0],0
        increasing = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                if increasing >0:
                    curr_sum+=nums[i]
                else:
                    increasing = 1
                    curr_sum = nums[i] + nums[i-1]
            else:
                increasing = 0
            max_sum = max(curr_sum,max_sum)
        return max_sum
