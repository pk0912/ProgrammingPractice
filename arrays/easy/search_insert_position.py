from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_index = 0
        u_index = len(nums) - 1
        while l_index <= u_index:
            m_index = (l_index + u_index) // 2
            if nums[m_index] == target:
                return m_index
            elif nums[m_index] < target:
                l_index = m_index + 1
            else:
                u_index = m_index - 1
        return l_index


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))
print(sol.searchInsert([1, 3, 5, 6], 2))
print(sol.searchInsert([1, 3, 5, 6], 7))
print(sol.searchInsert([1, 3, 5, 6], 0))
