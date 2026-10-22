class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.count = k
        self.heap = []
        self.k = k

        for n in nums:
            if self.k == 0:
                if n > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, n)
            else:
                heapq.heappush(self.heap, n)
                self.k -= 1


    def add(self, val: int) -> int:
        if self.k == 0:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
            self.k -= 1
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)