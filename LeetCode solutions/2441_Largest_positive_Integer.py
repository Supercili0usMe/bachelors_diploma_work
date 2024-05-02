'''
Не самое трудное задание
'''
from typing import List


def findMaxK(nums: List[int]) -> int:
    maxPos = -1
    nums = set(nums)
    for num in nums:
        if num > 0:
            if -num in nums and num > maxPos:
                maxPos = num
    return maxPos

print(findMaxK([-1,2,-3,3]))
print(findMaxK([-1,10,6,7,-7,1]))
print(findMaxK([-10,8,6,7,-2,-3]))
print(findMaxK([-24,8,6,46,-45,-5,37,-10,1]))
print(findMaxK([-9,-43,24,-23,-16,-30,-38,-30]))