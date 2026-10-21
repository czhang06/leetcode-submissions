class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        result = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][0]:
                ht, x = stack.pop()
                result = max(result, ht * (i - x))
                start = x
            stack.append((heights[i], start))
        n = len(heights)
        for ht, x in stack:
            result = max(result, ht * (n - x))
        return result
