def containDuplicates(nums):
    counts = {}
    for i in nums:
        if i in counts:
            return True
        counts[i] = 1 + counts.get(i, 0)
    
    return False

# Insted of using dictionary() you can use set()

def containDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    
    return False