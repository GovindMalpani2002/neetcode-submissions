class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        count = 1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] != arr[i-1] or i==0:
                if arr[i] == count:
                    return count
                else:
                     count = 0
            count+=1    
        return -1



        