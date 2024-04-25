'''
В решении этой задаче мне помог данный комментарий:
The way I understand it:

Generally a character can be start of the sequence or part of another sequence
If there exists a sequence which a character can be a part of, greedily joining the previous sequence will be a better decision.
Keep track of the maximum length which can end with char-c in an array
Max of this array is the result.
eg:
'acfbd'
[a,b,c,d,e,f]
[0,0,0,0,0,0] <- initial state

for a: best case scenario is 1 (surrounding is zero)
for c: best case is max(a,b,c,d,e) + 1 => [1,0,2,0,0,0]
for f: bese case is max(c,d,e,f)+1 => [1,0,2,0,0,1]
for b: best case is max(a,b,c,e)+1 => [1,3,2,0,0,1]
for d: besy case is max(b,c,d,e,f)+1 => [1,3,2,4,0,1]
'''
def longestIdealString(s: str, k: int) -> int:
    # Initial vars
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = dict.fromkeys([l for l in alphabet], 0)
    
    # Solution
    for ch in s:
        i = alphabet.find(ch)
        start, stop = i-k, i+k+1
        if start < 0: start = 0
        if stop > len(alphabet): stop = len(alphabet)
        letters = [alphabet[i] for i in range(start, stop)]
        d[ch] = max([d[l] for l in letters]) + 1
    return max(d.values())

# print(longestIdealString('acfgbd', 2))  # 4
print(longestIdealString('abcd', 3))  # 4