class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        return [num for num, freq in items[:k]]