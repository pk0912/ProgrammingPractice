from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 2
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]


if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
