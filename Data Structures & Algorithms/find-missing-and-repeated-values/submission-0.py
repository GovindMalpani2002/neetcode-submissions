class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        a,b = 0,0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    a = grid[i][j]
                seen.add(grid[i][j])
        for i in range(1,n**2 +1):
            if i not in seen:
                b = i
        return [a,b]