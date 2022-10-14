from functools import lru_cache
from typing import List


class Solution:
    def digLetter(self, digit):
        dig_letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        return dig_letter_map.get(digit, [])

    @lru_cache(None)
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        child_combs = self.letterCombinations(digits[1:])
        parent_child_combs = []
        parent_combs = self.digLetter(digits[0])
        if len(child_combs) == 0:
            return parent_combs
        for p in parent_combs:
            parent_child_combs += [p + c for c in child_combs]
        return parent_child_combs


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
