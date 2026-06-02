class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                tmp.append(nums[i])
                count+=1
        
        for i in range(len(nums)):
            if i < len(tmp):
                nums[i] = tmp[i]
            else:
                nums[i] = val
        return len(tmp)
        