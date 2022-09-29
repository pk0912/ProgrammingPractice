from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            nonlocal board, visited_nodes
            visited_nodes.add((i, j))
            board[i][j] = -1
            if i - 1 >= 0 and board[i - 1][j] == 'O' and (i - 1, j) not in visited_nodes:
                dfs(i - 1, j)
            if j - 1 >= 0 and board[i][j - 1] == 'O' and (i, j - 1) not in visited_nodes:
                dfs(i, j - 1)
            if j + 1 < n and board[i][j + 1] == 'O' and (i, j + 1) not in visited_nodes:
                dfs(i, j + 1)
            if i + 1 < m and board[i + 1][j] == 'O' and (i + 1, j) not in visited_nodes:
                dfs(i + 1, j)

        m = len(board)
        n = len(board[0])
        visited_nodes = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if board[i][j] == 'O' and (i, j) not in visited_nodes:
                        dfs(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 'O'


if __name__ == '__main__':
    a = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
    b = [["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","O","X","X","O"],["X","O","X","O","O","X","X","O","X","O"],["X","X","O","X","X","O","X","O","O","X"],["O","O","O","O","X","O","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]]
    print(b)
    Solution().solve(b)
    print(b)
