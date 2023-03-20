def longestPalindrome(s):
    counts = {}
    result = 0
    odd_found = False

    for i in s:
        counts[i] = 1 + counts.get(i, 0)
    
    # for count in counts.values():
    #     result += (count // 2) * 2
    #     if result % 2 == 0 and count % 2 == 1:
    #         result += 1
    #return result
    
    for count in counts.values():
        if count % 2 == 0: result += count
        else:
            odd_found = True
            result += count -1
    if odd_found: result += 1
    
    return result
