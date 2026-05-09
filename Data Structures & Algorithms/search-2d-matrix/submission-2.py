class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = row * col - 1

        while low <= high:
            mid = low + (high - low) // 2
            x = mid // col
            y = mid % col

            if matrix[x][y] < target:
                low = mid + 1
            elif matrix[x][y] > target:
                high = mid - 1
            else:
                return True
        return False 
