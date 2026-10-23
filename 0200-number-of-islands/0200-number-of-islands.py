class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ds = [(1,0), (-1,0), (0,1), (0,-1)]

        y, x = len(grid), len(grid[0])

        result = 0

        for a in range(y):
            for b in range(x):
                if grid[a][b] == "1":
                    result += 1
                    qu = [(a, b)]
                    while qu:
                        p, q = qu.pop()
                        if p < 0 or q < 0 or p >= y or q >= x or grid[p][q] != "1":
                            continue
                        grid[p][q] = "#"
                        for dy, dx in ds:
                            qu.append((p + dy, q + dx))
        
        return result