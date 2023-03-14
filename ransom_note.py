def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine): return False

    ransomDict, magazineDict = {}, {}

    for i in ransomNote:
        ransomDict[i] = 1 + ransomDict.get(i, 0)
    
    for i in magazine:
        magazineDict[i] = 1 + magazineDict.get(i, 0)

    for i in ransomDict.keys():
        if (ransomDict[i] > magazineDict.get(i, 0)):
            return False
    
    return True
    