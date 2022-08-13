from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_time_for_rotting = 0
        m = len(grid)
        n = len(grid[0])
        bfs_queue = deque()
        zero_nodes = 0
        non_zero_nodes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs_queue.append((i, j))
                    non_zero_nodes += 1
                if grid[i][j] == 0:
                    zero_nodes += 1

        while bfs_queue:
            tmp_len = len(bfs_queue)
            made_rotten = False
            for _ in range(0, tmp_len):
                i, j = bfs_queue.popleft()
                if grid[i][j] == 2:
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        bfs_queue.append((i, j - 1))
                        grid[i][j - 1] = 2
                        made_rotten = True
                        non_zero_nodes += 1
                    if j + 1 < n and grid[i][j + 1] == 1:
                        bfs_queue.append((i, j + 1))
                        grid[i][j + 1] = 2
                        made_rotten = True
                        non_zero_nodes += 1
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        bfs_queue.append((i - 1, j))
                        grid[i - 1][j] = 2
                        made_rotten = True
                        non_zero_nodes += 1
                    if i + 1 < m and grid[i + 1][j] == 1:
                        bfs_queue.append((i + 1, j))
                        grid[i + 1][j] = 2
                        made_rotten = True
                        non_zero_nodes += 1
            if made_rotten:
                total_time_for_rotting += 1

        if non_zero_nodes + zero_nodes != m * n:
            return -1

        return total_time_for_rotting


if __name__ == '__main__':
    print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(Solution().orangesRotting([[0, 2]]))
    print(Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
