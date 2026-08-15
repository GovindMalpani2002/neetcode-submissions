class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        out = []
        n = len(nums) 
        for i in range(n):
            out[i] = nums[i]
            out[i+n] = nums[i]
        return out