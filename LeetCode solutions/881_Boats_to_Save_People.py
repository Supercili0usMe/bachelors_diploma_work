'''
1. сортируем список
2. вводим два итератора и результирующую переменную
3. Пока start <= end:
    a. Если сумма people[start] + people[end] помещается в лодку:
        Увеличиваем минимальный вес
    b. Уменьшаем максимальный вес
    с. Добавляем лодку
4. Возвращаем количество лодок
'''
from typing import List


class Solution:
    def numRescueBoats(people: List[int], limit: int) -> int:
        people.sort()
        start, end, ans = 0, len(people) - 1, 0
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            ans += 1
        return ans

print(Solution.numRescueBoats([1, 2], 3))
print(Solution.numRescueBoats([3,2,2,1], 3))
print(Solution.numRescueBoats([3,5,3,4], 3))