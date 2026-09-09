class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        map = {}
        a,b = 0,0
        for num in nums:
            map[num] = 1 + map.get(num,0)
        for i in range(1,len(nums)+1):
            if i not in map:
                b = i
            elif map[i] == 2:
                a = i
        return [a,b]