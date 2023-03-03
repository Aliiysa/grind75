def twoSum(nums, target):

    remainings = {}

    for i, num in enumerate(nums):
        difference = target - num

        if difference in remainings:
            return [remainings[difference], i]
        else:
            remainings[num] = i
