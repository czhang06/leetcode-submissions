class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        y, x = len(grid), len(grid[0])
        q = deque()
        ds = [(1,0),(-1,0),(0,1),(0,-1)]

        fresh = 0
        for a in range(y):
            for b in range(x):  
                if grid[a][b] == 1:
                    fresh += 1
                if grid[a][b] == 2:
                    q.append((a, b))
        
        minutes = 0
        while q and fresh > 0:
            minutes += 1
            for i in range(len(q)):
                cy, cx = q.popleft()
                for dy, dx in ds:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < y and 0 <= nx < x and grid[ny][nx] == 1:
                        fresh -= 1
                        grid[ny][nx] = 2
                        q.append((ny, nx))
        
        return minutes if fresh == 0 else -1
        
