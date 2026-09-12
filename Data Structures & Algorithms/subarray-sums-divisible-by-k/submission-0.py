class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n, res = len(nums),0
        for i in range(n):
            curr_sum = 0
            for j in range(i,n):
                curr_sum+= nums[j]
                if curr_sum % k == 0:
                    res +=1
        return res