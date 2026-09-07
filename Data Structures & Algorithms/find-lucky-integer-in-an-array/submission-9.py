class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        arr.sort()
        count = 1
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1] == arr[i]:
                count+=1
            else:
                if arr[i+1] == count:
                    return count 
                count = 1
        if arr[0] == count:
                return count
        return -1



        