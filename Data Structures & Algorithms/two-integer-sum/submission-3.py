class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            indices[num] = i
            comp = target - nums[i]
            if comp in indices and indices[comp]!= i:
                return[min(i,indices[comp]), max(i,indices[comp])]
        return [] 

