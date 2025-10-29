class Solution:
    def findMedianSortedArrays(nums1, nums2) -> float:
        mergedNums = sorted(nums1 + nums2)
        n = len(mergedNums)
        if n % 2 == 1:  
            return mergedNums[n // 2]
        else:  
            return (mergedNums[n // 2 - 1] + mergedNums[n // 2]) / 2