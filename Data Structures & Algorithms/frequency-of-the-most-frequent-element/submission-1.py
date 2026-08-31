class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,total,res = 0,0,0
        for r in range(l,len(nums)):
            total+=nums[r]
            
            if nums[r]*(r - l + 1) > total + k:
                total -=nums[l]
                l+=1
            res = max(res,r-l+1)
        return res
            