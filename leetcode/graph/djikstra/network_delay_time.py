import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist_list = [float("inf")] * (n + 1)
        dist_list[0] = 0
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        min_heap = []
        heapq.heapify(min_heap)
        dist_list[k] = 0
        heapq.heappush(min_heap, (0, k))
        while min_heap:
            distance, popped_node = heapq.heappop(min_heap)
            for node, weight in adj_list[popped_node]:
                node_dist = distance + weight
                if node_dist < dist_list[node]:
                    dist_list[node] = node_dist
                    heapq.heappush(min_heap, (node_dist, node))
        if float("inf") in dist_list:
            return -1
        return max(dist_list)


if __name__ == '__main__':
    print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
