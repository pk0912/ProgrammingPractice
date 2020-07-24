from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return len(height)


sol = Solution()
sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
