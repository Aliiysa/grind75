def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    pCount, sCount = {}, {}

    for c in range(len(p)):
        pCount[p[c]] = 1 + pCount.get(p[c], 0)
        sCount[s[c]] = 1 + sCount.get(s[c], 0)
    
    result = [0] if pCount == sCount else []
    left = 0
    for right in range(len(p), len(s)):
        sCount[s[right]] = 1 + sCount.get(s[right], 0)
        sCount[s[left]] -= 1

        if sCount[s[left]] == 0:
            sCount.pop(s[left])
        left += 1
        if sCount == pCount:
            result.append(left)
    
    return result