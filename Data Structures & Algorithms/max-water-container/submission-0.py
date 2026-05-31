class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for r in range(len(heights) -1,-1,-1):
            for l in range(len(heights)):
                max_area = max(min(heights[r],heights[l])* (r - l), max_area)
        return max_area
