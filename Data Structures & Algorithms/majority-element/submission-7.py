class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_value = 0
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for key,val in count.items():
            if max_value < val:
                res = key
                max_value = max(val,max_value)
        return res
