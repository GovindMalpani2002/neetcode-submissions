class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            presum,postsum = 0,0
            for j in range(i):
                presum+=nums[j]
            for k in range(i+1,n):
                postsum+=nums[k]
            if presum == postsum:
                return i
        return -1


