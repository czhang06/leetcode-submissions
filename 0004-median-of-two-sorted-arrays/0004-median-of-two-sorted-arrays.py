class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            x = (m + n + 1) // 2 - i

            nums1left = float('-inf') if i == 0 else nums1[i - 1]
            nums1right = float('inf') if i == m else nums1[i]

            nums2left = float('-inf') if x == 0 else nums2[x - 1]
            nums2right = float('inf') if x == n else nums2[x]

            if nums1left <= nums2right and nums2left <= nums1right:
                if (m + n) % 2 == 1:
                    return max(nums1left, nums2left)
                else:
                    return (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2.0

            elif nums1left > nums2right:
                right = i - 1
            else:
                left = i + 1
                