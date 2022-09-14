from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        node_color = [-1] * n
        bfs_q = deque()
        for i in range(n):
            if node_color[i] == -1 and len(bfs_q) == 0:
                node_color[i] = 0
                bfs_q.appendleft(i)
            while bfs_q:
                popped_ele = bfs_q.popleft()
                adj_color = abs(node_color[popped_ele] - 1)
                for e in graph[popped_ele]:
                    if node_color[e] == -1:
                        node_color[e] = adj_color
                        bfs_q.appendleft(e)
                    else:
                        if node_color[e] == node_color[popped_ele]:
                            return False
        return True


if __name__ == '__main__':
    print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
