import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        for i in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, i)
            else:
                if min_heap[0] <= i:
                    heapq.heappushpop(min_heap, i)
        return min_heap[0]


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
