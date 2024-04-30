def wonderfulSubstrings(word: str) -> int:
    freq={}
    freq[0]=1
    mask, res = 0, 0

    for ch in word:
        bit = ord(ch) - 97
        mask ^= (1 << bit)
        if mask in freq:
            res += freq[mask]
            freq[mask] += 1
        else:
            freq[mask] = 1
        
        for odd_ch in range(11):
            if (mask ^ (1 << odd_ch)) in freq:
                res += freq[mask ^ (1 << odd_ch)]
    return res

print(wonderfulSubstrings('aba'))
print(wonderfulSubstrings('aabb'))
print(wonderfulSubstrings('he'))
print(wonderfulSubstrings('acadac'))