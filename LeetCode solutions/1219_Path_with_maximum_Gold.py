from typing import List


class Solution:
    def getMaximumGold(grid: List[List[int]]) -> int:
        directions = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        maxGold = 0

        def dfs_backtrack(grid, rows, cols, row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == 0:
                return 0
            max_gold = 0
            val = grid[row][col]
            grid[row][col] = 0
            
            for d in range(4):
                max_gold = max(max_gold, dfs_backtrack(grid, rows, cols, directions[d] + row, directions[d+1] + col))
            
            grid[row][col] = val
            return max_gold + val

        for i in range(rows):
            for j in range(cols):
                maxGold = max(maxGold, dfs_backtrack(grid, rows, cols, i, j))
        return maxGold

print("24", Solution.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
print("28", Solution.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print("0", Solution.getMaximumGold([[0]]))
print("100", Solution.getMaximumGold([[100]]))
print("147", Solution.getMaximumGold([[0,56,0,41,0],[0,0,45,0,0],[70,0,0,0,0],[11,0,67,0,0],[66,0,0,67,0]]))