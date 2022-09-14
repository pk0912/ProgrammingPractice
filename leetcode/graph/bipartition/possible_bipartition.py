from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n < 2:
            return True
        adj_list = defaultdict(list)
        for i, j in dislikes:
            adj_list[i].append(j)
            adj_list[j].append(i)
        color_node = [-1] * (n + 1)
        bfs_q = deque()
        for i in range(1, n + 1):
            if color_node[i] == -1 and len(bfs_q) == 0:
                color_node[i] = 0
                bfs_q.appendleft(i)
            while bfs_q:
                popped_ele = bfs_q.popleft()
                adj_ele = adj_list[popped_ele]
                color = color_node[popped_ele]
                adj_color = abs(color - 1)
                for e in adj_ele:
                    if color_node[e] == -1:
                        color_node[e] = adj_color
                        bfs_q.appendleft(e)
                    else:
                        if color_node[e] == color:
                            return False
        return True


if __name__ == '__main__':
    print(Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
    print(Solution().possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
