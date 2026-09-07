class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for num in arr:
            count = 0
            for a in arr:
                if num == a:
                    count+=1
            if num == count:
                res = num
        return res



        