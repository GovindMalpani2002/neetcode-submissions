class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        # Hash map to store: {prefix_sum : how_many_times_it_appeared}
        # Base case: A prefix sum of 0 has appeared 1 time (before adding any elements)
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists in our history, it means a valid subarray exists!
            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
                
            # Record the current prefix sum in our history map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count