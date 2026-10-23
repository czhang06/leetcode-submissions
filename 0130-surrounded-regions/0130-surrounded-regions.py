class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        y, x = len(board), len(board[0])
        ds = [(1,0), (-1,0), (0,1), (0, -1)]

        q = []

        for i in range(y):
            if board[i][0] == "O":
                q.append((i,0))
                board[i][0] = "#"
            if board[i][x - 1] == "O":
                q.append((i, x-1))
                board[i][x-1] = "#"


            
        for i in range(x):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "#"
            if board[y - 1][i] == "O":
                q.append((y-1, i))
                board[y-1][i] = "#"
        
        while q:
            a, b = q.pop()
            for dy, dx in ds:
                ny, nx = a + dy, b + dx
                if 0 <= ny < y and 0 <= nx < x and board[ny][nx] == "O":
                    q.append((ny, nx))
                    board[ny][nx] = "#"
        
        for a in range(y):
            for b in range(x):
                if board[a][b] == "#":
                    board[a][b] = "O"
                elif board[a][b] == "O":
                    board[a][b] = "X"
        
