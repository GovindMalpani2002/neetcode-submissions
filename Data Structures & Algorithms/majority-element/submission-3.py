class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res, max_count = 0, 0
        for num in nums:
            count[num]  +=  1
            if count[num] > max_count:
                res = num
                max_count = count[num]
        return res
        
