def maxSubArray(nums):
    
    # Kadane's Algorithm
    
    maxSum, curSum = nums[0], 0

    for i in nums:

        curSum += i
        if curSum < i:
            curSum = i
            
        if maxSum < curSum:
            maxSum = curSum
        
    return maxSum

