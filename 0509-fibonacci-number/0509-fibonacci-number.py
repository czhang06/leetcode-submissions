class Solution:
    def fib(self, n: int) -> int:
        
        @cache
        def fib(n):
            if n < 2:
                return n
            return fib(n-1) + fib(n-2)
        return fib(n)