class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_value = 0
        for num in nums:
            count[num] = 1 + count.get(num,0)
            if max_value < count[num]:
                res = num
                max_value = max(count[num],max_value)
        return res
