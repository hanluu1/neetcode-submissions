class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        land = None
        found = False
        ans = 0
        #scan first land
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land = (i, j)
                    found = True
                    break
            if found: break
        
        q = deque([land])
        visited = set()
        visited.add(land)
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        
        while q:
            x, y = q.popleft()
            ans += 4  
            
            for dx, dy in directions:
                landx = x + dx
                landy = y + dy
                
                if 0 <= landx < rows and 0 <= landy < cols and grid[landx][landy] == 1:
                    ans -= 1
                
                    if (landx, landy) not in visited:
                        visited.add((landx, landy))
                        q.append((landx, landy))
        
        return ans
