class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        def dfs(r, c):            
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or grid[r][c] == '0':
                return       
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
                    
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                
                if cell == '0':
                    continue
                
                if cell == '1':
                    num_islands += 1
                    dfs(r, c)
                                  
        return num_islands