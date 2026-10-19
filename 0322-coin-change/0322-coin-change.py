class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        counts = [float('inf')] * (amount + 1)
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        for c in coins:
            if c <= amount:
                counts[c] = 1
        
        for i in range(1, len(counts)):
            if counts[i] == float('inf'):
                continue
            for c in coins:
                if i + c > amount:
                    continue
                counts[i + c] = min(counts[i + c], counts[i] + 1)
            
        if counts[amount] == float('inf'):
            return -1
        else:
            return counts[amount]
