def minWindow(s, t):
    if t == "": return ""

    tCount, window = {}, {}
    
    for c in t:
        tCount[c] = 1 + tCount.get(c, 0)

    have, need = 0, len(tCount)
    result, resLen = [-1, -1], float("inf")
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = 1 + window.get(char, 0)

        if char in tCount and window[char] == tCount[char]:
            have += 1
        
        while have == need:
            # update result
            resLen = min(right - left + 1, resLen)
            result = [left, right]
            # pop from the left of window
            window[s[left]] -= 1
            if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                have -= 1
            left += 1            
    
    left, right = result
    return s[left : right + 1] if resLen != float("inf") else ""