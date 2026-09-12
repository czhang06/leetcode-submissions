class Solution(object):
    def exist(self, board, word):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        height = len(board)
        width = len(board[0])

        def backtrack(y, x, i):
            if i == len(word):
                return True

            temp = board[y][x]
            board[y][x] = "#"

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if (0 <= ny < height and
                    0 <= nx < width and
                    board[ny][nx] == word[i]):

                    if backtrack(ny, nx, i + 1):
                        return True

            board[y][x] = temp
            return False

        for y in range(height):
            for x in range(width):
                if board[y][x] == word[0]:
                    if backtrack(y, x, 1):
                        return True

        return False