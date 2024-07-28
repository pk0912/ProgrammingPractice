from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letter_count = Counter(s)
        t_letter_count = Counter(t)
        for k, v in s_letter_count.items():
            if v != t_letter_count.get(k, 0):
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("cat", "car"))
