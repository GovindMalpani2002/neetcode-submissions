class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 1,len(nums)
        while l <= r:
            mid = l + (r-l)//2
            count = sum(1 for num in nums if num >=mid)
            if count == mid:
                return mid
            elif count < mid:
                r = mid - 1
            else:
                l = mid + 1
        return -1