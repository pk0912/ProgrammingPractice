class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_ptr = 0
        first_occurrence = -1
        needle_start = 0
        needle_end = 0
        while haystack_ptr < len(haystack) and needle_end < len(needle):
            if haystack[haystack_ptr] == needle[needle_end]:
                if first_occurrence == -1:
                    first_occurrence = haystack_ptr
                haystack_ptr += 1
                needle_end += 1
            else:
                haystack_ptr = needle_start + 1
                needle_start = haystack_ptr
                needle_end = 0
                first_occurrence = -1
        if needle_end < len(needle):
            return -1
        return first_occurrence


if __name__ == '__main__':
    print(Solution().strStr("sadbutsad", "sad"))
