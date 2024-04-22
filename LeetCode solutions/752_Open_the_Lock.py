'''
Немного усложненный вариант BFS (поиск в ширину)
без помощи ChatGPT (он оптимизировал код), вылезала Time Limit Error
'''
from typing import List
from collections import defaultdict, deque


def openLock(deadends: List[str], target: str) -> int:
    if target == "0000":
        return 0
    
    deadends_set = set(deadends)
    if "0000" in deadends_set:
        return -1

    adjacency_list = defaultdict(list)
    for num in range(10000):
        node = str(num).zfill(4)
        if node in deadends_set:
            continue
        for i, curr_digit in enumerate(node):
            pos_digit = int(curr_digit) + 1 if int(curr_digit) < 9 else 0
            neg_digit = int(curr_digit) - 1 if int(curr_digit) > 0 else 9
            new_node1 = node[:i] + str(pos_digit) + node[i+1:]
            new_node2 = node[:i] + str(neg_digit) + node[i+1:]
            if new_node1 not in deadends_set:
                adjacency_list[node].append(new_node1)
            if new_node2 not in deadends_set:
                adjacency_list[node].append(new_node2)

    queue = deque([("0000", 0)])
    visited = {"0000"}

    while queue:
        current_node, depth = queue.popleft()
        if current_node == target:
            return depth
        for neighbor in adjacency_list[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    return -1
