class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]*(n+1)
        postsum = [0]*(n+1)
        for i in range(1,n+1):
            presum[i] = presum[i-1] + nums[i-1]
        for j in range(n-2,-1,-1):
            postsum[j] = postsum[j+1] + nums[j+1]
        for k in range(n):
            if presum[k] == postsum[k]:
                return k
        return -1
