class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x *= -1
            neg = True
        r = 0
        while x > 0:
            q = x // 10
            r = x % 10 + r * 10
            x = q
        if neg:
            r *= -1
        if -2 ** 31 <= r <= (2 ** 31) - 1:
            return r
        return 0


if __name__ == '__main__':
    print(Solution().reverse(1534236469))
    print(Solution().reverse(-123))
