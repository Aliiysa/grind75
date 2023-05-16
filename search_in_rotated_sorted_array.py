def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        medium = (left + right) // 2
        if nums[medium] == target:
            return medium
        if nums[left] <= nums[medium]:
            if target > nums[medium] or target < nums[left]:
                left = medium + 1
            else:
                right = medium - 1
        else:
            if target < nums[medium] or target > nums[right]:
                right = medium - 1
            else:
                left = medium + 1
    return -1