from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_cons_count = 0
        for num in nums:
            cons_count = 1
            if num - 1 not in nums_set:
                temp = num
                while 1:
                    temp += 1
                    if temp in nums_set:
                        cons_count += 1
                    else:
                        max_cons_count = max(max_cons_count, cons_count)
                        break
        return max_cons_count


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
