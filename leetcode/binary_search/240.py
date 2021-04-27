class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in list(chain(*matrix))


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1

        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
