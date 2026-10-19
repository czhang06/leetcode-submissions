class Solution(object):
    def coinChange(self, coins, amount):
        counts = [float('inf')] * (amount + 1)
        counts[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    counts[i] = min(counts[i], counts[i - c] + 1)

        return counts[amount] if counts[amount] != float('inf') else -1