class Solution:
    def check(self,nums: List[int]) -> bool:
        count_drops = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                count_drops +=1
        return count_drops <=1