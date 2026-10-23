class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        y, x = len(heights), len(heights[0])
        pacific = [[0] * x for i in range(y)]
        atlantic = [[0] * x for i in range(y)]

        result = []

        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        pq = []
        aq = []
        for i in range(y):
            pq.append((i, 0))
            aq.append((i, x - 1))
            pacific[i][0] = 1
            atlantic[i][x - 1] = 1
        for i in range(x):
            pq.append((0, i))
            aq.append((y - 1, i))
            pacific[0][i] = 1
            atlantic[y - 1][i] = 1

        while pq:
            a, b = pq.pop()
            for dy, dx in ds:
                ny, nx = a + dy, b + dx
                if 0 <= ny < y and 0 <= nx < x and not pacific[ny][nx] and heights[ny][nx] >= heights[a][b]:
                    pq.append((ny, nx))
                    pacific[ny][nx] = 1
        
        while aq:
            a, b = aq.pop()
            for dy, dx in ds:
                ny, nx = a + dy, b + dx
                if 0 <= ny < y and 0 <= nx < x and not atlantic[ny][nx] and heights[ny][nx] >= heights[a][b]:
                    aq.append((ny, nx))
                    atlantic[ny][nx] = 1

        for a in range(y):
            for b in range(x):
                if pacific[a][b] and atlantic[a][b]:
                    result.append([a, b])
        return result