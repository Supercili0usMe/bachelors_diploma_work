'''
Элементарно, Ватсон!
После предыдущих мозговыносящих задач, это просто расслабление
'''
from functools import reduce
from typing import List


def minOperations(nums: List[int], k: int) -> int:
    return bin(k ^ reduce(lambda x, y: x ^ y, nums)).count("1")
    ...

print(minOperations([2,1,3,4], 1))
print(minOperations([2,0,2,0], 0))
print(minOperations([0], 1023))
print(minOperations([1], 1024))
print(minOperations([1,2,3,4,5,6], 100))
print(minOperations([0,1,2,4,8,16,32,64,128,256,512], 1024))