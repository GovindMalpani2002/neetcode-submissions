class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) -1
                while l < r:
                    foursum = nums[i] + nums[j] + nums[l] + nums[r]
                    if foursum > target:
                        r-=1
                    elif foursum < target:
                        l+=1
                    else:
                        fourpair = tuple(sorted([nums[i],nums[j],nums[l],nums[r]]))
                        if fourpair not in seen:
                            seen.add(fourpair)
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        r-=1
                        l+=1
        return res

            