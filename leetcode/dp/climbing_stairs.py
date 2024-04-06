class Solution:
    def climbStairs(self, n: int) -> int:
        # TC: O(n)
        # Recursive Memoized Solution : Accepted at leetcode SC: O(n) + O(n)
        # dp = [-1] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # def helper(m: int):
        #     if m <= 1:
        #         return 1
        #     if dp[m] == -1:
        #         dp[m] = helper(m - 1) + helper(m - 2)
        #     return dp[m]
        # return helper(n)

        # Tabulation Solution : Accepted at leetcode SC: O(n)
        # dp = [-1] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # Tabulation Solution: Constant Space
        prev = 1
        prev2 = 1
        for i in range(2, n + 1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr
        return prev


if __name__ == '__main__':
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
