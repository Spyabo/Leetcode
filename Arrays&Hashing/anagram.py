def isAnagram(s: str, t: str) -> bool:
    dictS = {}
    dictT = {}
    
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        dictS[s[i]] = dictS.get(s[i], 0) + 1
        dictT[t[i]] = dictT.get(t[i], 0) + 1
    for j in dictS:
        if j not in dictT:
            return False
        if dictS[j] != dictT[j]:
            return False
    return True

isAnagram(s = 'anagram',t = 'nagaram') 