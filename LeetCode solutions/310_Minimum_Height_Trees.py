from typing import List
from collections import defaultdict, deque
'''
Основная идея решения: корень дерева минимальной высоты близок к центру дерева.
Сам алгоритм схож с отчисткой лука - нужно убирать внешние слои (листья) один за одним,
пока не доберемся до ядра. 
Пошагово алгоритм можно расписать следующим образом:
1. Найти все листья в графе (вершины с одним соседом)
2. Удалить все найденные листья с их ребрами, чтобы получился новый слой листьев
3. Повторять процесс пока не останутся 1 или 2 вершины.

Почему 1 или 2? Потому что если в дерево состоит из нечетного количества вершин, центральная
вершина будет одна, а если в дереве четное число вершин - будет 2 центра. 
'''

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    # Single-node tree
    if n == 1:
        return [0]
    
    # Prepare adjacency list and degree list
    adjacency_list = defaultdict(list)
    degrees = [0] * n
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    # Queue with all leaf nodes
    leaves_queue = deque(i for i, degree in enumerate(degrees) if degree == 1)
    ans = []

    # Implementation of BFS to trimming leaves
    while leaves_queue:
        ans.clear()
        for _ in range(len(leaves_queue)):
            current_node = leaves_queue.popleft()
            ans.append(current_node)
            for neighbor in adjacency_list[current_node]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    leaves_queue.append(neighbor)
                
    return ans

print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))