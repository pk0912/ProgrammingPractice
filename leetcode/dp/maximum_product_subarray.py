from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            temp = max(num, num * max_prod, num * min_prod)
            min_prod = min(num, num * max_prod, num * min_prod)
            max_prod = temp
            result = max(result, max_prod)
        return result


if __name__ == '__main__':
    print(Solution().maxProduct([-2, 3, -4]))


"""
[-2,0,-1]
[0,1,2,3]
[0,2]
"""