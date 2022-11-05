class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * (n + 1)
        for i in range(m):
            temp = [0] * (n + 1)
            for j in range(n):
                if i == 0 and j == 0:
                    temp[j+1] = 1
                else:
                    temp[j+1] = prev[j+1] + temp[j]
            prev = temp
        return prev[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
