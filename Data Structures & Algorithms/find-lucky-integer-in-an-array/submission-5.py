class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = [0]*(max(arr)+1)
        for i in range(len(arr)):
            mp[arr[i]] +=1
        for i in range(len(mp)-1,0,-1):
            if mp[i] == i:
                return i
        return -1


        