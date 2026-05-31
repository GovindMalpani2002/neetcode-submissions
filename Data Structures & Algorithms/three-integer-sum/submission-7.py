class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i, a in enumerate(nums):
            if i >0 and a == nums[i -1]:
                continue
            l, r = i +1, len(nums) -1
            while l <r:
                if nums[l] + nums[r] + a > 0:
                    r-=1
                elif nums[l] + nums[r] + a < 0:
                    l+=1
                else:
                    triplet = tuple(sorted([a,nums[l],nums[r]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
        return res
    

