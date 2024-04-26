'''
Дана целочисленная матрица n x n.
Вернуть минимальную траекторию падения с ненулевыми сдвигами*

* траектория падения с ненулевыми сдвигами - это выбор ровно
одного элемента из каждой строки матрицы таким образом, чтобы никакие
два элемента в соседних строках не находились в одном столбце.

Интересная задачка на динамическое программирование. Сам решение придумать 
не смог, помог видос с объяснением основной концепции решения:
https://www.youtube.com/watch?v=349jxgTbFgo
'''
from typing import List


def minFallingPathSum(grid: List[List[int]]) -> int:
    if len(grid) == 1:
        return grid[0][0]
    min1, min2 = 100, 100
    min1_id = -1
    for row_i, row in enumerate(grid):
        if row_i != 0:
            for elem_i in range(len(row)):
                if elem_i != min1_id:
                    row[elem_i] += min1
                else:
                    row[elem_i] += min2
        min1 = min(row)
        min1_id = row.index(min1)
        min2 = min(x for i, x in enumerate(row) if i != min1_id)
    return min1

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(minFallingPathSum([[7]]))
print(minFallingPathSum([[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]))
print(minFallingPathSum([[-7, 1, -3], [-5, 0, 4], [-6, -8, 8]]))
print(minFallingPathSum([[-8, 6, 5, 7], [-3, 4, 4, 2], [3, -1, 5, -6], [5, 3, 6, 2]]))