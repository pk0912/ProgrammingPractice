from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        start = 0
        end = 0
        letter_counts = defaultdict(int)
        max_len = 0
        while end < len(s):
            if letter_counts[s[end]] == 0:
                letter_counts[s[end]] += 1
                end += 1
            else:
                max_len = max(max_len, end - start)
                letter_counts[s[start]] -= 1
                start += 1
        return max(max_len, end - start)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
