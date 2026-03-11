def threeSum(nums):
    res = []
    dummy = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if(nums[i]+nums[j]+nums[k] == 0):
                    dummy = [nums[i],nums[j],nums[k]]
                    dummy.sort()
                    if dummy not in res:
                        res.append(dummy)
    return res


def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total > 0:
                right -= 1

            elif total < 0:
                left += 1

            else:
                res.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1

                while left < right and nums[right] == nums[right+1]:
                    right -= 1

    return res
