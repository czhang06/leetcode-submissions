class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        res = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res