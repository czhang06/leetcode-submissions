class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            a = -1 * heapq.heappop(heap)
            b = -1 * heapq.heappop(heap)

            c = a - b
            if c != 0:
                heapq.heappush(heap, -c)
        
        if heap:
            return heap[0] * -1
        else:
            return 0