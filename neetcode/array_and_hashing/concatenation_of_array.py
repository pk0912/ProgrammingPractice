from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == '__main__':
    print(Solution().getConcatenation([1, 2, 1]))
    print(Solution().getConcatenation([1, 3, 2, 1]))
