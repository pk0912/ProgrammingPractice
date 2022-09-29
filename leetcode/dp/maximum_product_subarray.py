from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float("-inf")
        curr_prod = 1
        start = 0
        end = 0
        while end < len(nums):
            temp = max(curr_prod * nums[end], nums[end])
            if temp >= max_prod:
                max_prod = temp
                curr_prod = temp
                end += 1
            else:
                if nums[start] == 0:
                    curr_prod = nums[end]
                    start = end
                else:
                    curr_prod = curr_prod // nums[start]
                    start += 1
            if start == end:
                end += 1
        return max_prod


if __name__ == '__main__':
    print(Solution().maxProduct([-2, 3, -4]))


"""
[-2,0,-1]
[0,1,2,3]
[0,2]
"""