from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def helper(start, end, par_str):
            nonlocal output
            if start == end == n:
                output.append(par_str)
                return

            if start < n:
                helper(start + 1, end, par_str + "(")

            if end < start:
                helper(start, end + 1, par_str + ")")

        helper(1, 0, "(")
        return output


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))


"""
["(())","()()"]
["(())()","()()()","()(())","(()())","((()))"]
["((())())","(()()())","(()(()))","((()()))","(((())))", ]
["(()())()()","()(())(())","(())()(())","((()))()()","()()(()())","(((())))","(())(()())","((()()))","()()((()))","((())())","(())()()()","(())(())()","(()(()))","()()()()()","(()()())","()()()(())","()(())()()","(())((()))","()()(())()","((()))(())","(()())(())"]
"""
