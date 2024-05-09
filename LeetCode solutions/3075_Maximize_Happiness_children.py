from typing import List


class Solution:
    def maximumHappinessSum(happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)[:k]
        ans = sum(max(n-i, 0) for i, n in enumerate(happiness))
        return ans

print(Solution.maximumHappinessSum([1,2,3], 2))
print(Solution.maximumHappinessSum([1,1,1,1], 2))
print(Solution.maximumHappinessSum([2,3,4,5], 1))
print(Solution.maximumHappinessSum([2,23,97], 2))
'''
You are given an array happiness of length n, and a positive integer k.
There are n children standing in a queue, where the ith child has happiness value happiness[i].
You want to select k children from these n children in k turns.
In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1.
Note that the happiness value cannot become negative and gets decremented only if it is positive.
Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.
'''