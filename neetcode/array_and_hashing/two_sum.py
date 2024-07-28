from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_ind_dict = dict()
        for i in range(0, len(nums)):
            if target - nums[i] in diff_ind_dict.keys():
                return [diff_ind_dict.get(target - nums[i]), i]
            diff_ind_dict[nums[i]] = i
        return []


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
