"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Hint:
Focus from the right side. Find the max iteratively from the RHS,
for each element the right max will be calculated beforehand.
This will help in runtime efficiency as max will be calculated on only 2 elements each time.
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr


if __name__ == '__main__':
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
    print(Solution().replaceElements([400]))
