class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            next_greater = -1
            for i in range(len(nums2)-1,-1,-1):
                if nums2[i] > num:
                    next_greater = nums2[i]
                elif nums2[i] == num:
                    res.append(next_greater)
        return res
                    
