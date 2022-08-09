# [
#     [00,01,02,03]   [30,20,10,00]
#     [10,11,12,13]   [31,21,11,01]
#     [20,21,22,23]   [32,22,12,02]
#     [30,31,32,33]   [33,23,13,03]
# ]
# [
#     [00,01,02]      [20,10,00]
#     [10,11,12]      [21,11,01]
#     [20,21,22]      [22,12,02]
# ]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        while l < r:
            for i in range(r-l):
                top = l
                bottom = r

                topLeft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]

                matrix[bottom-i][l] = matrix[bottom][r-i]

                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topLeft

            r -= 1
            l += 1
