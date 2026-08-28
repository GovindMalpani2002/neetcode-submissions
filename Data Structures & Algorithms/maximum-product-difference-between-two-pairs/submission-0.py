class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        fir_max = sec_max = float('-inf')
        fir_min = sec_min = float('inf')
        for num in nums:
            if num > fir_max:
                sec_max = fir_max
                fir_max = num
            elif num > sec_max:
                sec_max = num
            if num < fir_min:
                sec_min = fir_min
                fir_min = num
            elif num < sec_min:
                sec_min = num
        return fir_max*sec_max - fir_min*sec_min
            
        
