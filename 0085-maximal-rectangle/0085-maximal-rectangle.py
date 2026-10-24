class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        x = len(matrix[0])

        heights = [0] * x
        best = 0


        for row in matrix:
            for c in range(x):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0
            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and h < stack[-1][1]:
                    a, b = stack.pop()
                    start = a
                    best = max(best, b * (i - a))
                stack.append((start, h))
            for a, b in stack:
                best = max(best, b * (x - a))
        return best
            