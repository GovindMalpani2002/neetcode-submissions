class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_freq = 0
        for num in nums:
            count[num] = 1 + count.get(num,0)
        ans = 0
        for num, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                ans = num
            return ans
           
        