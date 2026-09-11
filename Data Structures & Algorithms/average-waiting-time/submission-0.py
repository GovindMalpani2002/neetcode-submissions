class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        waiting_time = 0
        for arrival,time in customers:
            total_time = max(total_time,arrival) + time
            waiting_time += total_time - arrival
        return waiting_time/ len(customers) 