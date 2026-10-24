class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        arr = [0] * (len(cost) + 1)
        arr[1] 

        for i in range(2, len(arr)):
            arr[i] = min(cost[i - 2] + arr[i - 2], cost[i - 1] + arr[i - 1])
        return arr[-1]