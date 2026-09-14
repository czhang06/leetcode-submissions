import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = []
        for num in nums:
            heapq.heappush(arr, -1 * num)

        for i in range(k - 1):
            heapq.heappop(arr)

        return -1 * heapq.heappop(arr)