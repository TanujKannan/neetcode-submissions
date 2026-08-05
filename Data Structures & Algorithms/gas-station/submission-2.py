class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start_index = 0

        total_used = 0

        for i in range(len(gas)):
            total_used += gas[i] - cost[i]

            if total_used < 0:
                start_index = i+1
                total_used = 0
        
        return start_index
        