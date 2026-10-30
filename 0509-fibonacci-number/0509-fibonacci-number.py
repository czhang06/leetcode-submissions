class Solution:
    def fib(self, n: int) -> int:
        mem = [0] * (n + 1)
        
        if n < 2:
            return n
        if n == 2:
            return 1
        mem[0], mem[1], mem[2] = 0, 1, 1
        def fib(n):
            if not mem[n-1]:
                mem[n-1] = fib(n-1)
            if not mem[n-2]:
                mem[n-2] = fib(n-2)
            return mem[n-2] + mem[n-1]
        return fib(n)