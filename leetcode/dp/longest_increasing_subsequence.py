from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            tmp = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp = max(dp[i] + dp[j], tmp)
            dp[i] = tmp

        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))