class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        result = 0

        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        y, x = len(grid), len(grid[0])

        for a in range(y):
            for b in range(x):
                if grid[a][b] == 1:
                    q = [(a, b)]
                    grid[a][b] = "#"
                    size = 0
                    while q:
                        m, n = q.pop()
                        size += 1
                        for dy, dx in ds:
                            ny, nx = m + dy, n + dx
                            if not (ny < 0 or nx < 0 or ny >= y or nx >= x or grid[ny][nx] != 1):
                                grid[ny][nx] = "#"
                                q.append((ny, nx))
                    
                    result = max(result, size)
        return result
