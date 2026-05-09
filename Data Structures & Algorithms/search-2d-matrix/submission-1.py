class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0]) 
        
        low = 0
        high = row * col - 1 #length of the whole matrix -1 

        while low <= high:
            mid = low + (high-low) // 2 
            x = mid // col
            y = mid % col
            midNum = matrix[x][y]
            if midNum == target:
                return True
            if midNum < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
            

        