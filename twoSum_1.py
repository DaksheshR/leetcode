def twoSum_bruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return([i, j])
    return([])

def twoSum_twoPassHashTable(nums, target):
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
    for i in range(len(nums)):
        if(target - nums[i] in d and d[target - nums[i]] != i):
            return([i, d[target-nums[i]]])
    return([])

def twoSum_onePassHashTable(nums, target):
    d = {}
    for i, v in enumerate(nums):
        if(target-v in d):
            return([d[target-v], i])
        d[v] = i
    return([])

