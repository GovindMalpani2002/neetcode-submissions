class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)- 1
        while l< r:
            max_area =max((r - l)* min(heights[r], heights[l]), max_area)
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return max_area
