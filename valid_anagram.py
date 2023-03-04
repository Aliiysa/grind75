def isAnagram(s, t):

    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[i] = 1 + countS.get(s[i], 0)
        countT[i] = 1 + countT.get(t[i], 0)

    if countS.keys() != countT.keys():
        return False
    
    # for c in countS:
    #     if countS[c] != countT.get(c, 0):
    #         return False

    return True