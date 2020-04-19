# O(m x n) DP solution
class Solution:
    def minPathSum(self, grid):
        # Initialize memoization array: holds min path sum at (y, x)
        memo = [[-1 for col in row] for row in grid]
        
        def sum(y, x):
            # If we already know min sum path, just return it
            if memo[y][x] >= 0:
                return memo[y][x]

            # Base case: If we are at the top left corner, the value 
            # of the element is its min sum path
            if x-1 < 0 and y-1 < 0:
                memo[y][x] = grid[y][x]
                return memo[y][x]

            # If we are in the top row, the min sum path must be on the 
            # decreasing indices along this row.
            elif y-1 < 0:
                if memo[y][x-1] >= 0:
                    memo[y][x] = memo[y][x-1] + grid[y][x]
                    return memo[y][x]
                return grid[y][x] + sum(0, x-1)

            # If we are in the leftmost column, the min sum path must
            # be on the decreasing indices along this column
            elif x-1 < 0:
                if memo[y-1][x] >= 0:
                    memo[y][x] = memo[y-1][x] + grid[y][x]
                    return memo[y][x]
                return grid[y][x] + sum(y-1, 0)
            
            # If we are elsewhere in the grid, take the minimum of the
            # min path sums of the element above and to the left.
            else:
                memo[y][x]  = grid[y][x] + min(sum(y-1, x), sum(y, x-1))
                return memo[y][x]
        
        # Start recursion at the goal (bottom right-most) element
        return sum(len(grid) - 1, len(grid[0]) - 1)