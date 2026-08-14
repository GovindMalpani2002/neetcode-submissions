class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]* len(arr)
        right_max = -1
        for i in range(len(arr)-1,-1,-1):
            ans[i] = right_max
            right_max = max(right_max,arr[i])
        return ans


        
