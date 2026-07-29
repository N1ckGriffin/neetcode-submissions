class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [0] * len(cost)
        steps[0], steps[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            steps[i] = cost[i] + min(steps[i-2], steps[i-1])
        
        return min(steps[-1], steps[-2])