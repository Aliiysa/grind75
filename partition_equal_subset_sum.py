def canPartition(nums):
    if sum(nums) % 2:
        return False
    target = sum(nums) // 2
    dp = set()
    dp.add(0)

    for i in range(len(nums) -1, -1, -1):
        tempDP = set()
        for t in dp:
            if t + nums[i] == target:
                return True
            tempDP.add(t + nums[i])
            tempDP.add(t)
        dp = tempDP
    
    return True if target in dp else False