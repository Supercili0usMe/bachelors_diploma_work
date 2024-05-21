from typing import List


class Solution:
    def subsets(nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
        return ans

print(Solution.subsets([1,2,3]))
print(Solution.subsets([0]))
print(Solution.subsets([3,2,4,1]))
print(Solution.subsets([1,2]))