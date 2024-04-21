from typing import List
from collections import defaultdict, deque


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # Ordinary BFS for Graph
    # Обычный поиск в ширину для графа
    adjacency_list = defaultdict(list)
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    queue, visited = deque(), [False] * n
    visited[source] = True
    queue.append(source)

    while queue:
        currentNode = queue.popleft()
        print(f'{currentNode = }')
        for neighbor in adjacency_list[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited[destination]


# print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))