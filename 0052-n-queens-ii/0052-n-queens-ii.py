class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = [0]

        def backtrack(cols, diag1, diag2, x):
            if x == n:
                result[0] += 1
                return

            i = x

            for m in range(n):
                if not cols[m]:
                    d1 = i - m + n - 1
                    d2 = i + m

                    if not diag1[d1] and not diag2[d2]:
                        cols[m] = True
                        diag1[d1] = True
                        diag2[d2] = True

                        backtrack(cols, diag1, diag2, x + 1)

                        cols[m] = False
                        diag1[d1] = False
                        diag2[d2] = False

        backtrack([False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1), 0)

        return result[0]