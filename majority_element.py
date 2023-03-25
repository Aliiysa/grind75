def majorityElement(nums):
    count = {}
    result, maxCount = 0, 0

    for i in nums:
        count[i] = 1 + count.get(i, 0)
        result = i if count[i] > maxCount else result
        maxCount = max(count[i], maxCount)
    
    return result


    # return sorted(count.items(), key=lambda item:item[1])[-1][0]

    
    
    # Boyer-Moore Algorithm

    # result, count = 0, 0

    # for n in nums:
    #     if count == 0:
    #         result = n
    #     count += (1 if n == result else -1)
    # return result