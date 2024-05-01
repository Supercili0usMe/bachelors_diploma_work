'''
Достаточно простая задача, не требующая долгих размышлений
'''
def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word
    id = word.index(ch)
    return word[id::-1]+word[id+1:]

print(reversePrefix("abcdefd", 'd'))
print(reversePrefix("xyxzxe", 'z'))
print(reversePrefix("abcd", 'z'))
