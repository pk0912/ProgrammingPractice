"""
Maximum sum of non-adjacent elements in a list with non-negative numbers
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # Below is the approach of recursion using memoization
        # TC : O(n)  SC : O(n) + O(n)
        #         @lru_cache(None)
        #         def helper(ind):
        #             if ind == 0:
        #                 return nums[0]
        #             if ind < 0:
        #                 return 0
        #             pick = nums[ind] + helper(ind - 2)
        #             not_pick = helper(ind - 1)
        #             return max(pick, not_pick)

        #         return helper(len(nums) - 1)

        # Below is the approach with tabulation and constant space complexity
        # TC : O(n)  SC : O(1)
        prev2 = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            pick = nums[i]
            if i > 1:
                pick += prev2
            not_pick = prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr

        return prev