def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        medium = (high + low) // 2

        if nums[medium] < target:
            low = medium + 1
        if nums[medium] > target:
            high = medium - 1
        if nums[medium] == target:
            return medium
    return -1

print(search([-1, 0, 3, 5, 9, 12], target=8))