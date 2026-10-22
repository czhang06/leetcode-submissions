class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        d = {}
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1

        heap = []
        dq = deque()
        for task in d:
            heapq.heappush(heap, (-d[task]))
        
        time = 0
        while heap or dq:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    dq.append((cnt, time + n))
            if dq and dq[0][1] == time:
                heapq.heappush(heap, dq.popleft()[0])
        
        return time