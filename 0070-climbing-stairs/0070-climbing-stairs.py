class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        arr = [0] * (n + 1)
        arr[0] = 1

        for i in range(n):
            if i + 1 <= n:
                arr[i + 1] += arr[i]
            if i + 2 <= n:
                arr[i + 2] += arr[i]
        
        return arr[-1]