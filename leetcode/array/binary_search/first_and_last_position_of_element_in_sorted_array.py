from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        first_pos = -1
        last_pos = -1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                first_pos = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                last_pos = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [first_pos, last_pos]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 8, 10], 8))
