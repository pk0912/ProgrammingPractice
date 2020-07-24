from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for ind, val in enumerate(nums):
            if target - val in num_dict:
                return [num_dict.get(target - val), ind]
            num_dict[val] = ind
        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([1, 2, 3, 4], 8))
print(sol.twoSum([2, 6, 7, 4], 9))
print(sol.twoSum([1, 2, 2, 4], 4))
