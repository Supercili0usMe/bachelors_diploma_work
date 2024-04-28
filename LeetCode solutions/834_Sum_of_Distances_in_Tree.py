'''
Основная идея - перестроение дерева.
Каждый раз когда мы перестраиваем дерево, все дочерние вершины графа приближаются на 1,
а остальные удаляются на 1.
Основная формула перерасчета выглядит следующим образом:
ans[vert] = ans[parent] + num_vert - 2*(num_childs - 1)

Или же:
ans[vert] = ans[parent] + (num_vert - num_childs - 1) - num_childs - 1
'''
from typing import List


def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    nodeCount, result = [0]*(n+1), [0]*(n+1)
    parents_list = [[] for _ in range(n+1)]
    for edge in edges:
        u, v = edge
        parents_list[u].append(v)
        parents_list[v].append(u)
    
    def populate(node, adj, p=-1):
        nodeCount[node] = 1
        for ch in adj[node]:
            if ch==p: continue
            populate(ch, adj, node)
            nodeCount[node] += nodeCount[ch]
            result[node] += result[ch] + nodeCount[ch]
    
    def dfs(node, adj, p=-1):
        if p != -1:
            result[node] = result[p] - nodeCount[node] + (len(adj) - nodeCount[node] - 1)
        for ch in adj[node]:
            if ch==p: continue
            dfs(ch, adj, node)
            
    populate(1, parents_list)
    dfs(1, parents_list)
    return result[:-1]

assert sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]) == [8,12,6,10,10,10]
assert sumOfDistancesInTree(1, []) == [0]
assert sumOfDistancesInTree(2, [[1,0]]) == [1,1]