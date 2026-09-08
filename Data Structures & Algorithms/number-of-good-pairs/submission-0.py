class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        pair_count = 0
        for num in nums:
            if num in count:
                pair_count+= count[num]
                count[num] += 1
                
            else:
                count[num] = 1
        return pair_count

                