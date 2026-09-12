class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        threshold = len(nums) // 3
        res = []
        for key,values in count.items():
            if values > threshold:
                res.append(key)
        return res