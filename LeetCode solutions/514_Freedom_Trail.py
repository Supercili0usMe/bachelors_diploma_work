'''
Дан ротор с написанным кодом и ключевое слово.
Необходимо вернуть минимальное количество шагов для написания кода.

За 1 шаг можно сделать:
1) Повернуть ротор на 1 символ по часовой/против часовой стрелки.
2) Нажать на центральную кнопку для выбора символа.

Пример:
код = "godding", слово = "gd"

Шаг 1:
godding
|
Первый символ кодового слова 'g' уже находится в качестве выбора, значит просто нажимаем на кнопку (Шаг 1).
Следующий символ 'd' находится в 2-ух символах от выбранного, значит вращаем ротор 2 раза:

Шаг 2:
godding
 |

Шаг 3:
godding
  |
Нажимаем на кнопку, поскольку выбранный символ равен символу ключевого слова.
Ответ: 4
'''

def findRotateSteps(ring: str, key: str) -> int:
    steps, id = 0, 0
    for ch in key:
        for i in range(len(ring)):
            ch_ = ring[id]
            prev, next = ring[id-i], ring[(id+i) % len(ring)]
            if next == ch:
                steps = steps + i + 1
                id += i
                if id >= len(ring):
                    id %= len(ring)
                break
            if prev == ch:
                steps = steps + i + 1
                id -= i
                if id < 0:
                    id = len(ring) + id 
                break
    return steps
    ...

print(findRotateSteps("godding", 'og'))
print(findRotateSteps("godding", 'godding'))
print(findRotateSteps("abcde", "ade"))
print(findRotateSteps("iotfo", "fioot"))
print(findRotateSteps("aaaaa", "aaaaa"))
print(findRotateSteps("nyngl", "yyynnnnnnlllggg"))

'''
Признал поражение из-за нехватки времени, последний тест меня сломал
В будущем обязательно допилю решение до конца

Решение которое я использовал:
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        matches = {}
        for i in range(n):
            matches.setdefault(ring[i], []).append(i)
        
        pos_cost = [(0, 0)]
        for ch in key:
            pos_cost_curr = []
            for curr_pos in matches[ch]:
                curr_cost = float('inf')
                for pos, cost in pos_cost:
                    clkwise_trans_cost = abs(pos - curr_pos)
                    temp_cost = cost + min(clkwise_trans_cost, n - clkwise_trans_cost)
                    curr_cost = min(curr_cost, temp_cost)
                pos_cost_curr.append((curr_pos, curr_cost))
            pos_cost = pos_cost_curr
        
        min_cost = float('inf')
        for pos, cost in pos_cost:
            min_cost = min(min_cost, cost)
        
        return min_cost + len(key)
'''