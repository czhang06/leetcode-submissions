class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [0]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                res[x] = i - x
            stack.append(i)
        return res
            
        