"""
Cycle Detection in Directed Graph using BFS can be done by using Kahn's Algo
If it is Directed Acyclic Graph (DAG), using BFS topological sort could be done as well
"""


from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for p in prerequisites:
            adj_list[p[1]].append(p[0])

        indegree_list = [0] * numCourses

        for i in range(numCourses):
            for adj in adj_list[i]:
                indegree_list[adj] += 1

        bfs_queue = deque()

        for i in range(numCourses):
            if indegree_list[i] == 0:
                bfs_queue.append(i)

        topological_traversal = []

        while bfs_queue:
            node = bfs_queue.popleft()
            topological_traversal.append(node)
            for adj in adj_list[node]:
                indegree_list[adj] -= 1
                if indegree_list[adj] == 0:
                    bfs_queue.append(adj)

        if len(topological_traversal) != numCourses:
            return []

        return topological_traversal


if __name__ == '__main__':
    print(Solution().findOrder(2, [[1, 0]]))
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(Solution().findOrder(1, []))
    print(Solution().findOrder(3, [[1, 0], [1, 2], [0, 1]]))
