class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            map[num] = 1+ map.get(num,0)
        for key in map:
            if map[key] % 2 == 1:
                return False
        return True