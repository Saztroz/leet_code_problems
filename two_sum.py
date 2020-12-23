def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]

print(two_sum([2, 7, 9, 15], 24))


def two_sum(nums, target):
    hash = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hash:
            return (i, hash[comp])
        else:
            hash[nums[i]] = i
    return None

print(two_sum([2, 7, 9, 15], 24))