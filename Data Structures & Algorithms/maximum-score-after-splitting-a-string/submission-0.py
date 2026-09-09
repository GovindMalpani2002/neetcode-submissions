class Solution:
    def maxScore(self, s: str) -> int:
        count_zero, count_one = 0 ,s.count('1')
        max_count = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                count_zero +=1
            else:
                count_one-=1
            max_count = max(max_count,count_zero + count_one)
        return max_count
            