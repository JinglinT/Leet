class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        m = len(board)
        n = len(board[0])

        res = 0

        for i in range(m):
            prev = None
            for j in range(n):
                if board[i][j] == '.':
                    continue
                elif board[i][j] == 'R':
                    if prev == 'p':
                        res += 1
                elif board[i][j] == 'p':
                    if prev == 'R':
                        res += 1
                prev = board[i][j]

        for j in range(n):
            prev = None
            for i in range(m):
                if board[i][j] == '.':
                    continue
                elif board[i][j] == 'R':
                    if prev == 'p':
                        res += 1
                elif board[i][j] == 'p':
                    if prev == 'R':
                        res += 1
                prev = board[i][j]

        return res
