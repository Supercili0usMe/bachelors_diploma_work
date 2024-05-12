import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
        rate = sorted([(w/q, q) for q, w in zip(quality, wage)])
        res_sum = float("inf")
        heap, qualitySum = [], 0
        for ratio, q in rate:
            heapq.heappush(heap, -q)
            qualitySum += q
            if len(heap) > k:
                qualitySum += heapq.heappop(heap)
            if len(heap) == k:
                res_sum = min(res_sum, qualitySum * ratio)
        return round(res_sum, 5)

print(Solution.mincostToHireWorkers([10,20,5], [70,50,30], 2))
print(Solution.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))
print(Solution.mincostToHireWorkers([4,5], [8,14], 2))
print(Solution.mincostToHireWorkers([25,68,35,62,52,57,35,83,40,51], [147,97,251,129,438,443,120,366,362,343], 6), 1979.31429)
print(Solution.mincostToHireWorkers([3,5,8,10,9,5,1,2,4,1], [8,8,6,9,5,6,8,7,5,8], 3), 21.25000)
print(Solution.mincostToHireWorkers([5,7,4,2,6,5,10,9,4,2], [10,10,3,7,3,7,6,2,6,4], 3), 14.25000)