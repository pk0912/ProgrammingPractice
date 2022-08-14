from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if len(grid[0]) != n:
            return -1
        zero_count = 0
        one_count = 0
        bfs_queue = deque()
        visited_nodes = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    zero_count += 1
                if grid[i][j] == 1:
                    one_count += 1
                    bfs_queue.append(((i, j), 0))
                    visited_nodes.add((i, j))
        if zero_count == 0 or one_count == 0:
            return -1
        max_dist = 0
        while bfs_queue:
            tmp_len = len(bfs_queue)
            for _ in range(tmp_len):
                (i, j), k = bfs_queue.popleft()
                if j - 1 >= 0 and (i, j - 1) not in visited_nodes:
                    bfs_queue.append(((i, j - 1), k + 1))
                    visited_nodes.add((i, j - 1))
                    max_dist = max(max_dist, k + 1)
                if j + 1 < n and (i, j + 1) not in visited_nodes:
                    bfs_queue.append(((i, j + 1), k + 1))
                    visited_nodes.add((i, j + 1))
                    max_dist = max(max_dist, k + 1)
                if i - 1 >= 0 and (i - 1, j) not in visited_nodes:
                    bfs_queue.append(((i - 1, j), k + 1))
                    visited_nodes.add((i - 1, j))
                    max_dist = max(max_dist, k + 1)
                if i + 1 < n and (i + 1, j) not in visited_nodes:
                    bfs_queue.append(((i + 1, j), k + 1))
                    visited_nodes.add((i + 1, j))
                    max_dist = max(max_dist, k + 1)

        return max_dist


if __name__ == '__main__':
    print(Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
    print(Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
