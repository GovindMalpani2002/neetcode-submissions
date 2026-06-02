class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i < n:
            if nums[i] == val:
                n-=1
                swap(i,n)
                #nums[i] = nums[n]
            else:
                i+=1
        return n

          
        