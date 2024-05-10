from typing import List


class Solution:
    def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
        return sorted([(arr[i]/arr[j], arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr))])[k-1][1:]

print(Solution.kthSmallestPrimeFraction([1,2,3,5], 3))
print(Solution.kthSmallestPrimeFraction([1,7], 1))