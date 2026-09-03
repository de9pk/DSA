class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])

        def dfs(row, col, k):
            if k == len(word):
                return True

            if row < 0 or row >= r or col < 0 or col >= c:
                return False

            if board[row][col] != word[k]:
                return False

            original = board[row][col]
            board[row][col] = "#"

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:
                if dfs(row + dr, col + dc, k + 1):
                    return True

            board[row][col] = original

            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False