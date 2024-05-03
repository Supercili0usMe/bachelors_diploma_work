'''
version1 = rev0.rev1.rev2
version1 = rev0.rev1


'''

def compareVersion(version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        
        len_diff = len(version1) - len(version2)
        if len_diff < 0:
            version1 += [0] * abs(len_diff)
        elif len_diff > 0:
            version2 += [0] * len_diff
        
        for v1, v2 in zip(version1, version2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0


print(compareVersion("1.01", "1.001"))
print(compareVersion("1.0", "1.0.0"))
print(compareVersion("0.1", "1.1"))
print(compareVersion("1.2", "1.10"))
print(compareVersion("1.0.1", "1"))
print(compareVersion("0.1", "1.1"))