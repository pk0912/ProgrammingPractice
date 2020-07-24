class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if type(matrix) != list:
            return False
        if len(matrix) == 0:
            return False
        if type(matrix[0]) != list:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = cols - 1
        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


sol = Solution()
print(sol.searchMatrix(
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ],
    26,
))
print(sol.searchMatrix(
    [
        [1, 4, 7, 11, 15],
    ],
    0,
))
print(sol.searchMatrix(
    [1, 4, 7, 11, 15],
    0,
))
print(sol.searchMatrix(
    [],
    0,
))
print(sol.searchMatrix(
    [[]],
    0,
))
