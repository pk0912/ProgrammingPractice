from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        bfs_queue = deque()
        visited_nodes = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    bfs_queue.append((i, j))
                    visited_nodes.add((i, j))

        while bfs_queue:
            tmp_len = len(bfs_queue)
            for _ in range(tmp_len):
                i, j = bfs_queue.popleft()
                if j - 1 >= 0 and (i, j - 1) not in visited_nodes:
                    bfs_queue.append((i, j - 1))
                    visited_nodes.add((i, j - 1))
                    mat[i][j - 1] = mat[i][j] + 1
                if j + 1 < n and (i, j + 1) not in visited_nodes:
                    bfs_queue.append((i, j + 1))
                    visited_nodes.add((i, j + 1))
                    mat[i][j + 1] = mat[i][j] + 1
                if i - 1 >= 0 and (i - 1, j) not in visited_nodes:
                    bfs_queue.append((i - 1, j))
                    visited_nodes.add((i - 1, j))
                    mat[i - 1][j] = mat[i][j] + 1
                if i + 1 < m and (i + 1, j) not in visited_nodes:
                    bfs_queue.append((i + 1, j))
                    visited_nodes.add((i + 1, j))
                    mat[i + 1][j] = mat[i][j] + 1

        return mat


if __name__ == '__main__':
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
