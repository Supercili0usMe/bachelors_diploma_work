from typing import List


class Solution:
    def matrixScore(grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][0] == 0:
                    grid[i] = [0 if i == 1 else 1 for i in grid[i]]

        for i in range(n):
            for j in range(m):
                col = [grid[k][j] for k in range(n)]
                if sum(col) <= n/2:
                    col = [0 if i == 1 else 1 for i in col]
                    for k in range(n):
                        grid[k][j] = col[k]
        for i in grid:
            temp = "".join(str(num) for num in i)     
            ans += int(temp, 2)  
        return ans

print(Solution.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
print(Solution.matrixScore([[0]]))
print(Solution.matrixScore([[0,1,1],[1,1,1],[0,1,0]]))
print(Solution.matrixScore([[0],[1],[1],[0],[0],[1],[0],[1],[0],[0],[1],[1],[0],[0],[0],[1],[0],[1],[0],[0]]))
print(Solution.matrixScore([[0],[1]]))
print(Solution.matrixScore([[0, 1, 1], [1, 1, 1]]))
'''
0 1 1 0 0 1 0 1 0 0 1 1 0 0 0 1 0 1 0 0
1 1 1 0 0 1 0 1 0 0 1 1 0 0 0 1 0 1 0 0
0 0 0 1 1 0 1 0 1 1 0 0 1 1 1 0 1 0 1 1 

'''