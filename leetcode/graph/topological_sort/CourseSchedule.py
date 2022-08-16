from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        count = 0
        while bfs_queue:
            node = bfs_queue.popleft()
            count += 1
            for adj in adj_list[node]:
                indegree_list[adj] -= 1
                if indegree_list[adj] == 0:
                    bfs_queue.append(adj)

        return count == numCourses


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]))
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))
