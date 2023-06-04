def myAtoi(s):
    s = s.strip()

    if not s:
        return 0
    negative = False
    result = 0

    if s[0] == "-":
        negative = False
    elif s[0] == "+":
        negative = True
    elif not s[0].isdigit():
        return 0
    else:
        result = ord(s[0]) - ord("0")

    for i in range(1, len(s)):
        if s[i].isnumeric():
            result = result * 10 + (ord(s[i]) - ord("0"))
            if not negative and result >= (2**31 -1):
                return 2**31 -1
            if negative and result >= (2**31):
                return -2**31
        else:
            if not negative:
                return result
            else:
                return -result
    
    if not negative:
        return result
    else:
        return -result
