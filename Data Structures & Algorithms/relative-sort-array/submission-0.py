class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        additional = []
        for num in arr2:
            for i in range(len(arr1)):
                if num == arr1[i]:
                    res.append(num)
        for a in arr1:
            if a not in arr2:
                additional.append(a)
        additional.sort()

        
                    
        return res + additional
