class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        product = 1
        res = []
        for num in nums:
            if num != 0:
                product *= num
        for num in nums:
            if zero_count > 1:
             res.append(0)
            elif zero_count ==1:
                res.append(product if num == 0 else 0)
            else:
                res.append( product // num)
        return res