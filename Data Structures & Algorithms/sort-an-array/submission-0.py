class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
            else:
                continue
        return nums