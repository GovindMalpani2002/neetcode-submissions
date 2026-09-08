class Solution:
    def check(self,nums: List[int]) -> bool:
        count_drops = 1
        for i in range(2*len(nums)-1):
            if nums[i % len(nums)] <= nums[(i+1) % len(nums)]:
                count_drops +=1
            else:
                count_drops = 1
            if count_drops == len(nums):
                return True
        return len(nums) == 1
