import math
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        dist_mat = []
        for i in range(m):
            temp_list = []
            for j in range(n):
                temp_list.append(math.inf)
            dist_mat.append(temp_list)
        bfs_queue = deque()
        bfs_queue.append((0, 0))
        dist_mat[0][0] = 1

        while bfs_queue:
            i, j = bfs_queue.popleft()
            if i - 1 >= 0 and grid[i-1][j] == 0:
                if dist_mat[i-1][j] == math.inf:
                    bfs_queue.append((i - 1, j))
                dist_mat[i-1][j] = min(dist_mat[i-1][j], dist_mat[i][j]+1)
            if i - 1 >= 0 and j - 1 >= 0 and grid[i-1][j-1] == 0:
                if dist_mat[i - 1][j - 1] == math.inf:
                    bfs_queue.append((i - 1, j - 1))
                dist_mat[i - 1][j - 1] = min(dist_mat[i - 1][j - 1], dist_mat[i][j] + 1)
            if i - 1 >= 0 and j + 1 < n and grid[i-1][j+1] == 0:
                if dist_mat[i - 1][j + 1] == math.inf:
                    bfs_queue.append((i - 1, j + 1))
                dist_mat[i - 1][j + 1] = min(dist_mat[i - 1][j + 1], dist_mat[i][j] + 1)
            if i + 1 < m and grid[i+1][j] == 0:
                if dist_mat[i + 1][j] == math.inf:
                    bfs_queue.append((i + 1, j))
                dist_mat[i + 1][j] = min(dist_mat[i + 1][j], dist_mat[i][j] + 1)
            if j - 1 >= 0 and grid[i][j-1] == 0:
                if dist_mat[i][j - 1] == math.inf:
                    bfs_queue.append((i, j - 1))
                dist_mat[i][j - 1] = min(dist_mat[i][j - 1], dist_mat[i][j] + 1)
            if j + 1 < n and grid[i][j+1] == 0:
                if dist_mat[i][j + 1] == math.inf:
                    bfs_queue.append((i, j + 1))
                dist_mat[i][j + 1] = min(dist_mat[i][j + 1], dist_mat[i][j] + 1)
            if j - 1 >= 0 and i + 1 < m and grid[i+1][j-1] == 0:
                if dist_mat[i + 1][j - 1] == math.inf:
                    bfs_queue.append((i + 1, j - 1))
                dist_mat[i + 1][j - 1] = min(dist_mat[i + 1][j - 1], dist_mat[i][j] + 1)
            if i + 1 < m and j + 1 < n and grid[i+1][j+1] == 0:
                if dist_mat[i + 1][j + 1] == math.inf:
                    bfs_queue.append((i + 1, j + 1))
                dist_mat[i + 1][j + 1] = min(dist_mat[i + 1][j + 1], dist_mat[i][j] + 1)

        return dist_mat[m-1][n-1] if dist_mat[m-1][n-1] != math.inf else -1


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    print(Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
