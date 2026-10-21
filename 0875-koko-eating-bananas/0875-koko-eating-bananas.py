class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r
        while l <= r:
            m = (l + r) // 2
            n = 0
            for pile in piles:
                if n > h:
                    break
                n += math.ceil(pile / m)
            if n <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
            
        
        return res

            
