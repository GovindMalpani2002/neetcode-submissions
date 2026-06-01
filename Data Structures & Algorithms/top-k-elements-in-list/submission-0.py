class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        tmp = []
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for num, cnt in count.items():
            tmp.append([cnt,num])
        tmp.sort()

        res = []
        while len(res) < k:
            res.append(tmp.pop()[1])
        return res
            


            
