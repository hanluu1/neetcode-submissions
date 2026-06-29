class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1,0], [1,0], [0,1], [0, -1]] 
        rows, cols = len(grid), len(grid[0])
        islands = 0

        #detect the islands
        #if r, c out of bound less than 0 or larger than actual len of rows and cols
        #or it is water continue to go
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            
            grid[r][c] = '0' #after visited mark current cell 0 mean visited
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c) #dfs to find all the block with 1 to form the islands
                    islands += 1

        return islands

